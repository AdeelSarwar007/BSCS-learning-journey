import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute("""
CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

conn.commit()

cursor.execute(
"INSERT INTO students(name,city) VALUES('Adeel','Vehari')"
)

cursor.execute(
"INSERT INTO students(name,city) VALUES('Ali','Lahore')"
)

cursor.execute(
"INSERT INTO students(name,city) VALUES('Ahmed','Vehari')"
)

cursor.execute(
"INSERT INTO students(name,city) VALUES('Usman','Lahore')"
)

cursor.execute(
"INSERT INTO students(name,city) VALUES('Bilal','Multan')"
)

conn.commit()

print("\n===== HAVING REPORT =====")

cursor.execute("""
SELECT city,
COUNT(*)
FROM students
GROUP BY city
HAVING COUNT(*) > 1
""")

records = cursor.fetchall()

for record in records:
    print(record)

conn.close()

print("\nDay 27 Complete Successfully!")