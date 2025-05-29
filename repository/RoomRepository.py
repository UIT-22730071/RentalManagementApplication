from QLNHATRO.RentalManagementApplication.backend.model.Rooms import Room


class RoomRepository:


    @staticmethod
    def get_room_data_for_invoice_view(room_id):
        # TODO: Thay thế bằng truy vấn SQL thực tế
        room_data = {
            'room_name': 'Chưa có dữ liệu',
            'room_price': 0,
            'electric_price': 0,
            'internet_fee': 0,
            'another_fee': 0,
            'water_price': 0,
            'garbage_fee': 0,
        }
        return room_data 

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
        """Retrieve room data by ID (stub version with updated mock data)"""
        room = Room(
            room_id="P302",
            room_name="Phòng 302 - Chung cư mini",
            address="456 Nguyễn Văn Linh, Quận 7, TP.HCM",
            room_type="Chung cư mini",
            status="Đã thuê",
            area=32.5,
            floor=3,
            has_loft="Có gác lửng",
            bathroom="Có phòng tắm riêng",
            kitchen="Có nhà bếp",
            balcony="Có ban công",
            furniture="Giường, Tủ, Bàn làm việc",
            appliances="Máy giặt, Điều hòa, Tivi",
            utilities="Wifi miễn phí, Chỗ để xe",
            rent_price=4200000,
            deposit=4200000,
            electricity_price=3500,
            water_price=60000,
            internet_price=100000,
            other_fees=20000,
            max_tenants=3,
            pets_allowed="Không",
            contact_name="Anh Tuấn",
            contact_phone="0909 123 456",
            available_date="2025-05-01",
            image_path="images/p302.png",
            current_electricity=425,
            current_water=70,
            tenant_id="TNT002",
            landlord_id="CT002"
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

    @staticmethod
    def get_infor_number_room_of_tenant(lanlord_id):
        # TODO: Thực hiện truy vấn SQL SELECT
        print(f"✅ Lấy thống tin phòng cơ bản của người thuê {lanlord_id}")
        room_list = [
            {
                'id_room': 'P101',
                'room_name': "Phòng 101",
                'tenant_name': "Nguyen Van A",
                'price_rent': 3500000,
                'number_electric': 25,
                'number_water': 28,
                'status_invoice': 'Chưa thanh toán'
            },
            {
                'id_room': 'P102',
                'room_name': "Phòng 102",
                'tenant_name': "Tran Thi B",
                'price_rent': 3200000,
                'number_electric': 20,
                'number_water': 22,
                'status_invoice': 'Đã thanh toán'
            }
            # Bạn có thể thêm các phòng khác ở đây
        ]
        return room_list
    @staticmethod
    def create_new_room(id_landlord, room_create_data):
        # TODO: Thực hiện truy vấn SQL INSERT

        print(f"✅ Tạo phòng mô tả {room_create_data} cho người thuê {id_landlord}")

    @staticmethod
    def get_data_for_handle_room_home(room_id):
        #TODO tạo hàm select lấy dũ liệu số điện số nước use room_id
        #room_id = room_id
        #old_electricity,old_water,old_electricity_price,old_water_price truy cập hóa đơn kỳ trước
        data_room_home = {
            'current_electricity':356,
            'current_water':20,
            'electricity_price':3800,
            'water_price':100000,
            'old_electricity': 256,
            'old_water': 256,
            'old_electricity_price':3800,
            'old_water_price': 100000,
        }
        return  data_room_home

    @staticmethod
    def get_data_for_handle_room_infor(room_id):
        #TODO tạo truy cấp SQL để select các thông tin cần thiết
        '''SELECT
        r.RoomName AS room_name,
        r.Address AS address,
        r.RoomType AS room_type,
        r.Status AS status,
        r.Area AS area,
        r.Floor AS floor,
        r.HasLoft AS has_loft,
        r.Bathroom AS bathroom,
        r.Kitchen AS kitchen,
        r.Balcony AS balcony,
        r.Furniture AS furniture,
        r.FreeWifi AS free_wifi,
        r.Parking AS parking,
        r.AirConditioner AS air_conditioner,
        r.Fridge AS fridge,
        r.WashingMachine AS washing_machine,
        r.Security AS security,
        r.Television AS television,
        r.CurrentElectricityNum AS current_electricity,
        r.CurrentWaterNum AS current_water,
        r.RoomPrice AS rent_price,
        r.Deposit AS deposit,
        r.ElectricityPrice AS electricity_price,
        r.WaterPrice AS water_price,
        r.InternetPrice AS internet_price,
        r.OtherFees AS other_fees,
        r.GarbageServicePrice AS garbage_price,
        r.MaxTenants AS max_tenants,
        r.PetAllowed AS pets_allowed,
        r.RentalDate AS available_date,
        l.Fullname AS lanlord_name,
        l.PhoneNumber AS phone_lanlord
        FROM Rooms r
        LEFT JOIN Landlords l ON r.LandlordID = l.LandlordID '''

        # bên dưới là giả lập dữ liệu cần
        data = {
            "RoomName": "P302",
            "Address": "456 Đường Nguyễn Văn Linh, Quận 7, TP.HCM",
            "RoomType": "Chung cư mini",
            "Status": "Đã thuê",
            "Area": 32.5,

            "Floor": 3,
            "HasLoft": 1,
            "Bathroom": 1,
            "Kitchen": 1,
            "Balcony": 1,
            "Furniture": 1,

            # Thiết bị điện & tiện ích (dạng cờ bit 0/1)
            "AirConditioner": 1,
            "Fridge": 0,
            "WashingMachine": 1,
            "Television": 1,
            "Security": 1,
            "FreeWifi": 1,
            "Parking": 0,

            "CurrentElectricityNum": 425,
            "CurrentWaterNum": 70,
            "RoomPrice": 4200000,
            "Deposit": 4200000,
            "ElectricityPrice": 3500,
            "WaterPrice": 60000,
            "InternetPrice": 100000,
            "GarbageServicePrice": 30000,
            "OtherFees": 20000,

            "MaxTenants": 3,
            "PetAllowed": 0,
            "RentalDate": "2025-05-01",
            "Description": "Phòng view đẹp, có ban công rộng, gần trung tâm mua sắm",
            # trích từ lanlord data
            "Fullname": "Anh Tuấn",
            "PhoneNumber": "0909 123 456",
            "Email": "tuan.chutro@gmail.com"
        }
        return data

    @staticmethod
    def update_tenant_rent_room(room_id, tenant_id):
        #TODO Tao hàm truy vấn update data
        print(f"✅ Cập nhật người thuê {tenant_id} vào phòng {room_id}")
        return True
    @staticmethod
    def get_list_room_by_id_landlord(id_lanlord):
        """Cập nhật thông tin phòng"""
        ds_phong = [
        {"RoomID": 1, "RoomName": "Phòng A1"},
        {"RoomID": 2, "RoomName": "Phòng B2"}
        ]

        ''' trả về 1 danh sách các tên phòng kèm RoomID để hiển thị trên giao diện tìm người'''
        return ds_phong