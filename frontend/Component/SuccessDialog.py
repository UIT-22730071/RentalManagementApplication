from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class SuccessDialog(QDialog):
    def __init__(self, message,status, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cập nhật thành công")
        self.setFixedSize(400, 180)
        self.status = status


        # Áp dụng Global Style + Style riêng
        if self.status == 'Active':
            self.setStyleSheet(GlobalStyle.global_stylesheet() + """
                QDialog {
                    background-color: white;
                    border: 2px solid #27ae60;
                    border-radius: 12px;
                }
                QLabel {
                    color: #27ae60;
                    font-size: 16px;
                    font-weight: bold;
                }
                QPushButton {
                    background-color: #27ae60;
                    color: white;
                    padding: 8px 16px;
                    font-size: 14px;
                    font-weight: bold;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #1e8449;
                }
            """)
        else:
            self.setStyleSheet(GlobalStyle.global_stylesheet() + """
                            QDialog {
                                background-color: white;
                                border: 2px solid #E91B50;
                                border-radius: 12px;
                            }
                            QLabel {
                                color: #E91B50;
                                font-size: 16px;
                                font-weight: bold;
                            }
                            QPushButton {
                                background-color: #E91B50;
                                color: white;
                                padding: 8px 16px;
                                font-size: 14px;
                                font-weight: bold;
                                border-radius: 8px;
                            }
                            QPushButton:hover {
                                background-color: #F88686;
                            }
                        """)

        layout = QVBoxLayout(self)
        label = QLabel(message)
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignCenter)

        close_btn = QPushButton("OK")
        close_btn.clicked.connect(self.accept)

        layout.addStretch()
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(close_btn, alignment=Qt.AlignCenter)

    # Hàm tiện ích
    @staticmethod
    def show_success(message,status ,parent=None):
        dialog = SuccessDialog(message,status ,parent)
        dialog.exec_()
