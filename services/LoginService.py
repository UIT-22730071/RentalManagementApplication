from PyQt5.QtWidgets import QMessageBox

from QLNHATRO.RentalManagementApplication.Repository.LoginRepository import LoginRepository
from QLNHATRO.RentalManagementApplication.controller.LoginRegister.LoginController import LoginController
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.MainWindowLandlord import MainWindowLandlord


class LoginService:
    def __init__(self):
        pass

    landlord_window = None  # thuộc tính class-level

    @staticmethod
    #"admin" "admin"
    def check_login(main_window,username, password):
        # giả lập truy vấn cho ra kết quả
        print("login được gọi")
        user = LoginRepository.get_user(username)
        print(user)
        if username == user['username'] and password == user['password']:
            print("Thực hiện câu lệnh if ")
            print("đã mở Q Mess")
            LoginService.open_dashboard_window(main_window,user['role'],user['user_id'])

        else:
            QMessageBox.information(None, 'Thông báo', 'Sai tên tài khoản hoặc mật khẩu!')

    @staticmethod
    def open_dashboard_window(main_window,role, user_id):
        print(f"[DEBUG] mở dashboard với role={role}, id={user_id}")
        if role == "landlord":
            print(" mở landlord")
            controller = LoginController()
            print("đã mở controller")
            controller.set_main_window(main_window)  # truyền vào controller
            print("đã truyện vào controller")
            controller.go_to_main_windown_lanlord(main_window,user_id)
            print("đợi lanlord")
        elif role == "tenant":
            # controller Điều hướng đến MainWwindowTenant
            print("đợi Tenant")
        else:
            # controller Điều hướng đến MainWwindowAdmin
            print("đợi Admin")

