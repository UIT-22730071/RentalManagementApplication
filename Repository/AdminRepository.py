class AdminRepository:
    @staticmethod
    def get_all_users():
        #TODO: Tạo SQL truy xuất Database
        ''' Tài khoản admin tạo cố định không cho cập nhật hay update'''
        return [
            {"stt": 1, "username": "admin", "role": "admin", "status": "Active"},
            {"stt": 2, "username": "landlord01", "role": "Chủ trọ", "status": "Active"},
            {"stt": 3, "username": "tenant01", "role": "Người thuê trọ", "status": "Inactive"}
        ]

    @staticmethod
    def get_all_landlords():
        # TODO: Tạo SQL truy xuất Database
        return [
            {"name": "Nguyễn Văn A", "cccd": "123456789012", "phone": "0901234567", "email": "vana@example.com",
             "so_phong": 5,"username":"lanlord"},
            {"name": "Trần Thị B", "cccd": "987654321098", "phone": "0912345678", "email": "thib@example.com",
             "so_phong": 3,"username":"lanlord"}
        ]

    @staticmethod
    def get_all_tenants():
        # TODO: Tạo SQL truy xuất Database
        return [
            {"name": "Lê Thị C", "cccd": "012345678900", "phone": "0934567890", "email": "letc@example.com",
             "ngay_thue": "01/01/2024","username":"tenant"},
            {"name": "Phạm Văn D", "cccd": "112233445566", "phone": "0923456789", "email": "phamd@example.com",
             "ngay_thue": "15/03/2024","username":"tenant"}
        ]

    @staticmethod
    def get_all_rooms():
        # TODO: Tạo SQL truy xuất Database
        return [
            {
                "room_name": "Phòng A1",
                "room_type": "Phòng trọ",
                "landlord_name": "Nguyễn Văn A",
                "address": "123 Đường ABC, Quận 1",
                "status": "Trống",
                'room_id':"P101"
            },
            {
                "room_name": "Phòng B2",
                "room_type": "Chung cư",
                "landlord_name": "Trần Thị B",
                "address": "456 Đường XYZ, Quận 3",
                "status": "Đã thuê",
                'room_id': "P102"
            }
        ]

    @staticmethod
    def count_landlords_by_month(month, year):
        # TODO: Truy vấn SQL để đếm số chủ trọ đăng ký theo tháng
        return 2  # Giả lập

    @staticmethod
    def count_tenants_by_month(month, year):
        # TODO: Truy vấn SQL để đếm số người thuê mới theo tháng
        return 2  # Giả lập

    @staticmethod
    def count_rooms_by_month(month, year):
        # TODO: Truy vấn SQL để đếm số phòng tạo mới theo tháng
        return 2  # Giả lập
