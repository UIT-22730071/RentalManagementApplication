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