from QLNHATRO.RentalManagementApplication.Repository.MaintenanceRepository import MaintenanceRepository
from QLNHATRO.RentalManagementApplication.backend.model.MaintenanceRequest import MaintenanceRequest


class MaintenanceService:
    @staticmethod
    def create_request(room_id, tenant_id, description, image_path):
        request = MaintenanceRequest(room_id, tenant_id, description, image_path)
        MaintenanceRepository.save_request(request)
        return request
