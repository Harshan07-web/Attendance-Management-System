from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from datetime import date
current_date = date.today().isoformat()

app = Flask(__name__)
app.secret_key = "supersecretkey123" 

# MySQL Database Configuration
app.config['MYSQL_HOST'] = 'localhost'  
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = 'Harshan17'  
app.config['MYSQL_DB'] = 'attendancemanagement'  
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  

mysql = MySQL(app)

# Home Page Route
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/mark_attendance', methods=['GET', 'POST'])
def mark_attendance():
    if 'faculty_id' not in session:
        return redirect(url_for('login'))

    faculty_id = session['faculty_id']

    cur = mysql.connection.cursor()
    cur.execute("SELECT course_id, course_name FROM courses WHERE faculty_id = %s", (faculty_id,))
    courses = cur.fetchall()

    selected_course_id = request.args.get('course_id')
    selected_date = request.args.get('attendance_date')  
    students = []

    if selected_course_id and selected_date:
        cur.execute("""
            SELECT s.roll_number, s.name, s.student_id
            FROM students s
            JOIN enrollments e ON s.student_id = e.student_id
            WHERE e.course_id = %s
        """, (selected_course_id,))
        students = cur.fetchall()

    cur.close()
    return render_template(
        'mark_attendance.html',
        courses=courses,
        students=students,
        selected_course_id=selected_course_id,
        selected_date=selected_date,
        current_date=current_date
    )

@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    if 'faculty_id' not in session:
        return redirect(url_for('login'))

    faculty_id = session['faculty_id']
    course_id = request.form.get('course_id')
    attendance_date = request.form.get('attendance_date')  
    cur = mysql.connection.cursor()

    for key, value in request.form.items():
        if key.startswith('attendance_'):
            student_id = key.split('_')[1].strip()
            if student_id.isdigit():
                attendance_status = value
                cur.execute(
                    "INSERT INTO attendance (student_id, course_id, date, status) VALUES (%s, %s, %s, %s) "
                    "ON DUPLICATE KEY UPDATE status = VALUES(status)",
                    (int(student_id), int(course_id), attendance_date, attendance_status)
                )

    cur.execute(
        "SELECT f.name AS faculty_name, d.department_name AS department_name "
        "FROM faculty f "
        "JOIN department d ON f.department_id = d.department_id "
        "WHERE f.faculty_id = %s", (faculty_id,)
    )
    faculty_info = cur.fetchone()
    faculty_name = faculty_info['faculty_name'] if faculty_info else "N/A"
    depart_name = faculty_info['department_name'] if faculty_info else "N/A"

    cur.execute(
        "select course_name from courses where course_id = %s",(course_id,)
    )
    course_info = cur.fetchone()
    course_name = course_info['course_name'] if course_info else "N/A"


    mysql.connection.commit()
    cur.close()
    flash("Attendance submitted successfully!", "success")
    return render_template('confirmation_pg.html', cname=course_name, attendance_date=attendance_date ,fname =faculty_name ,dname = depart_name )


# View Attendance Route (For Faculty & Students)
@app.route('/view_attendance', methods=['GET', 'POST'])
def view_attendance():
    attendance_data = None
    course_name = None  

    if request.method == 'POST':
        student_id = request.form['student_id']
        department_id = request.form['department_id']

        cur = mysql.connection.cursor()

       
        cur.execute("SELECT * FROM students WHERE student_id = %s AND department_id = %s", (student_id, department_id))
        student = cur.fetchone()

        if student:
            
            cur.execute("""
                SELECT c.course_name, a.status, a.date
                FROM attendance a
                JOIN courses c ON a.course_id = c.course_id
                WHERE a.student_id = %s
                ORDER BY a.date DESC
            """, (student_id,))
            attendance_data = cur.fetchall()

        cur.close()

    return render_template('view_attendance.html', attendance_data=attendance_data)

# Faculty Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        department_id = request.form.get('department_id')

        cur = mysql.connection.cursor()
        query = "SELECT faculty_id, username, department_id FROM faculty WHERE username = %s AND password = %s AND department_id = %s"
        cur.execute(query, (username, password, department_id))
        faculty = cur.fetchone()
        cur.close()

        if faculty:
            session['logged_in'] = True
            session['faculty_id'] = faculty['faculty_id']
            session['username'] = username
            session['department_id'] = department_id
            flash("Login Successful", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid Credentials. Please try again.", "error")

    return render_template("login.html")

# Dashboard Route (Faculty After Login)
@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        return render_template("dashboard.html", username=session['username'], department_id=session['department_id'])
    else:
        flash("You must log in first.", "error")
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()  
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

# Help & Support Page
@app.route('/help')
def help():
    return render_template("help.html")

if __name__ == '__main__':
    app.run(debug=True)
