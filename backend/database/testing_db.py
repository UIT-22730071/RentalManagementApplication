import sqlite3
import os

# ✅ Đường dẫn tuyệt đối đến file CSDL
db_path = r"H:\My Drive\01.UIT\HK7\03.DOAN\QLNHATRO\RentalManagementApplication\backend\database\rent_house_database.sqlite"

def test_database_connection():
    if not os.path.exists(db_path):
        print(f"❌ Database file không tồn tại: {db_path}")
        return

    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # Cho phép truy cập theo tên cột
        cursor = conn.cursor()

        print(f"✅ Đã kết nối tới: {db_path}")

        # Lấy danh sách bảng
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        if not tables:
            print("⚠️ CSDL chưa có bảng nào.")
        else:
            print("📋 Danh sách bảng có trong CSDL:")
            for t in tables:
                print("   -", t["name"])

        conn.close()
        print("🔒 Kết nối đã đóng.")
    except sqlite3.Error as e:
        print(f"❌ Lỗi kết nối hoặc truy vấn CSDL: {e}")

# Gọi hàm test
if __name__ == "__main__":
    test_database_connection()
