from QLNHATRO.RentalManagementApplication.backend.Repository.TenantRepository import TenantRepository


class TenantService:
    @staticmethod
    def get_tenant_by_cccd(cccd):
        """Tìm người thuê theo CCCD"""
        tenant =  TenantRepository.get_tenant_by_cccd(cccd)
        for tenant in TenantRepository.get_all_tenants():
            if tenant['cccd'] == cccd:
                data_tenant_show = {
                    'name_tenant': tenant['name'],
                    'cccd': tenant['cccd'],
                    'phone': tenant['sdt'],
                    'email': tenant['email'],
                }
                return data_tenant_show
        return None

    @staticmethod
    def get_tenant_by_room_id(room_id):
        """Lấy thông tin người thuê theo id phòng"""
        return TenantRepository.get_tenant_by_room_id(room_id)
