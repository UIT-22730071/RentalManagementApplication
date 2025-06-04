from typing import Dict, Any

db = 'rent_house_database.sqlite'
class Landlord:
    def __init__(self, data: Dict[str, Any]):
        self.landlord_id = data.get('LandlordID')
        self.fullname = data.get('Fullname')
        self.birth = data.get('Birth')
        self.cccd = data.get('CCCD')
        self.gender = data.get('Gender')
        self.job_title = data.get('JobTitle')
        self.marital_status = data.get('MaritalStatus')  # 'Married', 'Single', 'Other'
        self.email = data.get('Email')
        self.phone_number = data.get('PhoneNumber')
        self.home_address = data.get('HomeAddress')
        self.user_id = data.get('UserID')
        self.username = data.get("Username")
        self.so_phong = data.get("so_phong", 0)

