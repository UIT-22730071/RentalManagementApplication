import sqlite3

# Đường dẫn tới database và file schema.sql
db_path = r"H:\My Drive\01.UIT\HK7\03.DOAN\QLNHATRO\RentalManagementApplication\backend\database\rent_house_database.sqlite"
schema_file = r"H:\My Drive\01.UIT\HK7\03.DOAN\QLNHATRO\RentalManagementApplication\backend\database\init_db.sql"

def initialize_database():
    try:
        with sqlite3.connect(db_path) as conn:
            with open(schema_file, 'r', encoding='utf-8') as f:
                sql_script = f.read()
                conn.executescript(sql_script)
                print("✅ Database schema has been initialized successfully.")
    except Exception as e:
        print(f"❌ Lỗi khi khởi tạo schema: {e}")

if __name__ == "__main__":
    initialize_database()
