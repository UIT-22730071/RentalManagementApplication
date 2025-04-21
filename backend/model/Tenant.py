#TODO ?
class Tenant:
    def __init__(self, id_tenant, full_name, cccd,gender ,phone, email, marital_status):
        self.id_tenant = id_tenant
        self.full_name = full_name
        self.cccd = cccd
        self.gender = gender
        self.phone = phone
        self.email = email
        self.marital_status = marital_status

    def to_dict(self):
        """Trả về thông tin người thuê dưới dạng dictionary"""
        return {
            "id": self.id_tenant,
            "ho_ten": self.full_name,
            "cccd": self.cccd,
            "gender":self.gender,
            "sdt": self.phone,
            "email": self.email,
            "so_nguoi": self.marital_status
        }
    '''
    default_data = {
            'full_name': '',
            'birth_date': '',
            'citizen_id': '',
            'gender': '',
            'occupation': '',
            'phone_number': '',
            'marital_status': ''
        }
    '''