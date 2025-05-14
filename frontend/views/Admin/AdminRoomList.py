from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QMessageBox

from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI


class AdminRoomList(QWidget):
    def __init__(self, main_window, room_list=None):
        super().__init__()
        self.main_window = main_window
        self.room_list = room_list or [
            {
                "stt": 1,
                "room_name": "Phòng A1",
                "room_type": "Phòng trọ",
                "landlord": "Nguyễn Văn A",
                "address": "123 Đường ABC, Quận 1",
                "status": "Trống"
            },
            {
                "stt": 2,
                "room_name": "Phòng B2",
                "room_type": "Chung cư",
                "landlord": "Trần Thị B",
                "address": "456 Đường XYZ, Quận 3",
                "status": "Đã thuê"
            }
        ]

        self.setStyleSheet(GlobalStyle.global_stylesheet() + """
            QWidget {
                background-color: #F7F9FC;
            }
            QLabel {
                color: #202E66;
            }
        """)

        main_layout = QVBoxLayout()

        title = QLabel("🏠 Danh sách phòng trọ")
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

        headers = ["STT", "Tên phòng", "Loại phòng", "Chủ trọ", "Địa chỉ", "Trạng thái", "Xem chi tiết"]
        header_to_key = {
            "STT": "stt",
            "Tên phòng": "room_name",
            "Loại phòng": "room_type",
            "Chủ trọ": "landlord",
            "Địa chỉ": "address",
            "Trạng thái": "status"
        }

        self.table = TableUI(headers)
        self.table.populate(self.room_list, has_button=True, button_callback=self.show_detail, header_to_key=header_to_key)

        main_layout.addWidget(self.table)
        main_layout.addWidget(frame)
        self.setLayout(main_layout)

    def show_detail(self, row):
        try:
            room = self.room_list[row]
            QMessageBox.information(
                self,
                "Chi tiết phòng",
                f"🏠 {room['room_name']}\n📍 {room['address']}\n👤 Chủ trọ: {room['landlord']}\nTình trạng: {room['status']}"
            )
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể hiển thị chi tiết: {str(e)}")
