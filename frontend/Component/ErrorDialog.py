from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class ErrorDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("❌ Lỗi nhập liệu")
        self.setFixedSize(400, 180)

        self.setStyleSheet(GlobalStyle.global_stylesheet() + """
            QDialog {
                background-color: #fff0f0;
                border: 2px solid #e74c3c;
                border-radius: 12px;
            }
            QLabel {
                color: #e74c3c;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #e74c3c;
                color: white;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)

        layout = QVBoxLayout(self)
        label = QLabel(message)
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignCenter)

        close_btn = QPushButton("Đóng")
        close_btn.clicked.connect(self.accept)

        layout.addStretch()
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(close_btn, alignment=Qt.AlignCenter)

    # ✅ Hàm tiện ích gọi dialog nhanh
    @staticmethod
    def show_error(message, parent=None):
        dialog = ErrorDialog(message, parent)
        dialog.exec_()
