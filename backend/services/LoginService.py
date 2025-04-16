from PyQt5.QtWidgets import QMessageBox

from QLNHATRO.RentalManagementApplication.backend.Repository.LoginRepository import LoginRepository


class LoginService:
    def __init__(self):
        pass

    landlord_window = None  # thuộc tính class-level


    # xử lý 1 vấn đề là check user tồn tại và password đúng
    @staticmethod
    #"admin" "admin"
    def check_login(username, password):
        # giả lập truy vấn cho ra kết quả
        print("login được gọi")
        user = LoginRepository.get_user(username)
        print(user)
        if username == user['username'] and password == user['password']:
            print("user và passowrd đúng rồi")
            #LoginService.open_dashboard_window_and_close_login(login_window, user['role'], int(user['user_id']))
            return True
        else:
            QMessageBox.information(None, 'Thông báo', 'Sai tên tài khoản hoặc mật khẩu!')
            return False


    @staticmethod
    def get_role_user(user_id):
        role = LoginRepository.get_role_from_user_id(user_id)   # giả sủ role = landlord
        print(f"[DEBUG] mở dashboard với, id={user_id}")
        return role

    @staticmethod
    def open_dashboard_window_and_close_login(role, user_id):
        pass

    @staticmethod
    def close_main_window(main_window):
        main_window.close()