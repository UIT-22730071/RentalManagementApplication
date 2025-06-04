from typing import Dict, Any

db = 'rent_house_database.sqlite'

class InvoiceAnalytics:
    def __init__(self, data: Dict[str, Any]):
        self.invoice_id = data.get('InvoiceID')
        self.landlord_id = data.get('LandlordID')
        self.room_id = data.get('RoomID')
        self.tenant_id = data.get('TenantID')
        self.invoice_date = data.get('InvoiceDate')

        self.room_price = data.get('RoomPrice', 0.0)
        self.electricity_used = data.get('ElectricityUsed', 0)
        self.electricity_cost = data.get('ElectricityCost', 0.0)
        self.water_used = data.get('WaterUsed', 0)
        self.water_cost = data.get('WaterCost', 0.0)
        self.internet_fee = data.get('InternetFee', 0.0)
        self.garbage_fee = data.get('GarbageFee', 0.0)
        self.other_fee = data.get('OtherFee', 0.0)
        self.total_cost = data.get('TotalCost', 0.0)
        self.payment_status = data.get('PaymentStatus', 'Chưa thanh toán')