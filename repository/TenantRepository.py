


class TenantRepository:

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