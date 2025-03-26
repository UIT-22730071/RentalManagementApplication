# LandlordListInvoices.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame

from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI


class ListInvoices(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.invoices = [
            {"STT": "1", "ID Phòng": "01", "Tiền nhà": "2500000 VNĐ", "Tiền điện": "100000 VNĐ",
             "Tiền nước": "100000 VNĐ", "Tiền rác": "30000 VNĐ", "Tổng chi phí": "400000 VNĐ",
             "Ngày xuất hóa đơn": "01/01/2025","Chi tiết":""}
        ]

        main_layout = QVBoxLayout()
        self.setStyleSheet("background-color: #ecf0f1;")

        title = QLabel("🧾 Danh sách hóa đơn")
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
        #frame_layout = QVBoxLayout(frame)

        headers = [
            "STT", "ID Phòng", "Tiền nhà", "Tiền điện",
            "Tiền nước", "Tiền rác", "Tổng chi phí", "Ngày xuất hóa đơn", "Chi tiết hóa đơn"
        ]

        self.table = TableUI(headers)
        self.table.populate(self.invoices, has_button=True, button_callback=self.show_detail)

        #frame_layout.addWidget(self.table)
        main_layout.addWidget(self.table)
        main_layout.addWidget(frame)
        self.setLayout(main_layout)
    ## TODO: cần viết lại hàm show_detail khi có model
    def show_detail(self, row):
        print(f"🔍 Chi tiết hóa đơn dòng {row + 1}: {self.invoices[row]}")
