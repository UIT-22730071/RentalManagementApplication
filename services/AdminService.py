from QLNHATRO.RentalManagementApplication.Repository.AdminRepository import AdminRepository
from QLNHATRO.RentalManagementApplication.Repository.InvoiceRepository import InvoiceRepository


class AdminService:

    @staticmethod
    def get_all_users():
        """Trả về danh sách tài khoản người dùng (admin, chủ trọ, người thuê)"""
        return AdminRepository.get_all_users()

    @staticmethod
    def get_all_landlords():
        """Trả về danh sách chủ trọ với thông tin cơ bản và số phòng đang quản lý"""
        raw_data = AdminRepository.get_all_landlords()
        result = []
        for idx, landlord in enumerate(raw_data, 1):
            result.append({
                "stt": idx,
                "name": landlord.get("name", "N/A"),
                "cccd": landlord.get("cccd", "N/A"),
                "phone": landlord.get("phone", "N/A"),
                "email": landlord.get("email", "N/A"),
                "so_phong": landlord.get("so_phong", 0)
            })
        return result

    @staticmethod
    def get_all_tenants():
        """Trả về danh sách người thuê trọ"""
        raw_data = AdminRepository.get_all_tenants()
        result = []
        for idx, tenant in enumerate(raw_data, 1):
            result.append({
                "stt": idx,
                "name": tenant.get("name", "N/A"),
                "cccd": tenant.get("cccd", "N/A"),
                "phone": tenant.get("phone", "N/A"),
                "email": tenant.get("email", "N/A"),
                "ngay_thue": tenant.get("ngay_thue", "N/A")
            })
        return result

    @staticmethod
    def get_all_rooms():
        """Trả về danh sách phòng trọ"""
        raw_data = AdminRepository.get_all_rooms()
        result = []
        for idx, room in enumerate(raw_data, 1):
            result.append({
                "stt": idx,
                "room_name": room.get("room_name", "N/A"),
                "room_type": room.get("room_type", "N/A"),
                "landlord": room.get("landlord_name", "N/A"),
                "address": room.get("address", "N/A"),
                "status": room.get("status", "N/A")
            })
        return result

    @staticmethod
    def get_summary_dashboard_data():
        """Trả về dữ liệu thống kê hệ thống AdminHomePage"""
        return {
            "num_landlords": AdminRepository.count_landlords(),
            "num_tenants": AdminRepository.count_tenants(),
            "num_rooms": AdminRepository.count_rooms(),
            "num_paid_invoices": InvoiceRepository.count_paid_invoices()
        }

    @staticmethod
    def get_all_invoices_for_admin():
        """Trả về tất cả hóa đơn trong hệ thống"""
        raw_data = InvoiceRepository.get_all_invoices()
        result = []
        for idx, invoice in enumerate(raw_data, 1):
            total = (
                invoice.get("rent_price", 0)
                + invoice.get("electric_fee", 0)
                + invoice.get("water_fee", 0)
                + invoice.get("garbage_fee", 0)
                + invoice.get("internet_fee", 0)
                + invoice.get("other_fee", 0)
            )
            result.append({
                "STT": str(idx),
                "Tên Phòng": invoice.get("room_name", "N/A"),
                "Tiền nhà": f"{invoice.get('rent_price', 0):,} VNĐ",
                "Tiền điện": f"{invoice.get('electric_fee', 0):,} VNĐ",
                "Tiền nước": f"{invoice.get('water_fee', 0):,} VNĐ",
                "Tiền rác": f"{invoice.get('garbage_fee', 0):,} VNĐ",
                "Tổng chi phí": f"{total:,} VNĐ",
                "Ngày xuất hóa đơn": invoice.get("created_at", "N/A"),
                "Chi tiết hóa đơn": "Xem",
                "id_invoice": invoice.get("invoice_id")
            })
        return result
