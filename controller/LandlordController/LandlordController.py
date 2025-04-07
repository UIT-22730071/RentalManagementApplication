from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordCreateNewRoom import CreateNewRoom
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordFindNewTenant import FindNewTenant
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordHome import LandlordHome
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordInfo import LandlordInfo
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordListInvoices import ListInvoices
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.RoomList import RoomList
from QLNHATRO.RentalManagementApplication.services.LanlordService import LanlordService


class LandlordController:


    @staticmethod
    def go_to_home_page(view, id_lanlord):
        information_data, chart = LanlordService.handle_data_for_home_page(id_lanlord)
        print("đây là information",information_data)
        landlord_home = LandlordHome(view.main_window, id_lanlord, information_data, chart)
        view.set_right_frame(lambda *_: landlord_home)  # ✅ truyền widget đã tạo

    @staticmethod
    def go_to_info_page(view):
        view.set_right_frame(LandlordInfo)

    @staticmethod
    def go_to_room_list(view):
        view.set_right_frame(RoomList)

    @staticmethod
    def go_to_create_room(view):
        view.set_right_frame(CreateNewRoom)

    @staticmethod
    def go_to_invoice_list(view):
        view.set_right_frame(ListInvoices)

    @staticmethod
    def go_to_find_tenant(view):
        view.set_right_frame(FindNewTenant)