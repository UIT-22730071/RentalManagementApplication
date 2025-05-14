

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class ContactDialog(QDialog):
    def __init__(self, phone_number):
        super().__init__()
        self.setWindowTitle("📞 Thông tin liên hệ")
        self.setFixedSize(350, 150)
        self.setStyleSheet(GlobalStyle.global_stylesheet() + """
            QDialog {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFDEE9, stop:1 #B5FFFC);
                border-radius: 12px;
            }
            QLabel {
                font-size: 16px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 8px 16px;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        info_label = QLabel(f"📞 Số điện thoại liên hệ chủ trọ:\n \t{phone_number}\t ")
        info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(info_label)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)
