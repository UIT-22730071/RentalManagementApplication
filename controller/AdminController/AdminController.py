from PyQt5.QtWidgets import QApplication
from QLNHATRO.RentalManagementApplication.Repository.LandlordRepository import LanlordRepository
from QLNHATRO.RentalManagementApplication.Repository.UserRepository import UserRepository
from QLNHATRO.RentalManagementApplication.frontend.views.Admin.UserManagerView import AdminUserManagement
from QLNHATRO.RentalManagementApplication.services.AdminService import AdminService

class AdminController:

    _user_windows = []

    @staticmethod
    def go_to_home(view):
        from QLNHATRO.RentalManagementApplication.frontend.views.Admin.AdminHomePage import AdminHome
        from QLNHATRO.RentalManagementApplication.services.AdminService import AdminService

        summary_data = AdminService.get_summary_dashboard_data_with_growth()
        monthly_data = AdminService.get_system_stats_by_month()
        admin_home = AdminHome(view.main_window, summary_data, monthly_data)
        view.set_right_frame(lambda *_: admin_home)

    @staticmethod
    def go_to_user_management(view):

        user_list = AdminService.get_all_users()  # Tạm thời có thể mock
        view.set_right_frame(lambda: AdminUserManagement(view.main_window, user_list))

    @staticmethod
    def go_to_landlord_list(view):
        from QLNHATRO.RentalManagementApplication.frontend.views.Admin.AdminLandlordList import AdminLandlordList
        # Tạm thời dùng mock data; sau này sẽ gọi từ AdminService
        landlord_list = AdminService.get_all_landlords()
        view.set_right_frame(lambda: AdminLandlordList(view.main_window, landlord_list))

    @staticmethod
    def go_to_tenant_list(view):
        from QLNHATRO.RentalManagementApplication.frontend.views.Admin.AdminTenantList import AdminTenantList
        tenant_list = AdminService.get_all_tenants()  # Hoặc dữ liệu giả lập
        view.set_right_frame(lambda: AdminTenantList(view.main_window, tenant_list))

    @staticmethod
    def go_to_room_list(view):
        from QLNHATRO.RentalManagementApplication.frontend.views.Admin.AdminRoomList import AdminRoomList
        room_list = AdminService.get_all_rooms()  # Dữ liệu thật hoặc giả lập
        view.set_right_frame(lambda: AdminRoomList(view.main_window, room_list))

    @staticmethod
    def go_to_invoice_list(view):
        #print("[INFO] Điều hướng đến Danh sách hóa đơn")

        from QLNHATRO.RentalManagementApplication.frontend.views.Admin.AdminInvoiceList import AdminInvoiceList
        from QLNHATRO.RentalManagementApplication.services.AdminService import AdminService

        invoice_list = AdminService.get_all_invoices_for_admin()
        view.set_right_frame(lambda: AdminInvoiceList(view.main_window, invoice_list))

    @staticmethod
    def handle_exit(view):
        print("[INFO] Đóng ứng dụng")
        QApplication.quit()

    @staticmethod
    def handel_exit_window(view):
        view.main_window.close()
    '''--------------------------------------------------------------------'''

    @staticmethod
    def go_to_open_infor_lanlord(username):
        from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordInfo import LandlordInfo
        from QLNHATRO.RentalManagementApplication.frontend.Component.UserInfoWindow import UserInfoWindow

        user_id = UserRepository.get_user_id_from_username(username)
        id_landlord = LanlordRepository.get_id_landlord_from_user_id(user_id)

        from QLNHATRO.RentalManagementApplication.services.LanlordService import LanlordService
        information_data = LanlordService.handle_data_infor_page(id_landlord)

        content_widget = LandlordInfo(None, id_landlord, information_data)
        window = UserInfoWindow(content_widget, title=f"Thông tin Chủ trọ: {username}")
        window.show()
        window.activateWindow()
        AdminController._user_windows.append(window)



    @staticmethod
    def go_to_infor_tenant(username):
        from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantInfo import TenantInfo
        from QLNHATRO.RentalManagementApplication.frontend.Component.UserInfoWindow import UserInfoWindow
        from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository

        user_id = UserRepository.get_user_id_from_username(username)
        id_tenant = TenantRepository.get_tenant_id_from_user_id(user_id)

        from QLNHATRO.RentalManagementApplication.services.TenantService import TenantService
        initial_data = TenantService.get_tenant_infor(id_tenant)  # ✅ dùng hàm đúng để lấy data cá nhân
        content_widget = TenantInfo(None, initial_data, id_tenant)

        window = UserInfoWindow(content_widget, title=f"Thông tin Người thuê: {username}")
        window.show()
        window.activateWindow()
        AdminController._user_windows.append(window)

    @staticmethod
    def open_infor_admin_page(username):
        from QLNHATRO.RentalManagementApplication.frontend.views.Admin.AdminInfor import AdminInfo
        window = AdminInfo()
        window.show()
        window.activateWindow()
        AdminController._user_windows.append(window)

    '''--------------------------------------------------------------------'''