import sqlite3
import os

class Database:
    def __init__(self, db_filename="rent_house_database.sqlite"):
        # Lấy đường dẫn tuyệt đối đến thư mục hiện tại
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Ghép đường dẫn đến file .sqlite
        self.db_path = os.path.join(base_dir, db_filename)
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            print(f"[INFO] Đã kết nối tới: {self.db_path}")
        except sqlite3.Error as e:
            print(f"[LỖI] Không thể kết nối DB: {e}")

    def execute(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return self.cursor
        except sqlite3.Error as e:
            print(f"[LỖI] Lỗi truy vấn: {e}")
            return None

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        if self.conn:
            self.conn.close()
            print("[INFO] Kết nối đã được đóng.")
