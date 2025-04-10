INSERT INTO Department (department_name) VALUES
('Computer Science'),
('Information Technology'),
('Electronics and Communication'),
('Artificial Intelligence & Data Science'),
('Artificial Intelligence & Machine Learning');

INSERT INTO Courses (course_name, department_id, faculty_id) VALUES
('Database Management Systems', 1, 1),  -- CSE
('Database Management Systems', 2, 8),  -- IT
('Database Management Systems', 3, 15), -- ECE
('Database Management Systems', 4, 22), -- AIDS
('Database Management Systems', 5, 29), -- AIML

('Operating Systems', 1, 2),  
('Operating Systems', 2, 9),  
('Operating Systems', 3, 16),  
('Operating Systems', 4, 23),  
('Operating Systems', 5, 30),  

('Computer Networks', 1, 3),  
('Computer Networks', 2, 10),  
('Computer Networks', 3, 17),  
('Computer Networks', 4, 24),  
('Computer Networks', 5, 31),  

('Data Structures & Algorithms', 1, 4),  
('Data Structures & Algorithms', 2, 11),  
('Data Structures & Algorithms', 3, 18),  
('Data Structures & Algorithms', 4, 25),  
('Data Structures & Algorithms', 5, 32),  

('Software Engineering', 1, 5),  
('Software Engineering', 2, 12),  
('Software Engineering', 3, 19),  
('Software Engineering', 4, 26),  
('Software Engineering', 5, 33);

-- Unique Courses for Each Department
INSERT INTO Courses (course_name, department_id, faculty_id) VALUES
('Machine Learning', 1, 6),  
('Cloud Computing', 1, 7),  

('Cyber Security', 2, 13),  
('Web Technologies', 2, 14),  

('Embedded Systems', 3, 20),  
('VLSI Design', 3, 21),  

('Deep Learning', 4, 27),  
('Big Data Analytics', 4, 28),  

('Natural Language Processing', 5, 34),  
('Computer Vision', 5, 35);