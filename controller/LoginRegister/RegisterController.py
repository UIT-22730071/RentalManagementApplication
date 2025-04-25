from PyQt5.QtWidgets import QMessageBox

from QLNHATRO.RentalManagementApplication.backend.model.Admin import Admin
from QLNHATRO.RentalManagementApplication.backend.model.User import User



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
    @staticmethod
    def register_tenant(username, password,confirm_password ,role, main_window):
        from QLNHATRO.RentalManagementApplication.services.LoginService import LoginService
        if not username or not password or not confirm_password:
            print("Username and password are required.")
            return
        elif LoginService.check_confim_password(password, confirm_password):
            # lưu trữ dữ liệu username
            user = [username, password, role]
            # Gọi Service xử lý và gọi hàm cập nhật user mới
            # Đồng thời khi reposibily trả về true thì xác nhận mở form cập nhật thông tin cho người dùng
            LoginService.handle_data_user_to_create_new_user(user,main_window)
            # Hàm trên xử lý gọi tạo mới dữ liệu và nếu tạo mới thành công sẽ call mở luôn form cập nhật thông tin
        else:
            QMessageBox.warning(None, "Lỗi xác nhận", "🔐 Xác nhận mật khẩu không khớp!")
            return
