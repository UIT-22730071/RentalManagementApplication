#TODO ?
class Room:
    def __init__(self,
                 id_room,
                 room_name,
                 room_address,
                 room_type,
                 room_status,
                 room_area,
                 room_floor,
                 room_mezzanine,
                 room_bathroom,
                 room_kitchen,
                 room_balcony,
                 room_basic_furniture,
                 room_appliances,
                 room_amenities,
                 room_rent_price,
                 room_deposit,
                 room_electricity_price,
                 room_water_price,
                 room_internet_price,
                 room_other_fees,
                 room_max_occupancy,
                 room_pets_allowed,
                 room_contact_name,
                 room_contact_phone,
                 room_available_date,
                 room_image_path,
                 current_electricity_num,
                 current_water_num,
                 tenant_id,
                 landlord_id,
                 ):
    # tạo phương thức getter_setter
        self.id_room = id_room
        self.room_name = room_name
        self.room_address = room_address
        self.room_type = room_type
        self.room_status = room_status
        self.room_area = room_area
        self.room_floor = room_floor
        self.room_mezzanine = room_mezzanine
        self.room_bathroom = room_bathroom
        self.room_kitchen = room_kitchen
        self.room_balcony = room_balcony
        self.room_basic_furniture = room_basic_furniture
        self.room_appliances = room_appliances
        self.room_amenities = room_amenities
        self.room_rent_price = room_rent_price
        self.room_deposit = room_deposit
        self.room_electricity_price = room_electricity_price
        self.room_water_price = room_water_price
        self.room_internet_price = room_internet_price
        self.room_other_fees = room_other_fees
        self.room_max_occupancy = room_max_occupancy
        self.room_pets_allowed = room_pets_allowed
        self.room_contact_name = room_contact_name
        self.room_contact_phone = room_contact_phone
        self.room_available_date = room_available_date
        self.room_image_path = room_image_path
        self.current_electricity_num = current_electricity_num
        self.current_water_num = current_water_num
        self.tenant_id = tenant_id
        self.landlord_id = landlord_id

    def to_dict(self):
        """Trả về toàn bộ thông tin phòng dưới dạng dictionary"""
        return {
            "id": self.id_room,
            "ten_phong": self.room_name,
            "dia_chi": self.room_address,
            "loai_phong": self.room_type,
            "trang_thai": self.room_status,
            "dien_tich": self.room_area,
            "tang": self.room_floor,
            "gac_lung": self.room_mezzanine,
            "phong_tam": self.room_bathroom,
            "nha_bep": self.room_kitchen,
            "ban_cong": self.room_balcony,
            "noi_that": self.room_basic_furniture,
            "thiet_bi_dien": self.room_appliances,
            "tien_ich": self.room_amenities,
            "gia_phong": self.room_rent_price,
            "tien_coc": self.room_deposit,
            "gia_dien": self.room_electricity_price,
            "gia_nuoc": self.room_water_price,
            "internet": self.room_internet_price,
            "phi_khac": self.room_other_fees,
            "so_nguoi_toi_da": self.room_max_occupancy,
            "thu_cung": self.room_pets_allowed,
            "chu_tro": self.room_contact_name,
            "sdt": self.room_contact_phone,
            "ngay_co_the_thue": self.room_available_date,
            "hinh_anh": self.room_image_path,
            "chi_so_dien": self.current_electricity_num,
            "chi_so_nuoc": self.current_water_num,
            "id_nguoithue": self.tenant_id,
            "id_chutro": self.landlord_id
        }
    '''
    @staticmethod
    def get_room_data_from_id_room(id_room):
        # TODO: Thay thế bằng logic từ DB
        room = Room(  # Giả lập dữ liệu test
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
    '''

