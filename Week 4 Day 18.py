import sqlite3

conn = sqlite3.connect("library.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    book TEXT
)
""")

conn.commit()

print("Database Connected")
print("Teachers Table Created Successfully")

conn.close()
