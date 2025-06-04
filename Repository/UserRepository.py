import hashlib

from QLNHATRO.RentalManagementApplication.backend.database.Database import Database
from QLNHATRO.RentalManagementApplication.backend.model.User import User

class UserRepository:
    db = Database()

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def add_user(username, password, role) -> User | None:

        is_active = 1 if role == "admin" else 0
        hashed_pw = UserRepository.hash_password(password)

        try:
            UserRepository.db.connect()
            query = """INSERT INTO Users (Username, Password, Role, IsActive)
                       VALUES (?, ?, ?, ?)"""
            cursor = UserRepository.db.execute(query, (username, hashed_pw, role, is_active))
            if cursor:
                user_id = cursor.lastrowid
                print(f"Đã thêm user '{username}' với ID: {user_id}")
                return User(username, hashed_pw, role, user_id, is_active)
        except Exception as e:
            print(f"Lỗi khi thêm user: {e}")
        finally:
            if UserRepository.db: UserRepository.db.close()
        return None

    @staticmethod
    def check_duplicate_user(username: str) -> bool:
        try:
            UserRepository.db.connect()
            query = "SELECT 1 FROM Users WHERE Username = ?"
            cursor = UserRepository.db.execute(query, (username,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Lỗi check duplicate user: {e}")
            return False
        finally:
            UserRepository.db.close()

    @staticmethod
    def get_user_by_username(username: str) -> User | None:
        try:
            UserRepository.db.connect()
            query = """SELECT UserID, Username, Password, Role, IsActive
                       FROM Users \
                       WHERE Username = ?"""
            cursor = UserRepository.db.execute(query, (username,))
            row = cursor.fetchone()
            if row:
                return User(row["Username"], row["Password"], row["Role"], row["UserID"], row["IsActive"])
            print(f"⚠Không tìm thấy user: {username}")
        except Exception as e:
            print(f"Lỗi khi lấy user theo username: {e}")
        finally:
            UserRepository.db.close()
        return None

    @staticmethod
    def validate_password(username: str, password_input: str) -> bool:
        user = UserRepository.get_user_by_username(username)
        if not user:
            return False
        hashed_input = UserRepository.hash_password(password_input)
        return user.password == hashed_input

    @staticmethod
    def get_user_id_from_username(username: str) -> int | None:
        try:
            UserRepository.db.connect()
            query = "SELECT UserID FROM Users WHERE Username = ?"
            cursor = UserRepository.db.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                return result[0]
            print(f"Không tìm thấy UserID cho username: {username}")
        except Exception as e:
            print(f"Lỗi get_user_id_from_username: {e}")
        finally:
            UserRepository.db.close()
        return None

    @staticmethod
    def delete_user_by_username(username: str):
        """
        Xóa user khỏi bảng Users dựa vào Username.
        Yêu cầu CSDL có FOREIGN KEY ON DELETE CASCADE để xóa dữ liệu liên quan.
        """
        db = Database()
        if db.connect():
            try:
                # Kiểm tra user có tồn tại không
                check_query = "SELECT * FROM Users WHERE Username = ?"
                cursor = db.execute(check_query, (username,))
                user = cursor.fetchone() if cursor else None

                if user is None:
                    print(f"[WARNING] Không tìm thấy user có Username: {username}")
                    return False

                # Xóa user
                delete_query = "DELETE FROM Users WHERE Username = ?"
                result = db.execute(delete_query, (username,))

                if result and result.rowcount > 0:
                    print(f"[INFO] Đã xóa user: {username}")
                    return True
                else:
                    print(f"[WARNING] Không thể xóa user: {username}")
                    return False

            except Exception as e:
                print(f"[LỖI] Lỗi khi xóa user: {e}")
                return False
            finally:
                db.close()
        else:
            print("[LỖI] Không thể kết nối tới database.")
            return False