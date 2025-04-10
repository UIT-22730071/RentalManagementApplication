from backend.model import User
from backend.model import Admin

class RegisterController:
    def __init__(self):
        self.user_model = User
        self.admin_model = Admin

    def register_admin(self, username, password, role, fullname):
        if not username or not password:
            print("Username and password are required.")
            return

        try:
            user = self.user_model.User.add_user(username, password, role)
            self.admin_model.Admin.add_user_to_admin(user.user_id, fullname)
            print("Registered successfully.")
        except Exception as e:
            print(f"Error: {e}")

    # def register_tenant(self, username, password, role):