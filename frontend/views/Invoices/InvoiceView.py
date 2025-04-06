import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, \
    QFrame, QVBoxLayout, QMainWindow, QTableWidget, QHeaderView, QApplication

from QLNHATRO.RentalManagementApplication.Repository.InvoiceRepository import InvoiceRepository
from QLNHATRO.RentalManagementApplication.Repository.RoomRepository import RoomRepository
from QLNHATRO.RentalManagementApplication.backend.model.Rooms import Room


class InvoiceSentToTenantView(QMainWindow):
    def __init__(self, invoice_id, room_id):
        super().__init__()
        print("Đang tạo InvoiceView cho room_id:", room_id)

        # Set up the main window
        self.setWindowTitle("HÓA ĐƠN TRƯỚC KHI GỬI NGƯỜI THUÊ")
        self.setGeometry(100, 100, 900, 700)

        # Create main widget and layout
        main_widget = QFrame()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Title label
        title_label = QLabel("HÓA ĐƠN")
        title_label.setFont(QFont("Be Vietnam Pro", 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Room information section
        info_group = QGroupBox("Thông tin phòng")
        info_layout = QGridLayout()
        info_group.setLayout(info_layout)

        # Get room details
        try:
            room = RoomRepository.get_room_by_id(room_id)
            if room is None:
                raise ValueError(f"Room with ID {room_id} not found")

            # Các đoạn xử lý tiếp theo với room...

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tải thông tin phòng: {str(e)}")
            print(f"Room load error: {e}")
            self.close()
            return

        # Add room details to the grid
        info_layout.addWidget(QLabel("Tên phòng:"), 0, 0)
        info_layout.addWidget(QLabel(room['ten_phong']), 0, 1)

        info_layout.addWidget(QLabel("Tên người thuê:"), 1, 0)
        info_layout.addWidget(QLabel(room['ten_nguoithue']), 1, 1)

        info_layout.addWidget(QLabel("Giá phòng:"), 2, 0)
        info_layout.addWidget(QLabel(str(room['gia_phong'])), 2, 1)

        main_layout.addWidget(info_group)

        # Invoice details table
        invoice_group = QGroupBox("Chi tiết hóa đơn")
        invoice_layout = QVBoxLayout()
        invoice_group.setLayout(invoice_layout)

        # Create table for invoice details
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "STT", "Tên hàng hóa, dịch vụ", "Đơn vị tính", "Số lượng", "Đơn giá", "Thành tiền"
        ])

        # Adjust table properties
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        invoice_layout.addWidget(self.table)

        try:
            # Lấy dữ liệu hóa đơn từ repository
            invoice_data = InvoiceRepository.get_invoice_data(invoice_id)
            if not invoice_data:
                raise ValueError("Không tìm thấy dữ liệu hóa đơn")

            # Lấy giá từ thông tin hóa đơn (thay vì dùng room_id)
            electricity_price = invoice_data['electricity_price']
            water_price = invoice_data['water_price']
            rent_price = invoice_data['rent_price']
            internet_price = invoice_data['internet_price']
            other_fees = invoice_data['other_fees']

            old_e = invoice_data['old_electricity']
            new_e = invoice_data['new_electricity']
            old_w = invoice_data['old_water']
            new_w = invoice_data['new_water']

            electricity_usage = new_e - old_e
            water_usage = new_w - old_w

            # Thiết lập số dòng cho bảng
            self.table.setRowCount(5)

            # Danh sách các dòng hóa đơn
            invoice_rows = [
                ("1", "Tiền điện", "kWh", electricity_usage, electricity_price, electricity_usage * electricity_price),
                ("2", "Tiền nước", "m³", water_usage, water_price, water_usage * water_price),
                ("3", "Tiền nhà", "tháng", 1, rent_price, rent_price),
                ("4", "Internet", "", 1, internet_price, internet_price),
                ("5", "Chi phí khác", "", 1, other_fees, other_fees),
            ]

            # Hiển thị bảng chi tiết hóa đơn
            for idx, row in enumerate(invoice_rows):
                formatted_row = [str(row[0]), row[1], row[2], str(row[3]), str(row[4]), str(row[5])]
                self.insert_row(idx, formatted_row)

            # Tính tổng tiền
            total_cost = sum([row[5] for row in invoice_rows])

            # Hiển thị tổng cộng
            total_group = QGroupBox("Tổng cộng")
            total_layout = QGridLayout()
            total_group.setLayout(total_layout)
            total_layout.addWidget(QLabel("Tổng tiền:"), 0, 0)
            total_layout.addWidget(QLabel(f"{total_cost:,} VND"), 0, 1)

            main_layout.addWidget(invoice_group)
            main_layout.addWidget(total_group)

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", "Không thể lấy dữ liệu hóa đơn!")
            print(f"❌ Error loading invoice: {e}")

        # Button panel
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignRight)

        send_button = QPushButton("Gửi hóa đơn")
        back_button = QPushButton("Quay lại")

        send_button.clicked.connect(self.send_invoice)
        back_button.clicked.connect(self.close)

        button_layout.addWidget(send_button)
        button_layout.addWidget(back_button)
        main_layout.addLayout(button_layout)

    def insert_row(self, row_index, values):
        for col_index, value in enumerate(values):
            item = QTableWidgetItem(value)
            self.table.setItem(row_index, col_index, item)

    def send_invoice(self):
        QMessageBox.information(self, "Thành công", "Hóa đơn đã được gửi!")


