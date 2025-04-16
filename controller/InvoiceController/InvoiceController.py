from PyQt5.QtWidgets import QMessageBox

from QLNHATRO.RentalManagementApplication.backend.Repository import InvoiceRepository
from QLNHATRO.RentalManagementApplication.frontend.views.Invoices.InvoiceView import InvoiceSentToTenantView


class InvoiceController:
    def __init__(self):
        self.invoice_window = None
    #TODO: Lỗi chưa tìm ra nguyên nhân không mở được View InvoiceView

    def go_to_update_database(self, invoice_data_update_database):
        id_room = invoice_data_update_database['id_room']
        id_tenant = invoice_data_update_database['id_tenant']

        success = InvoiceRepository.update_invoice_to_database(invoice_data_update_database)

        if success:
            QMessageBox.information(None, "Thành công", "Hóa đơn đã được thêm vào hệ thống.")

            invoice_id = InvoiceRepository.get_new_id_invoice(id_room, id_tenant)

            # Create and store window reference in the existing instance
            self.invoice_window = InvoiceSentToTenantView(invoice_id, id_room)
            self.invoice_window.show()

            return invoice_id
        else:
            QMessageBox.warning(None, "Lỗi", "Không thể thêm hóa đơn.")
            return None




