class TenantRepository:
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
        for tenant in TenantRepository.get_all_tenants():
            if tenant['id'] == tenant_id:
                return tenant
        return None

    @staticmethod
    def get_tenant_by_cccd(cccd):
        """Lấy thông tin người thuê từ số CCCD"""
        # TODO: Thay thế bằng truy vấn SQL thực tế
        for tenant in TenantRepository.get_all_tenants():
            if tenant['cccd'] == cccd:
                return tenant
        return None

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
