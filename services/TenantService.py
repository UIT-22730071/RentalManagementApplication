from calendar import month

from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository


class TenantService:
    @staticmethod
    def get_tenant_by_cccd(cccd):
        """Tìm người thuê theo CCCD"""
        tenant =  TenantRepository.get_tenant_by_cccd(cccd)
        for tenant in TenantRepository.get_all_tenants():
            if tenant['cccd'] == cccd:
                data_tenant_show = {
                    'name_tenant': tenant['name'],
                    'cccd': tenant['cccd'],
                    'phone': tenant['sdt'],
                    'email': tenant['email'],
                }
                return data_tenant_show
        return None

    @staticmethod
    def get_tenant_by_room_id(room_id):
        """Lấy thông tin người thuê theo id phòng"""
        return TenantRepository.get_tenant_by_room_id(room_id)

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
