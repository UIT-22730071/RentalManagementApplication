from PyQt5.QtWidgets import QMessageBox

class ConfirmDialog:
    @staticmethod
    def ask(parent, message: str, title="Xác nhận") -> bool:
        box = QMessageBox(parent)
        box.setWindowTitle(title)
        box.setText(message)
        box.setIcon(QMessageBox.Question)
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        box.setDefaultButton(QMessageBox.No)

        # Áp dụng GlobalStyle
        from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
        box.setStyleSheet(f"""
            QMessageBox {{
                background-color: {GlobalStyle.MAIN_BG};
                color: {GlobalStyle.TEXT_COLOR};
                font-family: {GlobalStyle.FONT_FAMILY};
            }}
            QMessageBox QPushButton {{
                background-color: {GlobalStyle.PRIMARY_COLOR};
                color: white;
                font-size: 14px;
                font-family: {GlobalStyle.FONT_FAMILY};
                padding: 8px 20px;
                border-radius: 6px;
                min-width: 80px;
            }}
            QMessageBox QPushButton:hover {{
                background-color: #1D4DA5;
            }}
        """)

        return box.exec_() == QMessageBox.Yes
