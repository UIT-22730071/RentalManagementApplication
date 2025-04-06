#TODO ?
class Tenant:
    def __init__(self, id_tenant, full_name, cccd, phone, email, num_people=1):
        self.id_tenant = id_tenant
        self.full_name = full_name
        self.cccd = cccd
        self.phone = phone
        self.email = email
        self.num_people = num_people

    def to_dict(self):
        """Trả về thông tin người thuê dưới dạng dictionary"""
        return {
            "id": self.id_tenant,
            "ho_ten": self.full_name,
            "cccd": self.cccd,
            "sdt": self.phone,
            "email": self.email,
            "so_nguoi": self.num_people
        }
