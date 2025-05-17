from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QGroupBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class InfoUpdater(QDialog):
    def __init__(self, title, current_value, on_update_callback):
        """
        :param title: Tiêu đề hiển thị trên dialog
        :param current_value: Giá trị hiện tại để hiển thị
        :param on_update_callback: Hàm callback gọi sau khi nhấn 'Lưu' (truyền giá trị mới)
        """
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.setWindowTitle(f"📝 Cập nhật {title}")
        self.setFixedSize(400, 180)
        self.on_update_callback = on_update_callback

        # Thiết lập giao diện chính
        layout = QVBoxLayout(self)
        '''
        self.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
                border-radius: 10px;
            }
            QLabel {
                font-size: 14px;
                color: #343a40;
            }
            QLineEdit {
                background-color: white;
                border: 2px solid #ced4da;
                border-radius: 8px;
                padding: 6px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #007bff;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border-radius: 6px;
                padding: 6px 14px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton#cancel {
                background-color: #6c757d;
            }
            QPushButton#cancel:hover {
                background-color: #5a6268;
            }
        """)
        '''
        # GroupBox chứa nội dung nhập liệu
        group_box = QGroupBox(f" ✏️ {title}")
        #group_box.setFont(QFont("Arial", 10, QFont.Bold))
        group_layout = QVBoxLayout()

        self.input = QLineEdit()
        self.input.setText(current_value)
        self.input.setAlignment(Qt.AlignLeft)
        group_layout.addWidget(self.input)
        group_box.setLayout(group_layout)

        # Nút hành động
        button_layout = QHBoxLayout()
        save_btn = QPushButton("✔ Lưu")

        cancel_btn = QPushButton("✖ Hủy")
        cancel_btn.setObjectName("CancelBtn")


        save_btn.clicked.connect(self.save)
        cancel_btn.clicked.connect(self.reject)

        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)

        # Thêm vào layout chính
        layout.addWidget(group_box)
        layout.addLayout(button_layout)

    def save(self):
        new_value = self.input.text()
        self.on_update_callback(new_value)
        self.accept()
