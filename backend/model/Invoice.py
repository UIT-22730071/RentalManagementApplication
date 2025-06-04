from typing import Dict, Any

db = 'rent_house_database.sqlite'

class InvoiceModel:
    def __init__(self, data: Dict[str, Any]):
        self.invoice_id = data.get('InvoiceID')
        self.room_id = data.get('RoomID')
        self.tenant_id = data.get('TenantID')
        self.landlord_id = data.get('LandlordID')

        self.issue_date = data.get('issue_date')

        # Chỉ số điện nước
        self.curr_electric = data.get('CurrElectric', 0)
        self.curr_water = data.get('CurrWater', 0)
        self.pre_electric = data.get('PreElectric', 0)
        self.pre_water = data.get('PreWater', 0)

        # Chi phí
        self.total_electronic_cost = data.get('TotalElectronicCost', 0.0)
        self.total_water_cost = data.get('TotalWaterCost', 0.0)
        self.total_room_price = data.get('TotalRoomPrice', 0.0)
        self.internet_fee = data.get('InternetFee', 0.0)
        self.total_garbage_fee = data.get('TotalGarbageFee', 0.0)
        self.total_another_fee = data.get('TotalAnotherFee', 0.0)

        self.discount = data.get('Discount', 0.0)
        self.status = data.get('Status', 'Chưa thanh toán')  # 'Đã thanh toán', 'Chưa thanh toán'

    def calculate_total(self) -> float:
        """Tính tổng tiền hóa đơn"""
        total = (self.total_electronic_cost + self.total_water_cost +
                 self.total_room_price + self.internet_fee +
                 self.total_garbage_fee + self.total_another_fee - self.discount)
        return max(0.0, total)