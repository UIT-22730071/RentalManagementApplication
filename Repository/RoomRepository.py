from QLNHATRO.RentalManagementApplication.backend.model.Rooms import Room


class RoomRepository:
    @staticmethod
    def get_all_rooms():
        """Lấy danh sách tất cả các phòng từ database"""
        # TODO: Thay thế bằng truy vấn SQL thực tế
        rooms = [
            {
                'id': 'P101',
                'ten_phong': 'Phòng 101',
                'dia_chi': '123 Đường ABC, Phường XYZ, Bình Thạnh, TP.HCM',
                'gia_phong': 3500000,
                'gia_dien': 3800,
                'gia_nuoc': 100000,
                'chi_so_dien': 450,
                'chi_so_nuoc': 28,
                'internet': 100000,
                'phi_khac': 20000,
                'dien_tich': 25.5
            },
            {
                'id': 'P102',
                'ten_phong': 'Phòng 102',
                'dia_chi': '123 Đường ABC, Phường XYZ, Bình Thạnh, TP.HCM',
                'gia_phong': 3800000,
                'gia_dien': 3800,
                'gia_nuoc': 100000,
                'chi_so_dien': 320,
                'chi_so_nuoc': 15,
                'internet': 100000,
                'phi_khac': 20000,
                'dien_tich': 28
            }
        ]
        return rooms

    @staticmethod
    def get_room_by_id(room_id):
        """Retrieve room data by ID (stub version)"""
        # TODO: Thay thế bằng truy vấn SQL thực tế
        room = Room(
            room_id="P101",
            room_name="Room 101",
            address="123 ABC Street",
            room_type="Boarding Room",
            status="Occupied",
            area=25,
            floor=1,
            has_loft="Yes",
            bathroom="Private",
            kitchen="With kitchen",
            balcony="Yes",
            furniture="Bed, Closet",
            appliances="Air Conditioner, Water Heater",
            utilities="Wi-Fi, Camera",
            rent_price=3500000,
            deposit=3500000,
            electricity_price=3800,
            water_price=100000,
            internet_price=100000,
            other_fees=20000,
            max_tenants=2,
            pets_allowed="No",
            contact_name="Ms. Ba",
            contact_phone="090x xxx xxx",
            available_date="2025-04-06",
            image_path="images/p101.png",
            current_electricity=245,
            current_water=32,
            tenant_id="TNT001",
            landlord_id="CT001"
        )
        return room.to_dict()

    @staticmethod
    def update_room_tenant(room_id, tenant_id):
        """Cập nhật người thuê cho phòng"""
        # TODO: Thực hiện truy vấn SQL UPDATE
        print(f"✅ Cập nhật người thuê {tenant_id} vào phòng {room_id}")

    @staticmethod
    def update_room_metrics(room_id, electricity_num, water_num):
        """Cập nhật chỉ số điện nước cho phòng"""
        # TODO: Thực hiện truy vấn SQL UPDATE
        print(f"✅ Cập nhật chỉ số điện {electricity_num}, nước {water_num} cho phòng {room_id}")
