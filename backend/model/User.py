import sqlite3

class User:
    User = None

    def __init__(self, username, password, role, user_id=None, is_active = 0):
        self.username = username
        self.password = password
        self.role = role
        self.user_id = user_id
        self.is_active = is_active


    @staticmethod
    def add_user (username, password, role):
        if  User.check_duplicate_user(username):
            print(f"User with username: '{username}' already exists")
            return None
        else:
            conn = sqlite3.connect('rentalmanagement.sqlite')
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO Users(Username, Password, Role, IsActive) VALUES (?, ?, ?, ?)""", (username, password, role, 1 if role == "admin" else 0))
            user_id = cursor.lastrowid
            conn.commit()
            conn.close()
            print(f"User with username: '{username}' added to database successfully with ID: {user_id}")
            return User(username, password, role, user_id)


    @staticmethod
    def check_duplicate_user(username):
        conn = sqlite3.connect('rentalmanagement.sqlite')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Users WHERE Username = ?""", (username,))
        return cursor.fetchone() is not None

    @staticmethod
    def get_user_by_username(username):
        conn = sqlite3.connect('rentalmanagement.sqlite')
        cursor = conn.cursor()
        cursor.execute("""SELECT UserID, """)

    @staticmethod
    def check_correct_password(password_input, username):
        conn = sqlite3.connect('rentalmanagement.sqlite')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT Password FROM Users WHERE Username = ?""", (username,))
        if cursor.fetchone() == password_input:
            return True
        else:
            return False


    @staticmethod
    def check_password_not_equal(password, password_confirm):
        if password == password_confirm:
            return True
        else:
            return False


