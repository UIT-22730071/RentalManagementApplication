from QLNHATRO.RentalManagementApplication.Repository.LoginRepository import LoginRepository

from QLNHATRO.RentalManagementApplication.services.LoginService import LoginService


class LoginController:

    def __init__(self):
        self.main_window = None
        self.window = None


    #TODO: chuyển check signUp qua LoginService

    '''
    go to check login xử lý
    gọi Loginservice ==> check_login 
            checklogn ==> gọi LoginRepository ==> get_user
                getuser ==> truy ván sql thực tế lấy đối tượng user ==> trả về True or False
    '''

    @staticmethod
    def on_click_btn_login_test_new(main_window, username, password):
        #print("[LoginController] Bắt đầu xử lý đăng nhập...")

        if LoginService.check_login(username, password):  # user tồn tại trong DB
            user = LoginRepository.get_user(username)
            role = user['role']
            user_id = user['user_id']

            #print(f"[LoginController] Login thành công - Role: {role}, User ID: {user_id}")

            if role == 'landlord':
                from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordMenu import LandlordMenu
                #print("đã import")
                main_window.switch_to_page(LandlordMenu, user_id)
                #print("[LoginController] Đã chuyển sang giao diện LandlordMenu")

            elif role == 'tenant':
                from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantMenu import TenantMenu
                main_window.switch_to_page(TenantMenu, user_id)

            elif role == 'admin':
                from QLNHATRO.RentalManagementApplication.frontend.views.Admin.AdminMenu import AdminMenu
                main_window.switch_to_page(AdminMenu,user_id)
                print("[LoginController] Tạm thời chưa có giao diện Admin")

            else:
                print("[LoginController] Vai trò không hợp lệ")

        else:
            print("[LoginController] Đăng nhập thất bại: Sai tài khoản hoặc mật khẩu")


    '''
    def go_to_main_windown_lanlord(self,main_window ,user_id):
        print(f"[LoginController] sắp MainWindowLandlord với ID: {user_id}")
        id_lanlord = LanlordRepository.get_id_landlord_from_user_id(user_id)
        print(f"ID landlord lấy được: {id_lanlord}")

        try:
            print(">> đang khởi tạo MainWindowLandlord")
            #self.window = MainWindowLandlord(main_window, id_lanlord)
            print(">> đã khởi tạo xong MainWindowLandlord")
        except Exception as e:
            print(f"[ERROR] Lỗi khi khởi tạo MainWindowLandlord với ID: {id_lanlord}")
            print(e)
            traceback.print_exc()

        print(f"[LoginController] Đã tạo MainWindowLandlord với ID: {id_lanlord}")
        self.main_window.setCentralWidget(self.window)
        print(f"[LoginController] Đã setCentralWidget với ID: {id_lanlord}")
        return self.main_window
    '''