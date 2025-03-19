import sqlite3

conn = sqlite3.connect('rentalmanagement.sqlite')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE Users (
        id INT,
        username VARCHAR(50),
        password VARCHAR(20)
    );
''')

conn.commit()

cursor.execute("SELECT * FROM Users")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

# Testing Github - Try: 2