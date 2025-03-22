import sqlite3

conn = sqlite3.connect('rentalmanagement.sqlite')

cursor = conn.cursor()

# Initialize Database Script
with open('init_db.sql', 'r') as db_file:
    init_sql_script = db_file.read()

# Reset Database Script
with open('query_script.sql', 'r') as reset_database:
    reset_sql_script = reset_database.read()

cursor.executescript(init_sql_script)

conn.commit()

cursor.execute("SELECT * FROM Users")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()