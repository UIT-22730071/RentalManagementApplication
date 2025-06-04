from typing import Dict, Any

db = 'rent_house_database.sqlite'
class Room:
    def __init__(self, data: Dict[str, Any]):
        self.room_id = data.get('RoomID')
        self.room_name = data.get('RoomName')
        self.address = data.get('Address')
        self.room_type = data.get('RoomType')
        self.status = data.get('Status')  # "Còn trống" hoặc "Đã thuê"
        self.area = data.get('Area', 0.0)

        # Thông tin cấu trúc
        self.floor = data.get('Floor', 0)
        self.has_loft = data.get('HasLoft', 0)
        self.bathroom = data.get('Bathroom', 0)
        self.kitchen = data.get('Kitchen', 0)
        self.furniture = data.get('Furniture', 0)
        self.balcony = data.get('Balcony', 0)

        # Tiện ích
        self.free_wifi = data.get('FreeWifi', 0)
        self.parking = data.get('Parking', 0)
        self.air_conditioner = data.get('AirConditioner', 0)
        self.fridge = data.get('Fridge', 0)
        self.washing_machine = data.get('WashingMachine', 0)
        self.security = data.get('Security', 0)
        self.television = data.get('Television', 0)

        # Quy định
        self.pet_allowed = data.get('PetAllowed', 0)

        # Giá cả
        self.room_price = data.get('RoomPrice', 0.0)
        self.electricity_price = data.get('ElectricityPrice', 0.0)
        self.water_price = data.get('WaterPrice', 0.0)
        self.internet_price = data.get('InternetPrice', 0.0)
        self.other_fees = data.get('OtherFees', '')
        self.garbage_service_price = data.get('GarbageServicePrice', 0.0)
        self.deposit = data.get('Deposit', 0.0)

        # Chỉ số tiện ích
        self.current_electricity_num = data.get('CurrentElectricityNum', 0)
        self.current_water_num = data.get('CurrentWaterNum', 0)

        # Thông tin bổ sung
        self.max_tenants = data.get('MaxTenants', 1)
        self.rental_date = data.get('RentalDate')
        self.description = data.get('Description', '')

        # Quan hệ
        self.tenant_id = data.get('TenantID')
        self.landlord_id = data.get('LandlordID')