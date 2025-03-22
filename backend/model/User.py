import sqlite3


class User:
    def __init__(self, username, password, role, user_id, is_active = 0):
        self.username = username
        self.password = password
        self.role = role
        self.user_id = user_id
        self.is_active = is_active

    @staticmethod
    def add_user(self, username, password, role):
        if self.check_duplicate_user(username):
            print("User already exists")
            return False
        else:
            conn = sqlite3.connect('rentalmanagement.sqlite')
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO Users (Username, Password, Role, IsActive) VALUES (?, ?, ?, ?, ?)""", (username,password, role, 0))
            conn.commit()
            conn.close()
            return True if cursor.rowcount == 1 else False

    @staticmethod
    def check_duplicate_user(self, username):
        conn = sqlite3.connect('rentalmanagement.sqlite')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM Users WHERE Username = ?""", (username,))
        if cursor.fetchone() is not None:
            return True
        else:
            return False

    def checking_password(self, password_input, username):



