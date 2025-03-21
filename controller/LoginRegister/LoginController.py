from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.UpdateInfoAfterRegister import \
    UpdateInfoAfterRegister
from QLNHATRO.RentalManagementApplication.backend.model.User import check_password_not_equal



class LoginController():

    def __init__(self):
        self.main_window = None

    def go_to_check_login(self,email,password):
        pass

    def go_to_open_workspace(self):
        pass

    def open_update_info(self, role, username, password):
        self.main_window.setCentralWidget(UpdateInfoAfterRegister(role))

    def go_to_sign_up(self, username, password, password_confirm, role):
        check = check_password_not_equal(password, password_confirm)
        if check == True:
            self.open_update_info(role, username, password)

        else:
            pass

    def go_to_exsit(self,main_window):
        main_window.close()
        pass