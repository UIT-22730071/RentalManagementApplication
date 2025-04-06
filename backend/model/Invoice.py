class Invoice:
    def __init__(self,
                 invoice_id,                  # Mã hóa đơn
                 room,                        # Thông tin phòng (đối tượng hoặc dict)
                 tenant,                      # Thông tin người thuê (đối tượng hoặc dict)
                 rent_price,                  # Giá thuê phòng (VNĐ/tháng)
                 electricity_price,           # Đơn giá điện (VNĐ/kWh)
                 water_price,                 # Đơn giá nước (VNĐ/người hoặc m³)
                 internet_price,              # Phí internet (VNĐ/tháng)
                 old_electricity,             # Chỉ số điện cũ
                 new_electricity,             # Chỉ số điện mới
                 old_water,                   # Chỉ số nước cũ
                 new_water,                   # Chỉ số nước mới
                 other_fees,                  # Chi phí khác (rác, vệ sinh,...)
                 created_date):               # Ngày tạo hóa đơn (YYYY-MM-DD)

        self.invoice_id = invoice_id
        self.room = room
        self.tenant = tenant

        self.rent_price = rent_price
        self.electricity_price = electricity_price
        self.water_price = water_price
        self.internet_price = internet_price

        self.old_electricity = old_electricity
        self.new_electricity = new_electricity
        self.old_water = old_water
        self.new_water = new_water

        self.other_fees = other_fees
        self.created_date = created_date

    def to_dict(self):
        """Trả về thông tin hóa đơn dưới dạng dictionary"""
        return {
            'invoice_id': self.invoice_id,
            'room': self.room,
            'tenant': self.tenant,
            'rent_price': self.rent_price,
            'electricity_price': self.electricity_price,
            'water_price': self.water_price,
            'internet_price': self.internet_price,
            'chi_so_dien_cu': self.old_electricity,
            'chi_so_dien_moi': self.new_electricity,
            'chi_so_nuoc_cu': self.old_water,
            'chi_so_nuoc_moi': self.new_water,
            'phi_khac': self.other_fees,
            'ngay_tao': self.created_date
        }
