from datetime import datetime
from typing import Dict, Any
db = 'rent_house_database.sqlite'

class Advertisement:
    def __init__(self, data: Dict[str, Any]):
        self.ad_id = data.get('ad_id')
        self.room_id = data.get('RoomID')
        self.description = data.get('description', '')
        self.priority = data.get('priority', 'normal')
        self.image_path = data.get('image_path', 'default_image.png')
        self.created_at = data.get('created_at', datetime.now().isoformat())
