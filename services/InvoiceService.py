from QLNHATRO.RentalManagementApplication.Repository.InvoiceRepository import InvoiceRepository


class InvoiceService:
    @staticmethod
    def create_invoice(invoice_data):
        """Tạo hóa đơn mới"""
        # Xử lý logic tạo hóa đơn
        room = invoice_data['room']

        # Tạo ID hóa đơn
        invoice_id = f"INV-{room['id']}-{invoice_data['chi_so_dien_moi']}"

        # Chuẩn bị dữ liệu hóa đơn
        invoice = {
            'invoice_id': invoice_id,
            'room': room,
            'tenant': invoice_data['tenant'],
            'chi_so_dien_cu': room['chi_so_dien'],
            'chi_so_dien_moi': invoice_data['chi_so_dien_moi'],
            'chi_so_nuoc_cu': room['chi_so_nuoc'],
            'chi_so_nuoc_moi': invoice_data['chi_so_nuoc_moi'],
            'so_nguoi': invoice_data['so_nguoi'],
            'phi_khac': invoice_data['phi_khac'],
            'ngay_tao': 'Ngày tạo: 06/04/2025'
        }

        # Lưu hóa đơn vào database
        InvoiceRepository.save_invoice(invoice)

        return invoice