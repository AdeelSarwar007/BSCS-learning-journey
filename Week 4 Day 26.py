import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

conn.commit()

cursor.execute("DELETE FROM students")

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

conn.commit()

print("\n===== CITY REPORT =====")

cursor.execute("""
SELECT city,
COUNT(*)
FROM students
GROUP BY city
""")

records = cursor.fetchall()

for record in records:
    print(record)

conn.close()

print("\nDay 26 Complete Successfully!")