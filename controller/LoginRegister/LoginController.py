from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.MainWindowLandlord import MainWindowLandlord
from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.UpdateInfoAfterRegister import \
    UpdateInfoAfterRegister

from QLNHATRO.RentalManagementApplication.backend.model.User import User




class LoginController():

    def __init__(self):

        self.main_window = None
        self.window = None

    def set_main_window(self, main_window):
        self.main_window = main_window

    def go_to_check_login(self,email,password):
        pass

    def go_to_open_workspace(self):
        pass

    def open_update_info(self, role_text, username, password):
        print(f"[DEBUG] role_text={role_text}, username={username}, password={password}")
        update_form = UpdateInfoAfterRegister(self.main_window, role_text, username, password)
        self.main_window.setCentralWidget(update_form)

    def go_to_exsit(self,main_window):
        main_window.close()
        pass
    #TODO: chuyển check signUp qua LoginService
    def go_to_check_sign_up(self, username, password, password_confirm, role, main_window=None):
        # Kiểm tra main_window nếu chưa thiết lập
        if self.main_window is None and main_window is not None:
            self.set_main_window(main_window)

        # Giả sử hàm check_password_not_equal trả về True nếu mật khẩu KHÔNG trùng khớp
        if User.check_password_not_equal(password, password_confirm):
            if role:  # role là boolean True => Người thuê trọ
                role_text = "Người thuê trọ"
                role_user = "tenant"
            else:
                role_text = "Chủ trọ"
                role_user = "landlord"

            # User.add_user(username, password, role_user)  # Mở khi backend sẵn sàng
            print("tao goi add user ròi nha, neu nó đóng lỗi ở ko phải ở t đó")

            self.open_update_info(role_text, username, password)
            print(" t goi open update info")

    def go_to_main_windown_lanlord(self,main_window ,id_lanlord):
        print(f"[LoginController] sắp MainWindowLandlord với ID: {id_lanlord}")
        try:
            self.window = MainWindowLandlord(main_window, id_lanlord)
        except:
            print(f"lỗi ở đây: {id_lanlord}")

        print(f"[LoginController] Đã tạo MainWindowLandlord với ID: {id_lanlord}")
        self.main_window.setCentralWidget(self.window)
        print(f"[LoginController] Đã setCentralWidget với ID: {id_lanlord}")