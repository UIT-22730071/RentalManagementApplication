import sqlite3


class User:
    def __init__(self, username, password, role, user_id, is_active = 0):
        self.username = username
        self.password = password
        self.role = role
        self.user_id = user_id
        self.is_active = is_active


    # Giá trị nạp vào role gồm:
    # TODO: Role only have value (admin, landlord, tenant)
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
    def add_user_to_admin(self, username, password, user_id):
        conn = sqlite3.connect('rentalmanagement.sqlite')
        cursor = conn.cursor()



    @staticmethod
    def check_duplicate_user(self, username):
        print("connect phát")
        conn = sqlite3.connect('rentalmanagement.sqlite')
        print(" neu khong thay t là connect lỗi nha m")
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM Users WHERE Username = ?""", (username,))
        if cursor.fetchone() is not None:
            print("duplicheck True nha ==> next")
            return True
        else:
            return False
            print("duplicheck False nha ==> next")

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


