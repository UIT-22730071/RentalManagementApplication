from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QMessageBox

from QLNHATRO.RentalManagementApplication.controller.InvoiceController.InvoiceController import InvoiceController
from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Invoices.InvoiceView import InvoiceView


class AdminInvoiceList(QWidget):
    def __init__(self, main_window, invoice_list):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window

        self.invoices = invoice_list if invoice_list else [{
            "invoice_id": 1,
                "room_name": "Phòng A101",
                "rent_price": 1500000,
                "electric_fee": 300000,
                "water_fee": 100000,
                "garbage_fee": 50000,
                "internet_fee": 70000,
                "other_fee": 30000,
                "created_at": "2025-04-01",
                "landlord_name": "Nguyễn Văn A",
                "tenant_name": "Trần Thị B"
        }]

        main_layout = QVBoxLayout()

        title = QLabel("📄 TẤT CẢ HÓA ĐƠN HỆ THỐNG")
        title.setObjectName("Title")
        title.setFixedHeight(60)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                border: 1px solid #dcdcdc;
                padding: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }
        """)

        # Cập nhật headers cho đúng
        headers = [
            "STT", "Họ tên chủ trọ", "Họ tên người thuê",
            "Tổng chi phí", "Ngày xuất hóa đơn", "Chi tiết hóa đơn"
        ]

        self.table = TableUI(headers)
        self.table.populate(self.invoices, has_button=True, button_callback=self.show_detail)

        main_layout.addWidget(self.table)
        main_layout.addWidget(frame)
        self.setLayout(main_layout)

    def show_detail(self, row):
        try:
            invoice = self.invoices[row]
            id_invoice = invoice.get("id_invoice", None)
            if id_invoice:
                print(f"🧾 ID hóa đơn được chọn: {id_invoice}")
                from QLNHATRO.RentalManagementApplication.frontend.views.Invoices.MainWindowInvoice import \
                    MainWindowInvoice

                invoice_data, landlord_data, tenant_data, room_data = InvoiceController.open_view_invoice(id_invoice)

                # Mở hóa đơn trong cửa sổ mới
                self.invoice_window = MainWindowInvoice(invoice_data, landlord_data, tenant_data, room_data)
                self.invoice_window.show()

            else:
                print("⚠️ Không tìm thấy ID hóa đơn.")
        except IndexError:
            print("❌ Không tìm thấy dòng hóa đơn.")