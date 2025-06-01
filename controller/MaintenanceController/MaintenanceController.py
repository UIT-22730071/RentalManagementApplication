
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.RoomMaintenanceList import RoomMaintenanceList


class MaintenanceController:
    def __init__(self, maintenanceService):
        pass

    @staticmethod
    def go_to_maintenance_list(view, id_landlord):
        from QLNHATRO.RentalManagementApplication.services.MaintenanceService import MaintenanceService
        maintenance_list = MaintenanceService.get_maintenance_list(id_landlord)
        maintenance_list_view = RoomMaintenanceList(view.main_window, maintenance_list, id_landlord)
        view.set_right_frame(lambda *_: maintenance_list_view)

    @staticmethod
    def go_to_maintenance_detail_page(view, request_data):
        from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.MaintenanceRequestDetail import \
            MaintenanceRequestDetail

        detail_view = MaintenanceRequestDetail(request_data, parent=view.main_window)
        main_window = view.main_window
        main_window.setCentralWidget(detail_view)

