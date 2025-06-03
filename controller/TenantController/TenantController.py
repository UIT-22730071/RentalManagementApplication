
from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantHome import TenantHome

from QLNHATRO.RentalManagementApplication.services.TenantService import TenantService


class TenantController:
    def __init__(self,id_tenant):
        pass


    @staticmethod
    def go_to_home_page(view, id_tenant):
        #print(f"[DEBUG] Lấy dữ liệu cho tenant id: {id_tenant}")

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
            #print("[DEBUG] Dữ liệu nhận được:", information_data)
            monthly_data = TenantService.get_tenant_monthly_costs(id_tenant)
            tenant_home = TenantHome(view.main_window, id_tenant, information_data, monthly_data)
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

    @staticmethod
    def go_to_tenant_invoice_list_page(view, id_tenant):
        from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantInvoiceList import TenantListInvoices
        try:
            # Get invoice list data from the service
            invoice_list = TenantService.get_tenant_invoices(id_tenant)
            print(f"[DEBUG] Lấy danh sách hóa đơn cho tenant id: {id_tenant}")
            print(f"[DEBUG] Dữ liệu hóa đơn: {invoice_list}")

            # Create the tenant invoice list view with the data
            tenant_invoice_list = TenantListInvoices(view.main_window, invoice_list, id_tenant)

            # Set the right frame to display the invoice list
            view.set_right_frame(lambda *_: tenant_invoice_list)
        except Exception as e:
            print(f"[ERROR] Không thể lấy dữ liệu hóa đơn: {e}")
            import traceback
            traceback.print_exc()  # Print detailed stack trace
            # If there's an error, create an empty invoice list view
            tenant_invoice_list = TenantListInvoices(view.main_window, None, id_tenant)
            view.set_right_frame(lambda *_: tenant_invoice_list)

    @staticmethod
    def go_to_tenant_find_new_room_page(view, id_tenant):
        try:
            # Gọi service lấy danh sách các phòng đang quảng cáo
            advertised_rooms = TenantService.get_all_advertised_rooms()
            print(f"[DEBUG] Số phòng quảng cáo: {len(advertised_rooms)}")
            from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.FindNewRoom import FindNewRoom
            find_new_room_page = FindNewRoom(view.main_window, advertised_rooms)
            view.set_right_frame(lambda *_: find_new_room_page)

        except Exception as e:
            print(f"[ERROR] Lỗi khi lấy danh sách phòng quảng cáo: {e}")
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.critical(view, "Lỗi", "Không thể tải danh sách phòng quảng cáo.")

    @staticmethod
    def submit_maintenance_request(request_data):
        from QLNHATRO.RentalManagementApplication.services.MaintenanceService import MaintenanceService
        MaintenanceService.create_request(**request_data)
        print("[DEBUG] Gửi yêu cầu sửa chữa:", request_data)

    @staticmethod
    def go_to_tenant_maintenance_request(view, id_tenant):
        from QLNHATRO.RentalManagementApplication.frontend.views.Request.TenantMaintenanceRequest import \
            TenantMaintenanceRequest
        view.set_right_frame(lambda *_: TenantMaintenanceRequest(view.main_window, id_tenant))

    @staticmethod
    def get_room_id_by_tenant(tenant_id):
        return TenantService.get_room_id_by_tenant(tenant_id)
