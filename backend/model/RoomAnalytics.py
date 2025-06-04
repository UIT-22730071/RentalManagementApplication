from typing import Dict, Any

db = 'rent_house_database.sqlite'
class RoomAnalytics:
    def __init__(self, data: Dict[str, Any]):
        self.id_room_analytics = data.get('idRoomAnalytics')
        self.room_id = data.get('RoomID')
        self.month = data.get('Month')
        self.year = data.get('Year')
        self.electricity_cost = data.get('ElectricityCost', 0.0)
        self.water_cost = data.get('WaterCost', 0.0)

    @property
    def total_cost(self) -> float:
        """Tổng chi phí (được tính tự động)"""
        return self.electricity_cost + self.water_cost