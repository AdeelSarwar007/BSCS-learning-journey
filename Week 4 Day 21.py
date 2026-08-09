import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Add Student
def add():
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    cursor.execute(
        "INSERT INTO students(name, marks) VALUES(?, ?)",
        (name, marks)
    )

    conn.commit()
    print("Student Added Successfully")


# Show Students
def show():
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if len(students) == 0:
        print("No Records Found")
    else:
        print("\n--- Student Records ---")
        for student in students:
            print(student)


# Update Student
def update():
    student_id = int(input("Enter Student ID: "))
    marks = int(input("Enter New Marks: "))

    cursor.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (marks, student_id)
    )

    conn.commit()
    print("Student Updated Successfully")
