# MainWindowInvoice.py
from PyQt5.QtWidgets import QMainWindow
from QLNHATRO.RentalManagementApplication.frontend.views.Invoices.InvoiceView import InvoiceView


class MainWindowInvoice(QMainWindow):
    def __init__(self, invoice_data, landlord_data, tenant_data, room_data):
        super().__init__()
        self.setWindowTitle("Chi tiết Hóa đơn")
        self.setGeometry(350, 120, 950, 1000)
        self.setStyleSheet("background-color: #ecf0f1; border-radius: 12px;")

        # Tạo widget InvoiceView
        self.invoice_view = InvoiceView(
            main_window=self,  # truyền self để xử lý nút "Thoát"
            invoice_data=invoice_data,
            landlord_data=landlord_data,
            tenant_data=tenant_data,
            room_data=room_data
        )

        self.setCentralWidget(self.invoice_view)
