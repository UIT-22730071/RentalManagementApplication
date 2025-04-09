#TODO ?
class Room:
    def __init__(self,
                 room_id,
                 room_name,
                 address,
                 room_type,
                 status,
                 area,
                 floor,
                 has_loft,
                 bathroom,
                 kitchen,
                 balcony,
                 furniture,
                 appliances,
                 utilities,
                 rent_price,
                 deposit,
                 electricity_price,
                 water_price,
                 internet_price,
                 garbage_price,
                 other_fees,
                 max_tenants,
                 pets_allowed,
                 contact_name,
                 contact_phone,
                 available_date,
                 image_path,
                 current_electricity,
                 current_water,
                 tenant_id,
                 landlord_id,
                 ):
        self.room_id = room_id              # Mã phòng
        self.room_name = room_name          # Tên phòng
        self.address = address              # Địa chỉ phòng
        self.room_type = room_type          # Loại phòng (ví dụ: phòng trọ, căn hộ mini, studio,...)
        self.status = status                # Trạng thái phòng (Đang thuê, Còn trống)
        self.area = area                    # Diện tích phòng (đơn vị m²)
        self.floor = floor                  # Tầng lầu
        self.has_loft = has_loft            # Có gác lửng hay không (0 hoặc 1)
        self.bathroom = bathroom            # Kiểu phòng tắm (riêng, chung,...)
        self.kitchen = kitchen              # Mô tả nhà bếp (có bếp, bếp riêng,...)
        self.balcony = balcony              # Có ban công không
        self.furniture = furniture          # Nội thất cơ bản (giường, tủ,...)
        self.appliances = appliances        # Thiết bị điện (máy lạnh, máy giặt,...)
        self.utilities = utilities          # Tiện ích khác (Wifi, Camera,...)
        self.rent_price = rent_price        # Giá thuê phòng (VNĐ/tháng)
        self.deposit = deposit                      # Tiền cọc (VNĐ)
        self.electricity_price = electricity_price  # Giá điện (VNĐ/kWh)
        self.water_price = water_price              # Giá nước (VNĐ/người hoặc m³)
        self.internet_price = internet_price
        self.garbage_price = garbage_price# Phí internet (VNĐ/tháng)
        self.other_fees = other_fees                # Các loại phí khác (vệ sinh, rác,...)
        self.max_tenants = max_tenants              # Số người tối đa có thể thuê
        self.pets_allowed = pets_allowed            # Có cho phép nuôi thú cưng không ("Có"/"Không")
        self.contact_name = contact_name            # Tên người liên hệ (thường là chủ trọ)
        self.contact_phone = contact_phone          # Số điện thoại liên hệ
        self.available_date = available_date        # Ngày có thể bắt đầu thuê (dạng YYYY-MM-DD)
        self.image_path = image_path                # Đường dẫn ảnh minh họa căn phòng
        self.current_electricity = current_electricity          # Chỉ số điện hiện tại
        self.current_water = current_water                      # Chỉ số nước hiện tại
        self.tenant_id = tenant_id                              # Mã người thuê hiện tại (nullable)
        self.landlord_id = landlord_id                          # Mã chủ trọ quản lý phòng

    def to_dict(self):
        """Return full room data as dictionary"""
        return {
            "id": self.room_id,
            "room_name": self.room_name,
            "address": self.address,
            "room_type": self.room_type,
            "status": self.status,
            "area": self.area,
            "floor": self.floor,
            "has_loft": self.has_loft,
            "bathroom": self.bathroom,
            "kitchen": self.kitchen,
            "balcony": self.balcony,
            "furniture": self.furniture,
            "appliances": self.appliances,
            "utilities": self.utilities,
            "rent_price": self.rent_price,
            "deposit": self.deposit,
            "electricity_price": self.electricity_price,
            "water_price": self.water_price,
            "internet_price": self.internet_price,
            'garbage_price' : self.garbage_price,
            "other_fees": self.other_fees,
            "max_tenants": self.max_tenants,
            "pets_allowed": self.pets_allowed,
            "contact_name": self.contact_name,
            "contact_phone": self.contact_phone,
            "available_date": self.available_date,
            "image_path": self.image_path,
            "current_electricity": self.current_electricity,
            "current_water": self.current_water,
            "tenant_id": self.tenant_id,
            "landlord_id": self.landlord_id
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

