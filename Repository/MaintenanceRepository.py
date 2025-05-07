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

        maintenance_history = [
            {
                "id": 1,
                "description": "Vòi nước bị rỉ",
                "status": "Đã hoàn thành",
                "date": "01/04/2025"
            },
            {
                "id": 2,
                "description": "Đèn phòng tắm không sáng",
                "status": "Đang xử lý",
                "date": "20/04/2025"
            }
        ]

        return maintenance_history

    @staticmethod
    def get_requests_by_tenant_id(tenant_id):
        return [req for req in MaintenanceRepository.requests if req['tenant_id'] == tenant_id]
