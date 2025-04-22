


class TenantRepository:

    @staticmethod
    def get_room_infor_by_id_tenant(tenant_id):
        #TODO: Tạo truy vấn lấy id_room từ teantn_id ==> sau đó xử lý
        id_room = '01'
        #TODO: Tạo truy vấn lấy thông tin phòng từ id_room
        raw_data_room = {
            "id": '01',
            "room_name": "Phong A",
            "address": "A18, Tân Đô, Hải Sơn",
            "room_type": "Đơn",
            "area": "20",
            "rent_price": 1500000,
            "deposit": 1500000,
            "electricity_price": 3000,
            "water_price": 20000,
            "internet_price": 150000,
            'garbage_price': 30000,
            "other_fees": 20000,
            "available_date": "05/05/2020",
            "current_electricity": 300,
            "current_water":20,
            "tenant_id": '01',
            "landlord_id": '01'
        }
        return raw_data_room

    @staticmethod
    def get_chart_income_month(id_tenant):
        #TODO: Truy vấn trả về 1 chart sau khi chạy file phân tích
        chart = "0"
        return chart

    @staticmethod
    def get_tenant_data_for_invoice_view(tenant_id):
        # TODO: Thay thế bằng truy vấn SQL thực tế
        tenant_data = {
            'full_name': 'Chưa có dữ liệu',
            'citizen_id': 'Chưa có dữ liệu',
            'address': 'Khu Phố 6, Phường Linh Trung, Thành phố Thủ Đức, TP Hồ Chí Minh',
            'phone': 'Chưa có dữ liệu'
        }
        return tenant_data

    @staticmethod
    def get_number_e_and_number_w_from(tenant_id, month, year):
        data ={
            "number_e" : 120,
            "number_w" : 30
        }
        return data




    @staticmethod
    def get_all_tenants():
        """Lấy danh sách tất cả các người thuê từ database"""
        # TODO: Thay thế bằng truy vấn SQL thực tế
        tenants = [
            {
                'id': 'T001',
                'ho_ten': 'Nguyễn Văn A',
                'cccd': '012345678901',
                'sdt': '0901234567',
                'email': 'nguyenvana@email.com',
                'so_nguoi': 2
            },
            {
                'id': 'T002',
                'ho_ten': 'Trần Thị B',
                'cccd': '098765432109',
                'sdt': '0909876543',
                'email': 'tranthib@email.com',
                'so_nguoi': 1
            }
        ]
        return tenants

    @staticmethod
    def get_tenant_by_id(tenant_id):
        """Lấy thông tin người thuê từ id"""
        # TODO: Thay thế bằng truy vấn SQL thực tế

        # tenant chỉ chưa các thông tin của tenant dạng dict để truy vấn

        for tenant in TenantRepository.get_all_tenants():
            if tenant['id'] == tenant_id:
                return tenant
        return None

    @staticmethod
    def get_tenant_by_cccd(cccd):
        """Lấy thông tin người thuê từ số CCCD"""
        # TODO: Thay thế bằng truy vấn SQL thực tế
        tenant = {
            'name': "Phúc",
            'cccd': "082098013220",
            'phone': "0325575333",
            'email': "hoangphuc@gmail.com",
        }

        return tenant

    @staticmethod
    def get_tenant_by_room_id(room_id):
        """Lấy thông tin người thuê từ id phòng"""
        # TODO: Thay thế bằng truy vấn SQL thực tế JOIN
        room_tenant_mapping = {
            'P101': 'T001',
            'P102': 'T002'
        }
        tenant_id = room_tenant_mapping.get(room_id)
        if tenant_id:
            return TenantRepository.get_tenant_by_id(tenant_id)
        return None

    @staticmethod
    def get_tenant_id_from_user_id(user_id):
        # TODO: Thay thế bằng truy ván SQL thực tế
        tenant_id = '1'
        return tenant_id

    @staticmethod
    def get_data_for_tenant_home_page(id_tenant,month,year):
        #TODO: Có thể lấy dữ liệu trong hóa đơn gần nhất
        data = {
            'tien_dien': 1000000,
            'tien_nuoc': 2000000,
            'tong_chi_phi': 3000000,
            'ngay_den_han': '2023-12-31'
        }
        return data
    @staticmethod
    def get_month_with_last_invoice(id_tenant):
        # TODO: Thay thế bằng truy vấn SQL thực tế
        # Lấy tháng và năm của hóa đơn gần nhất
        month = 12
        year = 2024
        return month,year

    @staticmethod
    def get_tenant_infor_by_id_tenant(id_tenant):
        #TODO: Tạo hàm lấy dữ liêu người dùng
        default_data = {
            'full_name': 'Trần Văn Ở Thuê',
            'birth_date': '1998-01-01',
            'citizen_id': '083098103250',
            'gender': 'Nam',
            'occupation': 'Nhân viên',
            'phone_number': '036513251',
            'marital_status': 'độc toàn thân'
        }
        return default_data
    @staticmethod
    def update_tenant_info(tenant_id, updated_data):
        """
        Cập nhật thông tin người thuê trong database.
        :param tenant_id: ID người thuê
        :param updated_data: dict dữ liệu mới
        :return: True nếu cập nhật thành công, False nếu có lỗi
        """
        try:
            # Ví dụ sử dụng SQL (giả lập):
            query = "UPDATE tenants SET "
            fields = []
            values = []

            for key, value in updated_data.items():
                fields.append(f"{key} = ?")
                values.append(value)

            query += ", ".join(fields)
            query += " WHERE id = ?"
            values.append(tenant_id)

            print(f"[SQL] {query} | {values}")

            # TODO: thực thi query bằng cursor.execute(query, values)
            # cursor.commit()

            return True  # Trả về True nếu cập nhật thành công

        except Exception as e:
            print(f"[ERROR] Không thể cập nhật tenant: {e}")
            return False
