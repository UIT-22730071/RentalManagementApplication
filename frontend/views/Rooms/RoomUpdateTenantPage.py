from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class RoomUpdateTenantPage(QWidget):
    def __init__(self, main_window, room_id):
        super().__init__()
        self.main_window = main_window
        self.room_id = room_id
        layout = QVBoxLayout(self)
        label = QLabel(f"Đây là trang Cập nhật Người thuê cho Phòng {self.room_id}")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        # TODO: Load thông tin người thuê hiện tại (nếu có) và hiển thị form cập nhật
