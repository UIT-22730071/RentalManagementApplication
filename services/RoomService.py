from QLNHATRO.RentalManagementApplication.Repository.RoomRepository import RoomRepository


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
        room_data = RoomRepository.get_data_for_handle_room_infor(room_id)
        mapping = {
            "room_name": "Tên phòng",
            "address": "Địa chỉ",
            "room_type": "Loại phòng",
            "status": "Trạng thái",
            "area": "Diện tích",
            "floor": "Tầng",
            "has_loft": "Gác lửng",
            "bathroom": "Phòng tắm",
            "kitchen": "Nhà bếp",
            "balcony": "Ban công",
            "furniture": "Nội thất cơ bản",
            "appliances": "Thiết bị điện",
            "utilities": "Tiện ích",
            "current_electricity": "Số điện",
            "current_water": "Số nước",
            "rent_price": "Giá thuê",
            "deposit": "Tiền đặt cọc",
            "electricity_price": "Giá điện",
            "water_price": "Giá nước",
            "internet_price": "Internet",
            "garbage_price": "Phí rác",
            "other_fees": "Phí khác",
            "max_tenants": "Số người tối đa",
            "pets_allowed": "Thú cưng",
            "available_date": "Ngày có thể thuê",
            "lanlord_name": "Chủ trọ",
            "phone_lanlord": "SĐT"
        }

        translated = {}
        for en_key, vi_key in mapping.items():
            if en_key in room_data:
                value = room_data[en_key]
                # ✅ ép kiểu về string và xử lý đơn vị nếu cần
                if isinstance(value, float):
                    value = f"{value:.1f}"  # 1 chữ số thập phân
                elif isinstance(value, int):
                    value = f"{value:,}"  # format 3 chữ số một
                elif isinstance(value, (str,)):
                    value = str(value)
                elif isinstance(value, (bytes,)):
                    value = value.decode('utf-8')
                elif en_key == "available_date":
                    value = str(value)  # hoặc format thời gian

                # Thêm đơn vị nếu cần
                if en_key == "area":
                    value += " m²"
                if en_key == "current_water":
                    value += " m³"
                if en_key == "current_electricity":
                    value = str(value) if isinstance(value, str) else f"{value} KWH"
                if en_key == "rent_price" or en_key == "deposit":
                    value += " VNĐ/tháng"
                if en_key in ["electricity_price", "internet_price", "water_price", "garbage_price", "other_fees"]:
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
