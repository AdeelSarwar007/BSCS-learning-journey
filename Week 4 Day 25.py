import sqlite3

# Database Connection
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

conn.commit()

# Insert Data
cursor.execute("INSERT INTO students(name,marks) VALUES('Adeel',90)")
cursor.execute("INSERT INTO students(name,marks) VALUES('Ali',85)")
cursor.execute("INSERT INTO students(name,marks) VALUES('Ahmed',70)")
cursor.execute("INSERT INTO students(name,marks) VALUES('Usman',60)")

conn.commit()

print("\n===== ALL STUDENTS =====")

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

# COUNT
print("\n===== TOTAL STUDENTS =====")

cursor.execute(
    "SELECT COUNT(*) FROM students"
)

total_students = cursor.fetchone()

print("Total Students:", total_students[0])

# AVG
print("\n===== AVERAGE MARKS =====")

cursor.execute(
    "SELECT AVG(marks) FROM students"
)

average_marks = cursor.fetchone()

print("Average Marks:", average_marks[0])

# MAX
print("\n===== HIGHEST MARKS =====")

cursor.execute(
    "SELECT MAX(marks) FROM students"
)

highest_marks = cursor.fetchone()

print("Highest Marks:", highest_marks[0])

# MIN
print("\n===== LOWEST MARKS =====")

cursor.execute(
    "SELECT MIN(marks) FROM students"
)

lowest_marks = cursor.fetchone()

print("Lowest Marks:", lowest_marks[0])

# SUM
print("\n===== TOTAL MARKS =====")

cursor.execute(
    "SELECT SUM(marks) FROM students"
)

total_marks = cursor.fetchone()

print("Total Marks:", total_marks[0])

conn.close()

print("\nDay 25 Complete Successfully!")