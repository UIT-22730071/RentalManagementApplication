import sqlite3

db = 'rent_house_database.sqlite'
class Admin:
    Admin = None

    def __init__(self, admin_id, fullname, user_id):
        self.admin_id = admin_id
        self.fullname = fullname
        self.user_id = user_id

    @staticmethod
    def add_user_to_admin(self, user_id, fullname):
        conn = sqlite3.connect('rentalmanagement.sqlite')
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO Admins(Fullname, UserID) VALUES(?, ?)""", (fullname, user_id))
        admin_id = cursor.lastrowid
        conn.commit()
        conn.close()
        print(f"Admin '{fullname}' added to database with id: {admin_id}")
        return Admin(admin_id, fullname, user_id)

