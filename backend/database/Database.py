import sqlite3
import os
from typing import List, Optional, Tuple


class Database:
    def __init__(self, db_filename="identifier.sqlite"):
        # Lấy đường dẫn tuyệt đối đến thư mục hiện tại
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Ghép đường dẫn đến file .sqlite
        self.db_path = r"H:\My Drive\01.UIT\HK7\03.DOAN\QLNHATRO\RentalManagementApplication\backend\database\rent_house_database.sqlite"

        self.conn = None
        self.cursor = None

    def connect(self):
        """Kết nối đến database"""
        try:
            self.conn = sqlite3.connect(self.db_path)
            # Thiết lập Row factory để trả về dict thay vì tuple
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
            print(f"[INFO] Đã kết nối tới: {self.db_path}")
            return True
        except sqlite3.Error as e:
            print(f"[LỖI] Không thể kết nối DB: {e}")
            return False

    def execute(self, query, params=None):
        """Thực thi câu lệnh SQL"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return self.cursor
        except sqlite3.Error as e:
            print(f"[LỖI] Lỗi truy vấn: {e}")
            #self.conn.rollback()  # Rollback khi có lỗi
            return None

    def fetchall(self) -> List[sqlite3.Row]:
        """Lấy tất cả kết quả"""
        return self.cursor.fetchall()

    def fetchone(self) -> Optional[sqlite3.Row]:
        """Lấy một kết quả"""
        return self.cursor.fetchone()

    def close(self):
        """Đóng kết nối database"""
        if self.conn:
            self.conn.close()
            print("[INFO] Kết nối đã được đóng.")

    def execute_many(self, query: str, params_list: List[Tuple]) -> bool:
        """Thực thi nhiều câu lệnh SQL cùng lúc"""
        try:
            self.cursor.executemany(query, params_list)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"[LỖI] Lỗi execute_many: {e}")
            self.conn.rollback()
            return False