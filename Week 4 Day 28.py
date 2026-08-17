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

def add():
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    cursor.execute(
        "INSERT INTO students(name, marks) VALUES(?, ?)",
        (name, marks)
    )

    conn.commit()
    print("Student Added Successfully")

def show():
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if len(students) == 0:
        print("No Records Found")
    else:
        print("\n--- Student Records ---")
        for student in students:
            print(student)

def update():
    student_id = int(input("Enter Student ID: "))
    marks = int(input("Enter New Marks: "))

    cursor.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (marks, student_id)
    )

    conn.commit()
    print("Student Updated Successfully")

def delete():
    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    print("Student Deleted Successfully")

def search():
    name = input("Enter Name: ")

    cursor.execute(
        "SELECT * FROM students WHERE name=?",
        (name,)
    )

    students = cursor.fetchall()

    for student in students:
        print(student)
def report():
    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )
    print("Total Students:", cursor.fetchone()[0])

    cursor.execute(
        "SELECT AVG(marks) FROM students"
    )
    print("Average Marks:", cursor.fetchone()[0])

    cursor.execute(
        "SELECT MAX(marks) FROM students"
    )
    print("Highest Marks:", cursor.fetchone()[0])

    cursor.execute(
        "SELECT MIN(marks) FROM students"
    )
    print("Lowest Marks:", cursor.fetchone()[0])

while True:

    print("\n1.Add Student")
    print("2.Show Students")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Report")
    print("7.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add()

    elif choice == "2":
        show()

    elif choice == "3":
        search()

    elif choice == "4":
        update()

    elif choice == "5":
        delete()

    elif choice == "6":
        report()

    elif choice == "7":
        break

conn.close()