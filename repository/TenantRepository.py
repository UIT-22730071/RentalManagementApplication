from QLNHATRO.RentalManagementApplication.backend.database.Database import Database
from QLNHATRO.RentalManagementApplication.backend.model.Tenant import Tenant

db = Database()
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
        try:
            db.connect()
            query = """
                    SELECT T.TenantID, \
                           T.Fullname, \
                           T.Birth, \
                           T.CCCD, \
                           T.Gender, \
                           T.JobTitle, \
                           T.MaritalStatus, \
                           T.Email, \
                           T.PhoneNumber, \
                           T.HomeAddress, \
                           T.RentStartDate, \
                           T.RentEndDate, \
                           T.UserID, \
                           U.Username
                    FROM Tenants T
                             LEFT JOIN Users U ON T.UserID = U.UserID \
                    """
            cursor = db.execute(query)
            rows = cursor.fetchall() if cursor else []
            db.close()
            return [Tenant(dict(r)) for r in rows]
        except Exception as e:
            print(f"❌ Lỗi get_all_tenants: {e}")
            return []

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
    def get_tenant_by_cccd(cccd: str):
        """Trả về đối tượng Tenant từ số CCCD"""
        from QLNHATRO.RentalManagementApplication.backend.database.Database import Database
        from QLNHATRO.RentalManagementApplication.backend.model.Tenant import Tenant

        db = Database()
        db.connect()
        query = """
                SELECT * \
                FROM Tenants \
                WHERE CCCD = ? \
                """
        cursor = db.execute(query, (cccd,))
        row = cursor.fetchone()
        db.close()

        if row:
            columns = [column[0] for column in cursor.description]
            data = dict(zip(columns, row))
            return Tenant(data)  # ✅ Trả về đối tượng Tenant
        else:
            print(f"[⚠️ TenantRepository] Không tìm thấy tenant với CCCD: {cccd}")
            return None

    @staticmethod
    def get_tenant_by_room_id(room_id: int):
        from QLNHATRO.RentalManagementApplication.backend.database.Database import Database
        from QLNHATRO.RentalManagementApplication.backend.model.Tenant import Tenant

        db = Database()
        db.connect()
        query = """
                SELECT t.* \
                FROM Tenants t \
                         JOIN Rooms r ON t.TenantID = r.TenantID
                WHERE r.RoomID = ? \
                """
        cursor = db.execute(query, (room_id,))
        row = cursor.fetchone()
        db.close()

        if row:
            columns = [column[0] for column in cursor.description]
            data = dict(zip(columns, row))
            return Tenant(data)
        else:
            print(f"[⚠️ TenantRepository] Không tìm thấy tenant gắn với RoomID: {room_id}")
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
            'email':"tranvanthuetro@gmail.com",
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

    @staticmethod
    def get_user_id_from_id_tenant(id_tenant):
        #TODO: tạo truy vấn lấy dữ liêu data trả về user_id
        user_id = '1'
        return user_id

    @staticmethod
    def update_user_info(user_id, data):
        # TODO: Thực hiện truy vấn UPDATE SQL
        print(f"[DB] Đã cập nhật user_id={user_id} với data={data}")

    @staticmethod
    def get_tenant_id_from_user_name(username):
        tenant_id = 1
        return tenant_id

    @staticmethod
    def get_tenant_monthly_costs(id_tenant):
        # Truy vấn hóa đơn hoặc bảng analytics (nếu có)
        # Dưới đây là data mẫu:
        data = [
            {"month": "01/2024", "tien_dien": 200000, "tien_nuoc": 120000, "tong": 700000},
            {"month": "02/2024", "tien_dien": 240000, "tien_nuoc": 150000, "tong": 800000},
            {"month": "03/2024", "tien_dien": 180000, "tien_nuoc": 130000, "tong": 650000},
            {"month": "04/2024", "tien_dien": 260000, "tien_nuoc": 160000, "tong": 870000},
        ]
        return data
