from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QMessageBox

from QLNHATRO.RentalManagementApplication.controller.InvoiceController.InvoiceController import InvoiceController
from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Invoices.InvoiceView import InvoiceView


class AdminInvoiceList(QWidget):
    def __init__(self, main_window,invoice_list):
        super().__init__()

        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window

        if invoice_list:
            self.invoices = invoice_list
        else:
            self.invoices = [{
                "STT": "1",
                "Tên Phòng": "None",
                "Tiền nhà": "None VNĐ",
                "Tiền điện": "None VNĐ",
                "Tiền nước": "None VNĐ",
                "Tiền rác": "None VNĐ",
                "Tổng chi phí": "None VNĐ",
                "Ngày xuất hóa đơn": "01/01/2025",
                "Chi tiết hóa đơn": "Xem"
            }]

        main_layout = QVBoxLayout()



        title = QLabel("📄 TẤT CẢ HÓA ĐƠN HỆ THỐNG")
        #title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;")
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

        headers = [
            "STT", "Tên Phòng", "Tiền nhà", "Tiền điện",
            "Tiền nước", "Tiền rác", "Tổng chi phí", "Ngày xuất hóa đơn", "Chi tiết hóa đơn"
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
                print(f"[ADMIN] 🧾 Xem hóa đơn ID: {id_invoice}")
                invoice_data, landlord_data, tenant_data, room_data = InvoiceController.open_view_invoice(id_invoice)

                view = InvoiceView(
                    main_window=self.main_window,
                    invoice_data=invoice_data,
                    landlord_data=landlord_data,
                    tenant_data=tenant_data,
                    room_data=room_data
                )
                self.main_window.setCentralWidget(view)
            else:
                QMessageBox.warning(self, "Thông báo", "Không tìm thấy ID hóa đơn.")
        except Exception as e:
            import traceback
            traceback.print_exc()
            QMessageBox.critical(self, "Lỗi", f"Không thể hiển thị chi tiết hóa đơn: {e}")
