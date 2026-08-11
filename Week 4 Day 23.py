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
conn.commit()

cursor.execute("INSERT INTO students(name, marks) VALUES('Ali', 85)")
cursor.execute("INSERT INTO students(name, marks) VALUES('Ahmed', 72)")
cursor.execute("INSERT INTO students(name, marks) VALUES('Adeel', 90)")
cursor.execute("INSERT INTO students(name, marks) VALUES('Usman', 65)")

conn.commit()

print("\n===== ALL STUDENTS =====")
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

for student in students:
    print(student)

print("\n===== MARKS GREATER THAN 80 =====")
cursor.execute("SELECT * FROM students WHERE marks > 80")
students = cursor.fetchall()

for student in students:
    print(student)

print("\n===== ORDER BY MARKS DESC =====")
cursor.execute("SELECT * FROM students ORDER BY marks DESC")
students = cursor.fetchall()

for student in students:
    print(student)

print("\n===== TOP 2 STUDENTS =====")
cursor.execute("SELECT * FROM students LIMIT 2")
students = cursor.fetchall()

for student in students:
    print(student)

# Close Connection
conn.close()

print("\nDay 23 Complete Successfully!")