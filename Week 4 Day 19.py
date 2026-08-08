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

    print("\n--- Student Records ---")

    for student in students:
        print(student)

# Menu
while True:
    print("\n---------- Menu ----------")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter Number: ")

    if choice == "1":
        add()

    elif choice == "2":
        show()

    elif choice == "3":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice")

conn.close()