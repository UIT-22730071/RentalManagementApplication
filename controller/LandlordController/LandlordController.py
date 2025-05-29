from PyQt5.QtWidgets import QApplication


from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordHome import LandlordHome
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordListInvoices import ListInvoices
from QLNHATRO.RentalManagementApplication.services.InvoiceService import InvoiceService
from QLNHATRO.RentalManagementApplication.services.LanlordService import LanlordService
from QLNHATRO.RentalManagementApplication.services.RoomService import RoomService

from QLNHATRO.TestErrorUI.MainWindowLogin import MainWindow


class LandlordController:
    def __init__(self):
        pass

    @staticmethod
    def update_landlord_field(id_lanlord, field, value):
        LanlordService.update_field(id_lanlord, field, value)

    @staticmethod
    def go_to_home_page(view, id_lanlord):
        information_data, chart = LanlordService.handle_data_for_home_page(id_lanlord)
        print("đây là information",information_data)
        lanlord_home = LandlordHome(view.main_window, id_lanlord, information_data, chart)
        view.set_right_frame(lambda *_: lanlord_home)  # ✅ truyền widget đã tạo

    @staticmethod
    def go_to_info_page(view,id_lanlord):
        information_data = LanlordService.handle_data_infor_page(id_lanlord)
        print("đây là information của infor",information_data)
        from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordInfo import LandlordInfo
        lanlord_infor = LandlordInfo(view.main_window,id_lanlord ,information_data)
        view.set_right_frame(lambda *_: lanlord_infor)

    @staticmethod
    def go_to_room_list(view, id_lanlord):
        room_list = RoomService.handle_data_for_room_list_page(id_lanlord)
        print("đây là room list",room_list)
        from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.RoomList import RoomList
        room_list_view = RoomList(view.main_window, room_list, id_lanlord)
        view.set_right_frame(lambda *_: room_list_view)

    @staticmethod
    def go_to_invoice_list(view, id_lanlord):
        invoice_list = InvoiceService.handle_data_for_invoice_list_page(id_lanlord)
        print("đây là invoice list", invoice_list)
        invoice_list_view = ListInvoices(view.main_window, invoice_list, id_lanlord)
        view.set_right_frame(lambda *_: invoice_list_view)

    @staticmethod
    def handle_logout(view):
        """Quay về màn hình đăng nhập"""
        from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.HomeLogin import LoginWindow
        #print("[INFO] Đăng xuất khỏi dashboard landlord...")

        main_window = view.main_window
        login_widget = LoginWindow(main_window)  # truyền lại main_window nếu cần

        # Đặt lại central widget
        main_window.setCentralWidget(login_widget)

        # Reset kích thước chuẩn
        main_window.resize(800, 620)
        main_window.setMinimumSize(825, 600)
        main_window.setMaximumSize(825, 600)

        # Reset tiêu đề
        main_window.setWindowTitle("Đăng nhập hệ thống")

    @staticmethod
    def handle_exit():
        print("[INFO] Đóng ứng dụng")
        QApplication.quit()

    @staticmethod
    def go_to_LanlordFindNewTenant(view, id_lanlord):
        from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordFindNewTenant import FindNewTenant
        ds_phong = RoomService.get_list_room_by_id_landlord(id_lanlord)
        find_new_tenant_view = FindNewTenant(view.main_window, ds_phong=ds_phong)
        view.set_right_frame(lambda *_: find_new_tenant_view)