from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI
from QLNHATRO.RentalManagementApplication.controller.RoomController.RoomMenuController import RoomMenuController


class FindRoomViewForTenant(QWidget):
    def __init__(self, main_window, data_advertised_rooms):
        super().__init__()
        self.main_window = main_window
        self.data = data_advertised_rooms

        self.setStyleSheet("background-color: #ecf0f1;")
        layout = QVBoxLayout()

        title = QLabel("🏠 DANH SÁCH PHÒNG ĐANG ĐƯỢC QUẢNG CÁO")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                border: 1px solid #ccc;
                padding: 10px;
            }
        """)

        headers = ["STT", "Tên chủ trọ", "Diện tích phòng", "Giá phòng", "Ưu tiên", "Xem chi tiết"]
        self.table = TableUI(headers)

        self.table.populate(self.data, has_button=True, button_callback=self.show_detail)
        layout.addWidget(self.table)
        layout.addWidget(frame)

        self.setLayout(layout)

    def show_detail(self, row):
        room_id = self.data[row].get("id_room")
        if room_id:
            RoomMenuController.go_to_room_management(room_id)
