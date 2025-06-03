from QLNHATRO.RentalManagementApplication.Repository.LandlordRepository import LanlordRepository


class LanlordService:
    def __init__(self):  # Đúng
        pass


    @staticmethod
    def update_field(id_lanlord, field, value):
        print(f"[Service] Cập nhật {field} = {value} cho landlord {id_lanlord}")
        LanlordRepository.update_field(id_lanlord, field, value)

    @staticmethod
    def handle_data_for_home_page(id_lanlord):
        #prepare data
        income_last_month, income_last_month_sub_1 = LanlordRepository.get_data_for_handel_percent_income(id_lanlord)
        chart = LanlordRepository.get_chart_income_month(id_lanlord)
        total_income = LanlordRepository.get_total_income_from_all_of_rooms(id_lanlord)
        total_income_sub_1 = LanlordRepository.get_total_income_last_month(id_lanlord)
        total_number_invoice,total_number_invoice_last_month = LanlordRepository.get_total_number_room_have_invoice_not_complete(id_lanlord)
        total_number_room_not_teant,total_rooms_not_tenant_last_month = LanlordRepository.get_to_total_number_not_tenant(id_lanlord)

        #handle data
        percent_grow_income_month = ((income_last_month-income_last_month_sub_1)/income_last_month)*100
        percent_grow_total_income = ((total_income-total_income_sub_1 )/total_income)*100
        percent_grow_total_not_invoice = ((total_number_invoice-total_number_invoice_last_month)/total_number_invoice)*100
        percent_grow_total_not_tenant = ((total_number_room_not_teant-total_rooms_not_tenant_last_month)/total_number_room_not_teant)*100

        information_data = {
            "total_income": total_income,
            "percent_total_income_month": round(percent_grow_income_month, 2),
            "total_number_invoice": total_number_invoice,
            "total_number_room_not_teant": total_number_room_not_teant,
            "percent_grow_total_income": round(percent_grow_total_income, 2),
            "percent_grow_total_not_invoice": round(percent_grow_total_not_invoice, 2),
            "percent_grow_total_not_tenant": round(percent_grow_total_not_tenant, 2)
        }

        return information_data

    @staticmethod
    def handle_data_infor_page(id_lanlord):
        information_data = LanlordRepository.get_infor_lanlord(id_lanlord)
        return information_data

    '''---------------Analyst-----------------'''
    @staticmethod
    def get_dashboard_analyst(self, id_lanlord):
        """
        Lấy dữ liệu phân tích bảng điều khiển cho chủ nhà trọ.
        Query LandlordAnalytics bảng theo landlord_id, lấy 6 tháng gần nhất
        Tính tổng thu nhập, growth, số phòng cho thuê, v.v.
        Trả về dict cho view
        """
        pass
    @staticmethod
    def get_monthly_income(id_lanlord):
        """
        Xử lý dữ liệu phân tích cho chủ nhà trọ.
        Lấy dữ liệu từ LandlordAnalytics, tính toán các chỉ số cần thiết.
        Trả về dict chứa thông tin phân tích.
        """
        data = LanlordRepository.get_landlord_monthly_income(id_lanlord)
        return data



