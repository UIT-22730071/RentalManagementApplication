from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository


class TenantService:
    @staticmethod
    def get_tenant_by_cccd(cccd):
        """Tìm người thuê theo CCCD"""
        return TenantRepository.get_tenant_by_cccd(cccd)

    @staticmethod
    def get_tenant_by_room_id(room_id):
        """Lấy thông tin người thuê theo id phòng"""
        return TenantRepository.get_tenant_by_room_id(room_id)
