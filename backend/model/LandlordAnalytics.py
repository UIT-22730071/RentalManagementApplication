from typing import Dict, Any

db = 'rent_house_database.sqlite'
class LandlordAnalytics:
    def __init__(self, data: Dict[str, Any]):
        self.id = data.get('id')
        self.landlord_id = data.get('LandlordID')
        self.month = data.get('month')
        self.year = data.get('year')
        self.total_income = data.get('total_income', 0.0)
        self.number_of_rented_rooms = data.get('number_of_rented_rooms', 0)
        self.average_price = data.get('average_price', 0.0)
        self.growth_rate = data.get('growth_rate', 0.0)