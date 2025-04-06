import sqlite3
#TODO ?

class Admin():
    def __init__(self, admin_id, fullname, is_root = 1, user_id):
        self.admin_id = admin_id
        self.fullname = fullname
        self.is_root = is_root
        self.user_id = user_id

