from QLNHATRO.RentalManagementApplication.Repository.RoomRepository import RoomRepository


class RoomService:
    @staticmethod
    def get_all_rooms():
        """Lấy danh sách phòng có xử lý logic nếu cần"""

        return RoomRepository.get_all_rooms()

    @staticmethod
    def get_room_by_id(room_id):
        """Lấy thông tin phòng theo id"""
        return RoomRepository.get_room_by_id(room_id)

    @staticmethod
    def update_room_tenant(room_id, tenant_id):
        """Cập nhật người thuê cho phòng"""
        return RoomRepository.update_room_tenant(room_id, tenant_id)
