from QLNHATRO.RentalManagementApplication.Repository.RoomRepository import RoomRepository
from QLNHATRO.RentalManagementApplication.backend.database.Database import Database


class RoomService:

    @staticmethod
    def get_all_rooms():
        """Lấy danh sách phòng có xử lý logic nếu cần"""

        return RoomRepository.get_all_rooms()

    @staticmethod
    def get_room_by_id(room_id):
        """Lấy thông tin phòng theo id"""
        return RoomRepository.get_room_by_id(room_id)

    @staticmethod
    def update_room_tenant(room_id, tenant_id):
        """Cập nhật người thuê cho phòng"""
        return RoomRepository.update_room_tenant(room_id, tenant_id)

    @staticmethod
    def handle_data_for_room_list_page(id_lanlord):
        raw_data = RoomRepository.get_infor_number_room_of_tenant(id_lanlord)
        number_data =[]

        for idx , item in enumerate(raw_data,start=1):
            item_with_stt = {"STT": idx, **item}
            number_data.append(item_with_stt)

        return RoomService.map_keys_for_table(number_data)


    @staticmethod
    def map_keys_for_table(data):
        """Chuyển đổi key từ dữ liệu gốc sang key UI cần"""
        mapped = []
        for item in data:
            mapped.append({
                'stt': item['STT'],
                'ten_phong': item['room_name'],
                'nguoi_thue': item['tenant_name'],
                'gia': f"{item['price_rent']:,} VND",
                'so_dien': f"{item['number_electric']} KWH",
                'so_nuoc': f"{item['number_water']} m³",
                'hoa_don': item['status_invoice'],
                'id_room': item['id_room']
            })
        return mapped
    @staticmethod
    def handle_data_for_create_new_room(id_lanlord,room_create_data):
        return RoomRepository.create_new_room(id_lanlord,room_create_data)

    @staticmethod
    def collect_data_create_room(id_landlord,room_name, number_people, address, type_room
    ,status,other_infor,area, price_rent,electric_price, water_price, num_electric, num_water):
        room_create_data = {
            'id_landlord': id_landlord,
            'room_name': room_name,
            'number_people': number_people,
            'address': address,
            'type_room': type_room,
            'status': status,
            'other_infor': other_infor,
            'area': area,
            'price_rent': price_rent,
            'electric_price': electric_price,
            'water_price': water_price,
            'num_electric': num_electric,
            'num_water': num_water
        }

        return room_create_data

    @staticmethod
    def handle_data_for_room_home(room_id):
        data_room_home = RoomRepository.get_data_for_handle_room_home(room_id)
        new_data = {}
        '''
            'current_electricity':356,
            'current_water':20,
            'electricity_price':3800,
            'water_price':100000,
            'old_electricity': 256,
            'old_water': 256,
            'old_electricity_price':3800,
            'old_water_price': 100000,
        '''
        percent_grow_num_electricity = RoomService.percent_two_num(data_room_home['current_electricity'], data_room_home['old_electricity'])
        percent_grow_num_water = RoomService.percent_two_num(data_room_home['current_water'],data_room_home['old_water'])
        percent_grow_electricity_price = RoomService.percent_two_num(data_room_home['electricity_price'],data_room_home['old_electricity'])
        percent_grow_water_price = RoomService.percent_two_num(data_room_home['water_price'],data_room_home['old_water_price'])

        new_data['current_electricity'] = str(data_room_home['current_electricity'])+" KWH"
        new_data['current_water'] = str(data_room_home['current_water']) + " m³"
        new_data['electricity_price'] = str(data_room_home['electricity_price']) + " VNĐ/KWH"
        new_data['water_price'] = str(data_room_home['water_price']) + " VNĐ/m³"

        new_data['percent_grow_num_electricity'] = str(percent_grow_num_electricity) + " %"
        new_data['percent_grow_num_water'] = str(percent_grow_num_water) + " %"
        new_data['percent_grow_electricity_price'] = str(percent_grow_electricity_price) + " %"
        new_data['percent_grow_water_price'] = str(percent_grow_water_price) + " %"

        return  new_data

    @staticmethod
    def percent_two_num(a,b):
        percent = (a - b)/a
        percent = percent*100
        return round(percent,2)

    @staticmethod
    def get_translated_room_info(room_id):
        """Chuyển đổi key tiếng Anh → tiếng Việt để dùng trong giao diện RoomsInfor"""
        row = RoomRepository.get_data_for_handle_room_infor(room_id)  # dữ liệu thô
        if not row:
            return {}

        def yes_no_meaning(value, content):
            return content if str(value) == "1" or value == 1 else "Không"

        # Xử lý các tiện ích riêng biệt
        row["HasLoft"] = yes_no_meaning(row.get("HasLoft"), "Có gác lửng")
        row["Bathroom"] = yes_no_meaning(row.get("Bathroom"), "Có phòng tắm riêng")
        row["Kitchen"] = yes_no_meaning(row.get("Kitchen"), "Có nhà bếp")
        row["Balcony"] = yes_no_meaning(row.get("Balcony"), "Có ban công")
        row["Furniture"] = yes_no_meaning(row.get("Furniture"), "Có nội thất")
        row["PetAllowed"] = yes_no_meaning(row.get("PetAllowed"), "Cho phép thú cưng")

        # Thiết bị điện
        appliances = {
            "Điều hòa": row.get("AirConditioner"),
            "Máy giặt": row.get("WashingMachine"),
            "Tủ lạnh": row.get("Fridge"),
            "Tivi": row.get("Television"),
            "Bảo vệ": row.get("Security"),
        }
        row["appliances"] = ", ".join([name for name, v in appliances.items() if str(v) == "1"])

        # Tiện ích
        utilities = {
            "Wifi miễn phí": row.get("FreeWifi"),
            "Chỗ để xe": row.get("Parking"),
        }
        row["utilities"] = ", ".join([name for name, v in utilities.items() if str(v) == "1"])

        # Mapping hiển thị
        mapping = {
            "RoomName": "Tên phòng",
            "Address": "Địa chỉ",
            "RoomType": "Loại phòng",
            "Status": "Trạng thái",
            "Area": "Diện tích",

            "Floor": "Tầng",
            "HasLoft": "Gác lửng",
            "Bathroom": "Phòng tắm",
            "Kitchen": "Nhà bếp",
            "Balcony": "Ban công",
            "Furniture": "Nội thất cơ bản",

            "CurrentElectricityNum": "Số điện",
            "CurrentWaterNum": "Số nước",
            "RoomPrice": "Giá thuê",
            "Deposit": "Tiền đặt cọc",
            "ElectricityPrice": "Giá điện",
            "WaterPrice": "Giá nước",
            "InternetPrice": "Internet",
            "GarbageServicePrice": "Phí rác",
            "OtherFees": "Phí khác",
            "PetAllowed": "Thú cưng",

            "MaxTenants": "Số người tối đa",
            "RentalDate": "Ngày có thể thuê",
            "Description": "Mô tả",

            "appliances": "Thiết bị điện",
            "utilities": "Tiện ích",

            "Fullname": "Chủ trọ",
            "PhoneNumber": "SĐT",
            "Email": "Địa chỉ mail"
        }

        translated = {}
        for en_key, vi_key in mapping.items():
            if en_key in row:
                value = row[en_key]

                if isinstance(value, float):
                    value = f"{value:.1f}"
                elif isinstance(value, int):
                    value = f"{value:,}"
                elif isinstance(value, str):
                    value = value.strip()

                # Thêm đơn vị hiển thị
                if en_key == "Area":
                    value += " m²"
                elif en_key == "CurrentWaterNum":
                    value += " m³"
                elif en_key == "CurrentElectricityNum":
                    value += " KWH"
                elif en_key in ["RoomPrice"]:
                    value += " VNĐ/tháng"
                elif en_key in ["Deposit"]:
                    value += " VNĐ"
                elif en_key in ["ElectricityPrice", "InternetPrice", "WaterPrice", "GarbageServicePrice", "OtherFees"]:
                    value += " VNĐ"

                translated[vi_key] = value

        return translated

    @staticmethod
    def get_data_send_to_update_tenant_rent_room(room_id, tenant_id):
        # goi reposolity ddeer upate
        # Đúng ra thì cái return phải trả về true_ false để còn truy ngược về hiển thị cập nhật ok
        # cập nhật cái id_tenant vào id_room là
        is_update = RoomRepository.update_room_tenant(room_id, tenant_id)
        if is_update == True:
            print("cap nhat thanh cong")
            return True
        else:
            print("cap nhat khong thanh cong")
            return False

    @staticmethod
    def get_list_room_by_id_landlord(id_landlord):
        """Lấy danh sách phòng theo id chủ trọ"""
        return RoomRepository.get_list_room_by_id_landlord(id_landlord)

    @staticmethod
    def get_room_monthly_stats(room_id):
        return RoomRepository.get_room_monthly_stats(room_id)
