from QLNHATRO.RentalManagementApplication.Repository.RoomRepository import RoomRepository


class InvoiceRepository:
    @staticmethod
    def save_invoice(invoice_data):
        """Lưu hóa đơn vào database"""
        # TODO: Thay thế bằng truy vấn SQL INSERT
        print(f"✅ Đã lưu hóa đơn: {invoice_data['invoice_id']}")

        # Cập nhật chỉ số điện nước mới cho phòng
        RoomRepository.update_room_metrics(
            invoice_data['room']['id'],
            invoice_data['chi_so_dien_moi'],
            invoice_data['chi_so_nuoc_moi']
        )

        return True



