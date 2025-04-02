from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class ManageInvoicePage(QWidget):
    def __init__(self, main_window, room_id):
        super().__init__()
        self.main_window = main_window
        self.room_id = room_id
        layout = QVBoxLayout(self)
        label = QLabel(f"Đây là trang Cập nhật & Xuất Hóa đơn cho Phòng {self.room_id}")
        label.setAlignment(Qt.AlignCenter)
        export_button = QPushButton("Xuất hóa đơn tháng này")
        export_button.clicked.connect(self.export_invoice)
        layout.addWidget(label)
        layout.addWidget(export_button)
        # TODO: Hiển thị danh sách hóa đơn, cho phép cập nhật, tính toán hóa đơn mới

    def export_invoice(self):
        print(f"Yêu cầu xuất hóa đơn cho phòng {self.room_id}")
        # TODO: Logic xuất hóa đơn (PDF, Excel,...)
        pass