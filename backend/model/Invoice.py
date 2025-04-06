#TODO ?
class Invoice:
    def __init__(self, invoice_id, room, tenant, old_electricity, new_electricity,
                 old_water, new_water, num_people, other_fees, created_date):
        self.invoice_id = invoice_id
        self.room = room
        self.tenant = tenant
        self.old_electricity = old_electricity
        self.new_electricity = new_electricity
        self.old_water = old_water
        self.new_water = new_water
        self.num_people = num_people
        self.other_fees = other_fees
        self.created_date = created_date

    def to_dict(self):
        """Trả về thông tin hóa đơn dưới dạng dictionary"""
        return {
            'invoice_id': self.invoice_id,
            'room': self.room,
            'tenant': self.tenant,
            'chi_so_dien_cu': self.old_electricity,
            'chi_so_dien_moi': self.new_electricity,
            'chi_so_nuoc_cu': self.old_water,
            'chi_so_nuoc_moi': self.new_water,
            'so_nguoi': self.num_people,
            'phi_khac': self.other_fees,
            'ngay_tao': self.created_date
        }