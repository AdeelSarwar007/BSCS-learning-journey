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


# Delete Student
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

    if len(students) == 0:
        print("No Record Found")

    else:
        for student in students:
            print(student)

def topper():
    cursor.execute(
        "SELECT * FROM students ORDER BY marks DESC LIMIT 1"
    )

    student = cursor.fetchone()

    print("\nTopper:")
    print(student)

# Menu
while True:
    print("\n---------- Menu ----------")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Topper Student")
    print("7. Exit")

    choice = input("Enter Number: ")

    if choice == "1":
        add()

    elif choice == "2":
        show()

    elif choice == "3":
        update()

    elif choice == "4":
        delete()

    elif choice == "5":
        search()

    elif choice == "6":
        topper()

    elif choice == "7":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice")

conn.close()