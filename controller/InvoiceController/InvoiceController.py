from PyQt5.QtWidgets import QMessageBox

from QLNHATRO.RentalManagementApplication.Repository.InvoiceRepository import InvoiceRepository
from QLNHATRO.RentalManagementApplication.services.InvoiceService import InvoiceService


class InvoiceController:
    def __init__(self):
        self.invoice_window = None
        self.invoice_service = InvoiceService()
    #TODO: Lỗi chưa tìm ra nguyên nhân không mở được View InvoiceView

    def get_invoice_data_for_view(self, invoice_id):
        return self.invoice_service.get_invoice_data_for_view(invoice_id)

    def go_to_update_database(self, invoice_data_update_database):
        id_room = invoice_data_update_database['id_room']
        id_tenant = invoice_data_update_database['id_tenant']

        #success = InvoiceRepository.update_invoice_to_database(invoice_data_update_database)
        success = True
        if success:
            QMessageBox.information(None, "Thành công", "Hóa đơn đã được thêm vào hệ thống.")

            invoice_id = InvoiceRepository.get_new_id_invoice(id_room, id_tenant)

            # Create and store window reference in the existing instance
            #self.invoice_window = InvoiceSentToTenantView(invoice_id, id_room)
            #self.invoice_window.show()

            return invoice_id
        else:
            QMessageBox.warning(None, "Lỗi", "Không thể thêm hóa đơn.")
            return None


    ''' gọi hàm từ LanlordListInvoices'''
    @staticmethod
    def open_view_invoice(invoice_id):
        ''' Trong invoice id có đủ các id khác'''
        # Create and store window reference in the existing instance


        ''' gọi hàm service chuẩn bị đa ta cho 4 cái id trên'''
        total_data_invoice_view = InvoiceService.get_invoice_data_for_invoice_view(invoice_id)

        invoice_data = total_data_invoice_view['invoice_data']
        landlord_data = total_data_invoice_view['landlord_data']
        tenant_data = total_data_invoice_view['tenant_data']
        room_data = total_data_invoice_view['room_data']

        return invoice_data, landlord_data, tenant_data, room_data
