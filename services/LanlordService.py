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
        #chart = LanlordRepository.get_chart_income_month(id_lanlord)
        total_income = LanlordRepository.get_total_income_from_all_of_rooms(id_lanlord)
        total_income_sub_1 = LanlordRepository.get_total_income_last_month(id_lanlord)
        total_number_invoice, total_number_invoice_last_month = LanlordRepository.get_total_number_room_have_invoice_not_complete(
            id_lanlord)
        total_number_room_not_tenant, total_rooms_not_tenant_last_month = LanlordRepository.get_to_total_number_not_tenant(
            id_lanlord)

        # Xử lý các trường hợp có thể gây lỗi chia cho 0
        percent_grow_income_month = ((income_last_month - income_last_month_sub_1) / income_last_month * 100) if income_last_month else 0
        percent_grow_total_income = ((total_income - total_income_sub_1) / total_income * 100) if total_income else 0
        percent_grow_total_not_invoice = ((total_number_invoice - total_number_invoice_last_month) / total_number_invoice * 100) if total_number_invoice else 0
        percent_grow_total_not_tenant = ((total_number_room_not_tenant - total_rooms_not_tenant_last_month) / total_number_room_not_tenant * 100) if total_number_room_not_tenant else 0

        information_data = {
            "total_income": total_income,
            "percent_total_income_month": round(percent_grow_income_month, 2),
            "total_number_invoice": total_number_invoice,
            "total_number_room_not_tenant": total_number_room_not_tenant,
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

    @staticmethod
    def get_complete_analytics_data(id_landlord):
        """
        Lấy toàn bộ dữ liệu analytics để hiển thị dashboard
        """
        try:
            analytics_data = LanlordRepository.get_landlord_analytics_data(id_landlord)

            if not analytics_data:
                print("⚠️ Không có dữ liệu analytics")
                return None

            return {
                'monthly_income': [{'month': item['month'], 'total_income': item['total_income']} for item in
                                   analytics_data],
                'room_occupancy': [{'month': item['month'], 'rented_rooms': item['rented_rooms']} for item in
                                   analytics_data],
                'average_price': [{'month': item['month'], 'average_price': item['average_price']} for item in
                                  analytics_data],
                'growth_rate': [{'month': item['month'], 'growth_rate': item['growth_rate']} for item in
                                analytics_data],
                'raw_data': analytics_data
            }
        except Exception as e:
            print(f"❌ Lỗi get_complete_analytics_data: {e}")
            return None

    @staticmethod
    def get_dashboard_summary(id_landlord):
        """
        Tính toán các chỉ số tóm tắt cho dashboard
        """
        try:
            analytics_data = LanlordRepository.get_landlord_analytics_data(id_landlord)

            if not analytics_data or len(analytics_data) < 2:
                return None

            current_month = analytics_data[-1]  # Tháng gần nhất
            previous_month = analytics_data[-2] if len(analytics_data) > 1 else analytics_data[-1]

            # Tính các chỉ số
            total_income = current_month['total_income']
            income_change = ((current_month['total_income'] - previous_month['total_income']) / previous_month[
                'total_income'] * 100) if previous_month['total_income'] > 0 else 0

            current_rooms = current_month['rented_rooms']
            room_change = current_rooms - previous_month['rented_rooms']

            avg_price = current_month['average_price']
            price_change = ((current_month['average_price'] - previous_month['average_price']) / previous_month[
                'average_price'] * 100) if previous_month['average_price'] > 0 else 0

            current_growth = current_month['growth_rate']

            return {
                'total_income': total_income,
                'income_change_percent': round(income_change, 1),
                'current_rented_rooms': current_rooms,
                'room_change': room_change,
                'average_price': avg_price,
                'price_change_percent': round(price_change, 1),
                'growth_rate': current_growth,
                'trend': 'up' if income_change > 0 else 'down' if income_change < 0 else 'stable'
            }
        except Exception as e:
            print(f"❌ Lỗi get_dashboard_summary: {e}")
            return None
