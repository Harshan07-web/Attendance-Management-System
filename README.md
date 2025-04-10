## Flask Attendance Management System

A simple web-based attendance management system built using Flask, designed for educational institutions to manage and view attendance records of students.

---

## 🚀 Features

- Faculty login and dashboard
- Mark attendance for students by course
- View attendance reports (faculty and student views)
- Secure authentication (session-based)
- Organized template structure using Jinja2
- SQLite backend for quick setup and usage

---

## 🧠 Technologies Used

- **Python**
- **Flask**
- **MySQL**
- **HTML & CSS**

---

## 📁 Project Structure

Attendance-Management-System/  
│  
├── app.py                   
├── templates/               # HTML files  
├── static/                  # CSS/JS/Images  
├── database/                # SQL files  
├── requirements.txt         # Dependencies   
├── README.md                # Project description  
└── LICENSE                    

---

## 🧪 Setup Instructions

1. **Clone the repository**
   
   git clone https://github.com/Harshan07-web/Attendance-Management-System.git
   cd Attendance-Management-System

2. **Create virtual environment (optional but recommended)**

    python -m venv venv
    venv\Scripts\activate   # On Windows

3. **Install dependencies**
   
    pip install -r requirements.txt

4. **Set up the database**

    Execute the SQL scripts in /database to create and populate the database tables (using SQLite or DB browser).

5. **Run the application**

    python app.py

---

## 📚 To-Do / Future Enhancements

-Student login with password authentication  
-Attendance analytics (graphs, percentages)  
-CSV/PDF export of attendance data  
-Admin panel for managing users and courses  
-Add a faculty attendance   

---

## License

-This project is licensed under the MIT License.


