from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordCreateNewRoom import CreateNewRoom
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordFindNewTenant import FindNewTenant
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordHome import LandlordHome
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordListInvoices import ListInvoices
from QLNHATRO.RentalManagementApplication.services.LanlordService import LanlordService
from QLNHATRO.RentalManagementApplication.services.RoomService import RoomService


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
    def go_to_create_room(view):
        view.set_right_frame(CreateNewRoom)

    @staticmethod
    def go_to_invoice_list(view):
        view.set_right_frame(ListInvoices)

    @staticmethod
    def go_to_find_tenant(view):
        view.set_right_frame(FindNewTenant)

