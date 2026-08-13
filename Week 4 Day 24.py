import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Students Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

# Courses Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses(
    id INTEGER PRIMARY KEY,
    course_name TEXT,
    student_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
""")

conn.commit()

# Insert Students
cursor.execute("INSERT INTO students(name) VALUES('Adeel')")
cursor.execute("INSERT INTO students(name) VALUES('Ali')")

conn.commit()

# Insert Courses
cursor.execute(
"INSERT INTO courses(course_name, student_id) VALUES('Python',1)"
)

cursor.execute(
"INSERT INTO courses(course_name, student_id) VALUES('SQL',1)"
)

cursor.execute(
"INSERT INTO courses(course_name, student_id) VALUES('JavaScript',2)"
)

conn.commit()

print("\n===== INNER JOIN RESULT =====")

cursor.execute("""
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
ON students.id = courses.student_id
""")

records = cursor.fetchall()

for record in records:
    print(record)

conn.close()

print("\nDay 24 Complete Successfully!")