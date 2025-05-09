from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QFrame, QApplication, QLineEdit, QSizePolicy, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys


class ChangePasswordView(QWidget):
    def __init__(self, on_success_callback=None):
        super().__init__()
        self.on_success_callback = on_success_callback
        self.setWindowTitle("Đổi mật khẩu")
        self.setStyleSheet("background-color: white; border-radius: 40px;")
        self.setMinimumSize(800, 700)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(84, 24, 84, 24)
        layout.setSpacing(30)

        # Header
        header_frame = QFrame()
        header_layout = QVBoxLayout(header_frame)
        header_label = QLabel("Đổi mật khẩu")
        header_label.setFont(QFont("Be Vietnam Pro", 24, QFont.Bold))
        header_label.setStyleSheet(
            "color: white; background-color: #2158B6; border-radius: 12px; padding: 10px; border: 1px solid #202E66;")
        header_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(header_label)

        subtext = QLabel("🔒 Vui lòng nhập thông tin để thay đổi mật khẩu của bạn")
        subtext.setFont(QFont("Be Vietnam", 12))
        subtext.setStyleSheet("color: #202E66; font-weight: 500;")
        subtext.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(subtext)

        layout.addWidget(header_frame)

        # Form fields
        self.create_password_field(layout, "Mật khẩu hiện tại:", "current_password", True)
        self.create_password_field(layout, "Mật khẩu mới:", "new_password", True)
        self.create_password_field(layout, "Xác nhận mật khẩu mới:", "confirm_password", True)

        # Password requirements
        self.add_password_requirements(layout)

        # Change Password button
        change_button = QPushButton("Đổi mật khẩu")
        change_button.setStyleSheet(
            "background-color: #2158B6; color: white; border-radius: 9px; font-size: 14px; padding: 12px 38px;"
        )
        change_button.setFixedWidth(256)
        change_button.setFixedHeight(45)
        change_button.clicked.connect(self.on_submit)
        button_wrapper = QHBoxLayout()
        button_wrapper.addStretch()
        button_wrapper.addWidget(change_button)
        button_wrapper.addStretch()
        layout.addLayout(button_wrapper)

        # Add spacer at bottom
        layout.addStretch()

    def create_password_field(self, parent_layout, label_text, object_name, is_password=False):
        field_frame = QFrame()
        field_frame.setStyleSheet("QFrame { background-color: white; border: 1px solid #F5D8D8; border-radius: 16px; }")
        field_frame.setFixedHeight(100)
        field_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QVBoxLayout(field_frame)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(10)

        # Label
        label = QLabel(label_text)
        label.setFont(QFont("Be Vietnam", 14, QFont.Bold))
        label.setStyleSheet("color: #202E66; border: none;")
        layout.addWidget(label)

        # Text field
        text_field = QLineEdit()
        text_field.setObjectName(object_name)
        text_field.setFont(QFont("Be Vietnam", 12))
        text_field.setStyleSheet(
            "QLineEdit { color: #202E66; background-color: #F8F8F8; border-radius: 8px; padding: 8px; border: 1px solid #E0E0E0; }"
        )
        text_field.setFixedHeight(50)

        if is_password:
            text_field.setEchoMode(QLineEdit.Password)

            # Add show/hide password toggle
            input_layout = QHBoxLayout()
            input_layout.setContentsMargins(0, 0, 0, 0)
            input_layout.setSpacing(0)

            input_layout.addWidget(text_field)

            toggle_btn = QPushButton("👁️")
            toggle_btn.setFixedWidth(40)
            toggle_btn.setStyleSheet("background-color: #F8F8F8; border-radius: 8px; border: 1px solid #E0E0E0;")
            toggle_btn.clicked.connect(lambda: self.toggle_password_visibility(text_field))
            input_layout.addWidget(toggle_btn)

            layout.addLayout(input_layout)
        else:
            layout.addWidget(text_field)

        parent_layout.addWidget(field_frame)
        return text_field

    def toggle_password_visibility(self, text_field):
        if text_field.echoMode() == QLineEdit.Password:
            text_field.setEchoMode(QLineEdit.Normal)
        else:
            text_field.setEchoMode(QLineEdit.Password)

    def add_password_requirements(self, layout):
        req_frame = QFrame()
        req_frame.setStyleSheet("border: none;")
        req_layout = QVBoxLayout(req_frame)

        req_title = QLabel("Mật khẩu phải đáp ứng các yêu cầu sau:")
        req_title.setFont(QFont("Be Vietnam", 12, QFont.Bold))
        req_title.setStyleSheet("color: #202E66;")
        req_layout.addWidget(req_title)

        requirements = [
            "• Tối thiểu 8 ký tự",
            "• Bao gồm ít nhất 1 chữ cái viết hoa",
            "• Bao gồm ít nhất 1 chữ số",
            "• Bao gồm ít nhất 1 ký tự đặc biệt (!, @, #, $, v.v.)"
        ]

        for req in requirements:
            req_label = QLabel(req)
            req_label.setFont(QFont("Be Vietnam", 11))
            req_label.setStyleSheet("color: #202E66; font-style: italic;")
            req_layout.addWidget(req_label)

        layout.addWidget(req_frame)

    def validate_password(self, password):
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        has_length = len(password) >= 8

        if not all([has_upper, has_digit, has_special, has_length]):
            return False
        return True

    def on_submit(self):
        current_password = self.findChild(QLineEdit, "current_password").text()
        new_password = self.findChild(QLineEdit, "new_password").text()
        confirm_password = self.findChild(QLineEdit, "confirm_password").text()

        # Check if all fields are filled
        if not all([current_password, new_password, confirm_password]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin")
            return

        # Check if new password matches the confirmation
        if new_password != confirm_password:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu mới và xác nhận mật khẩu không khớp")
            return

        # Check if new password meets requirements
        if not self.validate_password(new_password):
            QMessageBox.warning(self, "Lỗi", "Mật khẩu mới không đáp ứng các yêu cầu bảo mật")
            return

        # Here you would typically verify the current password with your backend
        # For demo purposes, let's assume it's correct

        print("✅ Mật khẩu đã được thay đổi thành công")
        QMessageBox.information(self, "Thành công", "Mật khẩu của bạn đã được thay đổi thành công!")

        if self.on_success_callback:
            self.on_success_callback()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChangePasswordView()
    window.show()
    sys.exit(app.exec_())