import sqlite3

# Path to your SQLite database file
db_path = 'database_rental_management.db'

# Schema file containing your SQL commands
schema_file = 'database_rental_management.sql'

# Connect to the SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect(db_path)

try:
    # Read the schema from the file
    with open(schema_file, 'r', encoding='utf-8') as file:
        schema = file.read()

    # Execute the schema
    conn.executescript(schema)
    print("Database initialized successfully.")
except Exception as e:
    print(f"Error initializing database: {e}")
finally:
    conn.close()