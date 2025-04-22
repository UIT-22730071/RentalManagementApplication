# TenantListInvoices.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QMessageBox

from QLNHATRO.RentalManagementApplication.controller.InvoiceController.InvoiceController import InvoiceController
from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI
from QLNHATRO.RentalManagementApplication.frontend.views.Invoices.InvoiceView import InvoiceView


class TenantListInvoices(QWidget):
    def __init__(self, main_window, invoice_list, id_tenant):
        super().__init__()
        self.main_window = main_window
        self.id_tenant = id_tenant

        # Khởi tạo danh sách hóa đơn
        self.invoices = []

        if invoice_list is not None and len(invoice_list) > 0:
            # Transform invoice data to match table format
            for i, invoice in enumerate(invoice_list, 1):
                invoice_date = invoice['date']
                # Format date as month/year if possible
                try:
                    from datetime import datetime
                    date_obj = datetime.strptime(invoice_date, "%d-%m-%Y")
                    invoice_month = f"{date_obj.month:02d}/{date_obj.year}"
                except:
                    invoice_month = invoice_date

                self.invoices.append({
                    "STT": str(i),
                    "Hóa đơn tháng": invoice_month,
                    "Chỉ số điện": invoice['electricity'],
                    "Chỉ số nước": invoice['water'],
                    "Tổng Tiền": invoice['total_amount'],
                    "Ngày xuất hóa đơn": invoice_date,
                    "Tình trạng thanh toán": invoice['status'],
                    "Xem chi tiết": "Xem",
                    "id_invoice": invoice['invoice_id']  # Keep track of the invoice ID
                })
        else:
            # Default empty invoice for display
            self.invoices = [{
                "STT": "None",
                "Hóa đơn tháng": "None",
                "Chỉ số điện": "0 kWh",
                "Chỉ số nước": "0 m³",
                "Tổng Tiền": "0 VNĐ",
                "Ngày xuất hóa đơn": "None",
                "Tình trạng thanh toán": "None",
                "Xem chi tiết": "None",
                "id_invoice": None
            }]

        main_layout = QVBoxLayout()
        self.setStyleSheet("background-color: #ecf0f1;")

        title = QLabel("🧾 Danh sách hóa đơn của bạn")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;")
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
            "STT", "Hóa đơn tháng", "Chỉ số điện", "Chỉ số nước",
            "Tổng Tiền", "Ngày xuất hóa đơn", "Tình trạng thanh toán", "Xem chi tiết"
        ]
        self.table = TableUI(headers)
        # Make a mapping to ensure keys match headers
        header_to_key = {
            "STT": "STT",
            "Hóa đơn tháng": "Hóa đơn tháng",
            "Chỉ số điện": "Chỉ số điện",
            "Chỉ số nước": "Chỉ số nước",
            "Tổng Tiền": "Tổng Tiền",
            "Ngày xuất hóa đơn": "Ngày xuất hóa đơn",
            "Tình trạng thanh toán": "Tình trạng thanh toán",
            "Xem chi tiết": "Xem chi tiết"
        }

        self.table = TableUI(headers)
        # Pass header_to_key mapping to ensure columns match data
        self.table.populate(self.invoices, has_button=True, button_callback=self.show_detail,header_to_key=header_to_key)

        main_layout.addWidget(self.table)
        main_layout.addWidget(frame)

        self.setLayout(main_layout)

    def show_detail(self, row):
        try:
            invoice = self.invoices[row]
            id_invoice = invoice.get("id_invoice", None)
            if id_invoice:
                print(f"🧾 ID hóa đơn được chọn: {id_invoice}")

                # Gọi controller để chuẩn bị dữ liệu
                invoice_data, landlord_data, tenant_data, room_data = InvoiceController.open_view_invoice(
                    id_invoice)

                # Tạo giao diện hóa đơn và hiển thị
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
                print("⚠️ Không tìm thấy ID hóa đơn.")
        except IndexError:
            QMessageBox.warning(self, "Thông báo", "Không tìm thấy dòng hóa đơn.")
            print("❌ Không tìm thấy dòng hóa đơn.")

    def update_payment_status(self, id_invoice, new_status):
        """
        Cập nhật trạng thái thanh toán của hóa đơn

        Args:
            id_invoice: ID của hóa đơn cần cập nhật
            new_status: Trạng thái mới ("Đã thanh toán" hoặc "Chưa thanh toán")
        """
        for invoice in self.invoices:
            if invoice.get("id_invoice") == id_invoice:
                invoice["Tình trạng thanh toán"] = new_status
                # Refresh bảng
                header_to_key = {
                    "STT": "STT",
                    "Hóa đơn tháng": "Hóa đơn tháng",
                    "Chỉ số điện": "Chỉ số điện",
                    "Chỉ số nước": "Chỉ số nước",
                    "Tổng Tiền": "Tổng Tiền",
                    "Ngày xuất hóa đơn": "Ngày xuất hóa đơn",
                    "Tình trạng thanh toán": "Tình trạng thanh toán",
                    "Xem chi tiết": "Xem chi tiết"
                }
                self.table.populate(self.invoices, has_button=True, button_callback=self.show_detail,
                                    header_to_key=header_to_key)
                return True
        return False

    def pay_invoice(self, row):
        """
        Xử lý khi người dùng thanh toán hóa đơn
        Chức năng này sẽ được triển khai khi có chức năng thanh toán
        """
        try:
            invoice = self.invoices[row]
            id_invoice = invoice.get("id_invoice")
            if id_invoice:
                # Gọi controller để xử lý thanh toán
                success = InvoiceController.pay_invoice(id_invoice, self.id_tenant)
                if success:
                    self.update_payment_status(id_invoice, "Đã thanh toán")
                    QMessageBox.information(self, "Thông báo", "Thanh toán hóa đơn thành công!")
                else:
                    QMessageBox.warning(self, "Thông báo", "Thanh toán hóa đơn thất bại!")
            else:
                QMessageBox.warning(self, "Thông báo", "Không tìm thấy ID hóa đơn.")
        except IndexError:
            QMessageBox.warning(self, "Thông báo", "Không tìm thấy dòng hóa đơn.")