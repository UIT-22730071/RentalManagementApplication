from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os


class DashboardCard(QWidget):
    def __init__(self, title, value, change_percent, icon_path=None):
        super().__init__()

        # Layout chính
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(10, 10, 10, 10)  # Giảm padding tránh thừa ô vuông
        layout.setSpacing(8)  # Giữ khoảng cách hợp lý

        # Kiểu dáng thẻ
        self.setStyleSheet("""
            background-color: white;
            border-radius: 15px;
            padding: 15px;
            border: 1px solid #ddd;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);
        """)

        # Số liệu chính (Lớn)
        value_label = QLabel(value)
        value_label.setStyleSheet("font-size: 28px; font-weight: bold; color: #333;")
        value_label.setAlignment(Qt.AlignLeft)

        # Tiêu đề nhỏ
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 14px; color: #777;")
        title_label.setAlignment(Qt.AlignLeft)

        # Xử lý phần trăm thay đổi
        change_value = float(change_percent.replace('%', ''))  # Xóa ký tự `%`
        change_icon = "🔻" if change_value < 0 else "🔺"
        change_color = "#D9534F" if change_value < 0 else "#5CB85C"

        change_label = QLabel(f"{change_icon} {change_value}% since last month")
        change_label.setStyleSheet(f"font-size: 12px; color: {change_color};")
        change_label.setAlignment(Qt.AlignLeft)

        # Layout ngang chứa số liệu & icon
        top_layout = QHBoxLayout()
        top_layout.setSpacing(10)  # Giữ khoảng cách hợp lý
        top_layout.setAlignment(Qt.AlignLeft)

        # Icon bên phải (nếu có)
        icon_label = QLabel()
        if icon_path and os.path.exists(icon_path):
            try:
                pixmap = QPixmap(icon_path)
                icon_label.setPixmap(pixmap.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            except Exception as e:
                print(f"[WARNING] Lỗi khi load icon {icon_path}: {e}")
                icon_label.setText("💼")
        else:
            icon_label.setText("💼")

        icon_label.setStyleSheet(
            "font-size: 24px; color: #9370DB; background-color: rgba(200, 200, 255, 0.2); border-radius: 20px; padding: 10px;")

        top_layout.addWidget(value_label)
        top_layout.addStretch()
        top_layout.addWidget(icon_label)

        # Thêm vào layout chính
        layout.addLayout(top_layout)
        layout.addWidget(title_label)
        layout.addWidget(change_label)

        self.setLayout(layout)
