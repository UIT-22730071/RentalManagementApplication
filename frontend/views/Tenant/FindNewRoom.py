from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea, QPushButton, QHBoxLayout,
    QFrame, QGridLayout, QMessageBox
)
from PyQt5.QtCore import Qt


class FindNewRoom(QWidget):
    def __init__(self, main_window, advertised_rooms=None):
        super().__init__()
        self.main_window = main_window
        self.advertised_rooms = advertised_rooms or []

        self.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF6B6B, stop:1 #FFA07A);")

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        layout_main = QVBoxLayout(self)
        layout_main.addWidget(scroll)

        container = QWidget()
        container.setStyleSheet("background-color: #EAF9F6; border-radius: 20px; padding: 32px;")
        scroll.setWidget(container)

        layout = QVBoxLayout(container)
        layout.setSpacing(16)

        # Title
        title = QLabel("🏠 Danh sách phòng đang được quảng cáo")
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #2c3e50;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Room list
        self.room_list_container = QVBoxLayout()
        layout.addLayout(self.room_list_container)

        # Populate room list
        self.populate_rooms()

        # No rooms message
        if not self.advertised_rooms:
            no_rooms_label = QLabel("Hiện tại không có phòng nào được quảng cáo.")
            no_rooms_label.setStyleSheet("font-size: 16px; color: #7f8c8d; font-style: italic;")
            no_rooms_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(no_rooms_label)

    def populate_rooms(self):
        # Clear existing widgets
        while self.room_list_container.count():
            item = self.room_list_container.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # Add room cards
        for i, room in enumerate(self.advertised_rooms):
            room_card = self.create_room_card(i + 1, room)
            self.room_list_container.addWidget(room_card)

            # Add spacing between cards
            if i < len(self.advertised_rooms) - 1:
                self.room_list_container.addSpacing(15)

    def create_room_card(self, stt, room):
        # Room card container
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                border: 1px solid #ddd;
                padding: 15px;
            }
            QFrame:hover {
                border: 1px solid #6c63ff;
                background-color: #f9f9ff;
            }
        """)

        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(12)

        # Header with room name and price
        header_layout = QHBoxLayout()

        # Room number and name
        room_name = QLabel(f"{stt}. {room.get('room_name', 'Phòng không tên')}")
        room_name.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        header_layout.addWidget(room_name)

        header_layout.addStretch()

        # Price
        price_label = QLabel(f"💰 {room.get('price', 'Liên hệ')}")
        price_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #e74c3c;")
        header_layout.addWidget(price_label)

        card_layout.addLayout(header_layout)

        # Separator line
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("background-color: #ecf0f1; margin: 5px 0;")
        card_layout.addWidget(separator)

        # Room details grid
        details_grid = QGridLayout()
        details_grid.setHorizontalSpacing(20)
        details_grid.setVerticalSpacing(10)

        # Address
        address_label = QLabel("📍 Địa chỉ:")
        address_label.setStyleSheet("font-weight: bold; color: #333;")
        address_value = QLabel(room.get('address', 'Chưa cập nhật'))
        address_value.setWordWrap(True)
        details_grid.addWidget(address_label, 0, 0)
        details_grid.addWidget(address_value, 0, 1)

        # Description
        desc_label = QLabel("📝 Mô tả:")
        desc_label.setStyleSheet("font-weight: bold; color: #333;")
        desc_value = QLabel(room.get('description', 'Chưa có mô tả'))
        desc_value.setWordWrap(True)
        # Limit description length
        desc_text = desc_value.text()
        if len(desc_text) > 100:
            desc_value.setText(desc_text[:100] + "...")
        details_grid.addWidget(desc_label, 1, 0)
        details_grid.addWidget(desc_value, 1, 1)

        # Preferences
        pref_label = QLabel("💡 Ưu tiên:")
        pref_label.setStyleSheet("font-weight: bold; color: #333;")
        preferences = room.get('preferences', [])
        pref_text = ", ".join(preferences) if preferences else "Không có ưu tiên"
        pref_value = QLabel(pref_text)
        details_grid.addWidget(pref_label, 2, 0)
        details_grid.addWidget(pref_value, 2, 1)

        card_layout.addLayout(details_grid)

        # View details button
        view_btn = QPushButton("📋 Xem chi tiết")
        view_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c63ff;
                color: white;
                font-size: 16px;
                padding: 8px 16px;
                border-radius: 8px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #5a52d5;
            }
        """)
        view_btn.setProperty("room_id", room.get('id', None))
        view_btn.clicked.connect(lambda: self.view_room_details(room))

        card_layout.addWidget(view_btn, alignment=Qt.AlignRight)

        return card

    def view_room_details(self, room):
        room_id = room.get('id')
        if room_id:
            try:
                #TODO: Đang xử lý
                print("đang xử lý")
                #RoomDetailController.show_room_detail(room_id, self.main_window)
            except Exception as e:
                QMessageBox.critical(self, "Lỗi", f"Không thể hiển thị thông tin phòng: {str(e)}")
        else:
            QMessageBox.warning(self, "Thông báo", "Không tìm thấy thông tin phòng!")