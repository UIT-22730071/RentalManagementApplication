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

    @staticmethod
    def get_system_stats_by_month():
        # Trả về danh sách dict các tháng với số lượng user/room/invoice (có thể lấy từ DB thực tế)
        return [
            {"month": "01/2024", "landlord": 2, "tenant": 5, "room": 8, "invoice": 15},
            {"month": "02/2024", "landlord": 3, "tenant": 6, "room": 10, "invoice": 16},
            {"month": "03/2024", "landlord": 4, "tenant": 8, "room": 13, "invoice": 20},
            {"month": "04/2024", "landlord": 4, "tenant": 10, "room": 15, "invoice": 24},
            {"month": "05/2024", "landlord": 5, "tenant": 11, "room": 18, "invoice": 28},
            {"month": "06/2024", "landlord": 6, "tenant": 13, "room": 20, "invoice": 32},
            {"month": "07/2024", "landlord": 7, "tenant": 15, "room": 22, "invoice": 35},
            {"month": "08/2024", "landlord": 8, "tenant": 17, "room": 25, "invoice": 40},
            {"month": "09/2024", "landlord": 9, "tenant": 20, "room": 28, "invoice": 45},
            {"month": "10/2024", "landlord": 10, "tenant": 22, "room": 30, "invoice": 50}
        ]
