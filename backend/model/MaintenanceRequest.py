class MaintenanceRequest:
    def __init__(self, room_id, tenant_id, description, image_path, status="Chờ xử lý"):
        self.room_id = room_id
        self.tenant_id = tenant_id
        self.description = description
        self.image_path = image_path
        self.status = status
