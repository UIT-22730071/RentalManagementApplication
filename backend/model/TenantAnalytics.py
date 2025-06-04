from typing import Dict, Any

db = 'rent_house_database.sqlite'
class TenantAnalytics:
    def __init__(self, data: Dict[str, Any]):
        self.id = data.get('id')
        self.tenant_id = data.get('TenantID')
        self.month = data.get('month')
        self.year = data.get('year')
        self.electricity_cost = data.get('electricity_cost', 0.0)
        self.water_cost = data.get('water_cost', 0.0)
        self.due_date = data.get('due_date')

    @property
    def total_cost(self) -> float:
        """Tổng chi phí (được tính tự động)"""
        return self.electricity_cost + self.water_cost