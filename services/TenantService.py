
from datetime import datetime



from QLNHATRO.RentalManagementApplication.Repository.InvoiceRepository import InvoiceRepository
from QLNHATRO.RentalManagementApplication.Repository.LandlordRepository import LanlordRepository
from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository


class TenantService:

    @staticmethod
    def get_tenant_by_room_id(room_id: int):
        """Lấy tenant theo RoomID và trả về dict đơn giản cho UI"""
        tenant_obj = TenantRepository.get_tenant_by_room_id(room_id)
        if tenant_obj is None:
            print(f"[⚠️ TenantService] Không có tenant gắn với RoomID: {room_id}")
            return None

        return {
            'name_tenant': tenant_obj.fullname,
            'cccd': tenant_obj.cccd,
            'phone': tenant_obj.phone_number,
            'email': tenant_obj.email
        }

    @staticmethod
    def get_tenant_by_cccd(cccd: str):
        """Trả về dict đơn giản (dùng cho hiển thị UI) từ đối tượng Tenant"""
        tenant_obj = TenantRepository.get_tenant_by_cccd(cccd)
        if tenant_obj is None:
            print(f"[⚠️ TenantService] Không có tenant với CCCD: {cccd}.")
            return None

        return {
            'name_tenant': tenant_obj.fullname,
            'cccd': tenant_obj.cccd,
            'phone': tenant_obj.phone_number,
            'email': tenant_obj.email
        }

    @staticmethod
    def handle_data_for_tenant_home_page(id_tenant):
        from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository
        month,year = TenantRepository.get_month_with_last_invoice(id_tenant)
        month_last, year_last = TenantService.get_previous_month_and_year(month,year)
        # Lấy dữ liệu sử dụng từ repository (giả lập, bạn cần thay bằng SQL thật)
        data_this_month = TenantRepository.get_data_for_tenant_home_page(id_tenant,month,year)
        data_last_month = TenantRepository.get_data_for_tenant_home_page(id_tenant,month_last,year_last)

        # Tính toán phần trăm thay đổi
        def calc_percent(current, previous):
            if previous == 0:
                return 0.0
            return round((current - previous) / previous * 100, 1)

        percent_electric = calc_percent(data_this_month['tien_dien'], data_last_month['tien_dien'])
        percent_water = calc_percent(data_this_month['tien_nuoc'], data_last_month['tien_nuoc'])
        percent_total = calc_percent(data_this_month['tong_chi_phi'], data_last_month['tong_chi_phi'])

        # Lấy chart từ repository
        chart = TenantRepository.get_chart_income_month(id_tenant)

        # Trả về cả data và chart
        return {
            "tien_dien": data_this_month['tien_dien'],
            "tien_nuoc": data_this_month['tien_nuoc'],
            "tong_chi_phi": data_this_month['tong_chi_phi'],
            "ngay_den_han": data_this_month['ngay_den_han'],
            "percent_dien": percent_electric,
            "percent_nuoc": percent_water,
            "percent_total": percent_total
        }, chart

    @staticmethod
    def get_previous_month_and_year(month, year):
        if month == 1:
            return 12, year - 1
        else:
            return month - 1, year

    @staticmethod
    def get_tenant_infor(id_tenant):
        #TODO: nếu có thay đổi trong xử lý data thì hiệu chỉnh
        data = {} # nếu có xử lý thì hiệu chỉnh
        raw_data = TenantRepository.get_tenant_infor_by_id_tenant(id_tenant)
        return raw_data

    @staticmethod
    def update_tenant_info(tenant_id, updated_data):
        from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository
        print(f"[SERVICE] Đang cập nhật tenant {tenant_id} với dữ liệu: {updated_data}")
        return TenantRepository.update_tenant_info(tenant_id, updated_data)

    @staticmethod
    def handle_data_for_tenant_room_infor(tenant_id):
        from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository
        all_data = []
        raw_data_room = TenantRepository.get_room_infor_by_id_tenant(tenant_id)

        landlord_id = raw_data_room['landlord_id']
        raw_data_lanlord = LanlordRepository.get_infor_lanlord(landlord_id)

        date_new_invoice = InvoiceRepository.get_date_new_invoice_of_room(tenant_id)
        '''date_new_invoice = "06-04-25"'''
        try:
            date_obj = datetime.strptime(date_new_invoice, "%d-%m-%Y")
        except ValueError:
            date_obj = datetime.strptime(date_new_invoice, "%d-%m-%y")

        # Trích xuất tháng và năm
        month = date_obj.month
        year = date_obj.year

        pre_month, pre_year = (12, year - 1) if month == 1 else (month - 1, year)
        old_data_e_and_w = TenantRepository.get_number_e_and_number_w_from(tenant_id, month, year)
        current_data_e_and_w = TenantRepository.get_number_e_and_number_w_from(tenant_id, pre_month, pre_year)

        # Xử lý rawdata
        data_room ={
            "Số phòng":str(raw_data_room['room_name']),
            "Loại phòng":str(raw_data_room['room_type']),
            "Ngày bắt đầu thuê":str(raw_data_room['available_date']),
            "Tiền phòng":str(raw_data_room['rent_price'])+" VNĐ",
            "Tiền cọc":str(raw_data_room['deposit'])+" VNĐ",
            "Ngày đến hạn thanh toán":str(date_new_invoice),
            "Diện tích":str(raw_data_room['area']),

            "Chỉ số điện cũ":str(old_data_e_and_w["number_e"])+" kWh",
            "Chỉ số điện mới":str(current_data_e_and_w["number_e"])+" kWh",
            "Tiêu thụ điện":str(current_data_e_and_w['number_e']- old_data_e_and_w["number_e"])+" kWh",
            "Đơn giá điện":str(raw_data_room['electricity_price'])+" VNĐ/kWh",
            "Thành tiên điện":str((current_data_e_and_w['number_e']- old_data_e_and_w["number_e"])*raw_data_room['electricity_price'])+" VNĐ",

            "Chỉ số nước cũ:":str(old_data_e_and_w["number_w"])+" m³",
            "Chỉ số nước mới":str(current_data_e_and_w["number_w"])+" m³",
            "Tiêu thụ nước":str(current_data_e_and_w['number_w']- old_data_e_and_w["number_w"])+" m³",
            "Đơn giá nước":str(raw_data_room['water_price'])+" VNĐ/m³",
            "Thành tiên nước": str((current_data_e_and_w['number_w'] - old_data_e_and_w["number_w"]) * raw_data_room[
                'water_price']) + " VNĐ",

            "Chi phí khác":str(raw_data_room["other_fees"])+" VNĐ",
            "Internet":str(raw_data_room['internet_price']) + " VNĐ/tháng",
            "Tiền rác":str(raw_data_room['garbage_price']) + " VNĐ/tháng",
            "Tổng cộng":str(raw_data_room['rent_price']+(current_data_e_and_w['number_e']- old_data_e_and_w["number_e"])*raw_data_room['electricity_price'] + (current_data_e_and_w['number_w'] - old_data_e_and_w["number_w"]) * raw_data_room[
                'water_price']+raw_data_room["other_fees"]+raw_data_room['internet_price'])+ " VNĐ",

            "Tên chủ trọ":str(raw_data_lanlord['name']),
            "Số điện thoại":str(raw_data_lanlord['phone']),
            "Email":str(raw_data_lanlord['email']),
            "Địa chỉ":str(raw_data_room['address']),

        }

        return data_room

    @staticmethod
    def get_tenant_invoices(id_tenant):
        """
        Get all invoices for a specific tenant

        Args:
            id_tenant: The ID of the tenant

        Returns:
            A list of invoice data formatted for display
        """
        # Get raw invoice data from repository
        raw_invoices = InvoiceRepository.get_invoices_by_tenant_id(id_tenant)

        # Process the invoice data for display
        formatted_invoices = []
        for invoice in raw_invoices:
            # Calculate electricity and water usage
            electricity_usage = invoice['new_electricity'] - invoice['old_electricity']
            water_usage = invoice['new_water'] - invoice['old_water']

            # Calculate costs
            electricity_cost = electricity_usage * invoice['electricity_price']
            water_cost = water_usage * invoice['water_price']

            # Calculate total amount
            total_amount = (
                    invoice['rent_price'] +
                    electricity_cost +
                    water_cost +
                    invoice['internet_price'] +
                    invoice.get('garbage_fee', 0) +
                    invoice.get('other_fees', 0)
            )

            # Format the invoice for display
            formatted_invoice = {
                'invoice_id': invoice['invoice_id'],
                'date': invoice['created_date'],
                'room_name': invoice['room']['room_name'],
                'rent_price': f"{invoice['rent_price']:,} VNĐ",
                'electricity': f"{electricity_usage} kWh ({electricity_cost:,} VNĐ)",
                'water': f"{water_usage} m³ ({water_cost:,} VNĐ)",
                'internet': f"{invoice['internet_price']:,} VNĐ",
                'other_fees': f"{invoice.get('other_fees', 0):,} VNĐ",
                'total_amount': f"{total_amount:,} VNĐ",
                'status': 'Đã thanh toán' if invoice.get('is_paid', False) else 'Chưa thanh toán',
                'raw_data': invoice  # Keep the raw data for possible detailed view
            }

            formatted_invoices.append(formatted_invoice)

        # Sort invoices by date (newest first)
        formatted_invoices.sort(key=lambda x: x['date'], reverse=True)

        print(f"[SERVICE] Formatted invoices for tenant {id_tenant}: {formatted_invoices}")
        return formatted_invoices

    @staticmethod
    def get_all_advertised_rooms():
        from QLNHATRO.RentalManagementApplication.Repository.AdvertisementRepository import AdvertisementRepository
        return AdvertisementRepository.get_all_advertised_rooms()


    tenant_room_mapping = {
        1: 101,
        2: 102,
        3: 103
    }

    @staticmethod
    def get_room_id_by_tenant(tenant_id):
        room_id = TenantService.tenant_room_mapping.get(tenant_id)
        print(f"[DEBUG][Service] room_id của tenant {tenant_id} là {room_id}")
        return room_id

    @staticmethod
    def get_tenant_monthly_costs(id_tenant):
        # Call repository to get monthly costs data
        monthly_costs = TenantRepository.get_tenant_monthly_costs(id_tenant)
        #print(f"[DEBUG] Monthly costs for tenant {id_tenant}: {monthly_costs}")
        return monthly_costs