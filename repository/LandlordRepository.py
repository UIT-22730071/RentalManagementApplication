


class LanlordRepository:

    @staticmethod
    def get_landlord_data_for_invoice_view(id_lanlord):
        # TODO: Tao truy vấn SLQ select * from landlords where id
        landlord_data = {
            'name': 'Chưa có dữ liệu',
            'cccd': 'Đang cập nhật',
            'address': 'Khu Phố 6, Phường Linh Trung, Thành phố Thủ Đức, TP Hồ Chí Minh',
            'phone': 'Chưa có dữ liệu'
        }
        return landlord_data


    @staticmethod
    def get_all_landlords():
        #TODO: Tao truy vấn SLQ select * from landlords
        landlords = [
            {
                'id': 'L001',
                'ho_ten': 'Nguyễn Văn A',
                'cccd': '012345678901',
                'sdt': '0901234567',
                'email': 'nguyenvana@email.com',
                'so_phong': 2
            },
            {
                'id': 'L002',
                'ho_ten': 'Trần Thị B',
                'cccd': '098765432109',
                'sdt': '0909876543',
                'email': 'tranthib@email.com',
                'so_phong': 1
            }
        ]
        return landlords

    @staticmethod
    def get_id_landlord_from_user_id(user_id):
        #TODO: Tao truy vấn SLQ select landlord_id from landlords where user_id = ?
        id_lanlord = '1'
        return id_lanlord

    #-------------Lanlord Home --------------
    #TODO: sau khi có dữ liệu ảo thống kê sẽ vẽ biểu đồ
    '''return của hàm sẽ là 1 char'''
    @staticmethod
    def get_chart_income_month(id_lanlord):
        chart = "0"
        return chart

    @staticmethod
    def get_total_income_from_all_of_rooms(id_landlord):
        #TODO tạo 1 hàm select oll of income from all of Incoice
        total_income = 100000000
        return total_income
    @staticmethod
    def get_total_income_last_month(id_lanlord):
        #TODO taoj 1 hamf select tổng thu nhập tính đến tháng - 1 để tính % tang truỏng
        total_incom_mont_sub_1 = 95000000
        return total_incom_mont_sub_1

    @staticmethod
    def get_data_for_handel_percent_income(id_lanlord):
        #TODO tọa 1 hàm select all of income of 2 lose month (near)
        ''' data sẽ chuyển qua LanlordService xủ lý'''
        income_last_month = 30000000
        income_last_month_sub_1 = 28000000
        return income_last_month,income_last_month_sub_1

    @staticmethod
    def get_total_number_room_have_invoice_not_complete(id_lanlord):
        #TODO tạo 1 hàm select all of number invoice chua đóng tiền
        total_number_invoice = 3
        total_number_invoice_last_month = 2
        return total_number_invoice,total_number_invoice_last_month
    @staticmethod
    def get_to_total_number_not_tenant(id_lanlord):
        #TODO tạo 1ham fselect all of số phòng chua có người thuê
        total_number_room_not_teant = 2
        total_rooms_not_tenant_last_month = 3
        return total_number_room_not_teant,total_rooms_not_tenant_last_month
    # -------------Lanlord Infor --------------
    @staticmethod
    def get_infor_lanlord(id_lanlord):
        #TODO tạo 1 hàm select infor lanlord gom cac thong tin
        infor_lanlord = {
            'name': 'Nguyễn Văn A',
            'birth':'13/12/1998',
            'cccd': '012345678901',
            'sex': 'Nam',
            'job': 'Sinh viện',
            'phone': '0901234567',
            'marriage': 'Độc thân',
            'password': '**********'}
        return infor_lanlord

    @staticmethod
    def update_field(id_lanlord, field, value):
        # TODO: Viết truy vấn SQL update database
        print(f"[Repository] Update field `{field}` = {value} cho landlord {id_lanlord}")
        # Ví dụ (giả lập):
        # UPDATE landlords SET field = value WHERE id = id_lanlord;
