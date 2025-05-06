class MaintenanceRepository:
    # Dữ liệu yêu cầu sửa chữa giả lập
    requests = []

    @staticmethod
    def save_request(request_data):
        MaintenanceRepository.requests.append(request_data)
        print(f"[DEBUG][Repository] Đã lưu yêu cầu: {request_data}")

    @staticmethod
    def get_all_requests():
        return MaintenanceRepository.requests

    @staticmethod
    def get_requests_by_room_id(room_id):
        return [req for req in MaintenanceRepository.requests if req['room_id'] == room_id]

    @staticmethod
    def get_requests_by_tenant_id(tenant_id):
        return [req for req in MaintenanceRepository.requests if req['tenant_id'] == tenant_id]
