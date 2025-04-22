from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantHome import TenantHome
from QLNHATRO.RentalManagementApplication.services.TenantService import TenantService


class TenantController:
    def __init__(self,id_tenant):
        pass


    @staticmethod
    def go_to_home_page(view, id_tenant):
        print(f"[DEBUG] Lấy dữ liệu cho tenant id: {id_tenant}")

        try:
            information_data, chart = TenantService.handle_data_for_tenant_home_page(id_tenant)
            ''' data được trả về
                                "tien_dien": data_this_month['tien_dien'],
                                    "tien_nuoc": data_this_month['tien_nuoc'],
                                    "tong_chi_phi": data_this_month['tong_chi_phi'],
                                    "ngay_den_han": data_this_month['ngay_den_han'],
                                    "percent_dien": percent_electric,
                                    "percent_nuoc": percent_water,
                                    "percent_total": percent_total
                                '''
            print("[DEBUG] Dữ liệu nhận được:", information_data)
            tenant_home = TenantHome(view.main_window, id_tenant, information_data, chart)
            view.set_right_frame(lambda *_: tenant_home)
        except Exception as e:
            print(f"[ERROR] Không thể lấy dữ liệu: {e}")
            tenant_home = TenantHome(view.main_window, id_tenant)
            view.set_right_frame(lambda *_: tenant_home)

    @staticmethod
    def go_to_tenant_info_page(view, id_tenant):
        from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantInfo import TenantInfo
        initial_data = TenantService.get_tenant_infor(id_tenant)
        tenant_info = TenantInfo(view.main_window, initial_data, id_tenant)
        view.set_right_frame(lambda *_: tenant_info)


    @staticmethod
    def go_to_tenant_room_infor_page(view,id_tenant):
        from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantRoomInfo import TenantRoomInfo
        data_room =  TenantService.handle_data_for_tenant_room_infor(id_tenant)
        tenant_room_infor = TenantRoomInfo(view.main_window,data_room,id_tenant)
        view.set_right_frame(lambda *_: tenant_room_infor)