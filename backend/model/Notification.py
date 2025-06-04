from datetime import datetime
from typing import Dict, Any
db = 'rent_house_database.sqlite'

class Notification:
    def __init__(self, data: Dict[str, Any]):
        self.notification_id = data.get('NotificationID')
        self.user_id = data.get('UserID')
        self.content = data.get('Content')
        self.is_read = data.get('IsRead', 0)
        self.created_at = data.get('CreatedAt', datetime.now().isoformat())