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
        """Lấy thông tin phòng từ id"""
        # TODO: Thay thế bằng truy vấn SQL thực tế
        room = Room(
            id_room="P101",
            room_name="Phòng 101",
            room_address="123 Đường ABC",
            room_type="Trong dãy trọ",
            room_status="Đang thuê",
            room_area=25,
            room_floor=1,
            room_mezzanine="Có",
            room_bathroom="Khép kín",
            room_kitchen="Có bếp",
            room_balcony="Có",
            room_basic_furniture="Giường, Tủ",
            room_appliances="Máy lạnh, Nước nóng",
            room_amenities="Wifi, Camera",
            room_rent_price=3500000,
            room_deposit=3500000,
            room_electricity_price=3800,
            room_water_price=100000,
            room_internet_price=100000,
            room_other_fees=20000,
            room_max_occupancy=2,
            room_pets_allowed="Không",
            room_contact_name="Cô Ba",
            room_contact_phone="090x xxx xxx",
            room_available_date="2025-04-06",
            room_image_path="images/p101.png",
            current_electricity_num=245,
            current_water_num=32,
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
