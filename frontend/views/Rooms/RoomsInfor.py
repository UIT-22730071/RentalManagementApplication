# RoomInfor.py
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QScrollArea, QFrame, QGroupBox, QGridLayout, QDialog, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class RoomsInfor(QWidget):
    def __init__(self, main_window, room_id):
        super().__init__()
        self.main_window = main_window
        self.room_id = room_id
        self.room_data = {
            "Mã phòng": "P101",
            "Địa chỉ": "123 Đường ABC, Phường XYZ, Quận Bình Thạnh, TP. Hồ Chí Minh",
            "Loại phòng": "Phòng trọ trong dãy trọ",
            "Trạng thái": "Còn trống",
            "Diện tích": "25.5 m²",
            "Tầng": "1",
            "Gác lửng": "Có",
            "Phòng tắm": "Riêng trong phòng",
            "Nhà bếp": "Khu bếp riêng",
            "Ban công": "Có",
            "Nội thất cơ bản": "Giường, Tủ quần áo, Bàn học",
            "Thiết bị điện": "Điều hòa, Máy nước nóng",
            "Tiện ích": "Wifi, Camera, Chỗ để xe, Giờ giấc tự do",
            "Số điện":"365 KWH",
            "Số nước": "365 m3",
            "Giá thuê": "3.500.000 VNĐ/tháng",
            "Tiền đặt cọc": "3.500.000 VNĐ",
            "Giá điện": "3.800 VNĐ/kWh",
            "Giá nước": "100.000 VNĐ/người",
            "Internet": "100.000 VNĐ",
            "Phí rác": "50.000 VNĐ",
            "Phí khác": "Phí vệ sinh: 20.000 VNĐ",
            "Số người tối đa": "2",
            "Thú cưng": "Không",
            "Ngày có thể thuê": "2025-04-05",
            "Chủ trọ": "Cô Ba Chủ Trọ",
            "SĐT": "090x xxx xxx"
        }

        self.setStyleSheet("QWidget { background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFDEE9, stop:1 #B5FFFC); }")

        main_layout = QVBoxLayout(self)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # Card
        card = QFrame()
        card.setStyleSheet("QFrame { background: white; border-radius: 12px; }")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("📌 THÔNG TIN CHI TIẾT PHÒNG")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setStyleSheet("color: white; background-color: #2C3E50; border-radius: 10px; padding: 10px;")
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)

        # Section
        group = QGroupBox("📋 Thông tin phòng")
        group.setStyleSheet("""
            QGroupBox {
                font-weight: bold; border: 1px solid #3498db;
                border-radius: 10px; margin-top: 15px; padding-top: 15px;
                background-color: #f2f9fb;
            }
            QGroupBox::title {
                subcontrol-origin: margin; left: 10px;
                padding: 0 10px; font-size: 20px;
                background-color: white; border-radius: 5px; color: #2c3e50;
            }
        """)
        grid = QGridLayout(group)
        row = 0

        # Lưu label để cập nhật
        self.value_labels = {}

        for key, value in self.room_data.items():
            key_lbl = QLabel(key + ":")
            key_lbl.setStyleSheet("font-weight: bold;")
            val_lbl = QLabel(value)
            val_lbl.setWordWrap(True)
            self.value_labels[key] = val_lbl

            edit_btn = QPushButton("Thay đổi")
            edit_btn.setFixedWidth(80)  # Hoặc 70 tùy font
            edit_btn.setStyleSheet("""
                QPushButton {
                    background-color: #4FBEEE;
                    color: white;
                    border-radius: 10px;
                    padding: 4px 8px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #3ba8d8;
                }
                QPushButton:pressed {
                    background-color: #2b93c3;
                }
            """)
            edit_btn.clicked.connect(lambda _, k=key: self.open_edit_dialog(k))

            grid.addWidget(key_lbl, row, 0)
            grid.addWidget(val_lbl, row, 1)
            grid.addWidget(edit_btn, row, 2)
            row += 1

        card_layout.addWidget(group)
        scroll_layout.addWidget(card)
        scroll.setWidget(scroll_content)
        main_layout.addWidget(scroll)

    def open_edit_dialog(self, key):
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Cập nhật {key}")
        dialog.setModal(True)
        layout = QVBoxLayout(dialog)

        input_field = QLineEdit()
        input_field.setText(self.value_labels[key].text())
        layout.addWidget(input_field)

        btn = QPushButton("Lưu")
        btn.clicked.connect(lambda: self.save_change(dialog, key, input_field.text()))
        layout.addWidget(btn)

        dialog.exec()

    def save_change(self, dialog, key, text):
        self.value_labels[key].setText(text)
        dialog.accept()
