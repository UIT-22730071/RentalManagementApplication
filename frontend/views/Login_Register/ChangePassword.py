from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QFrame, QApplication, QLineEdit, QSizePolicy, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

from QLNHATRO.RentalManagementApplication.Repository.LoginRepository import LoginRepository
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.services.OTPService import OTPService
from QLNHATRO.RentalManagementApplication.utils.Validators import Validators


class ChangePasswordView(QWidget):
    def __init__(self, on_success_callback=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.setWindowTitle("Đổi mật khẩu")
        #self.setStyleSheet("background-color: white; border-radius: 40px;")
        self.setMinimumSize(850, 820)
        self.on_success_callback = on_success_callback

        layout = QVBoxLayout(self)
        layout.setContentsMargins(84, 24, 84, 24)
        layout.setSpacing(10)

        # Header
        header_frame = QFrame()
        header_layout = QVBoxLayout(header_frame)

        header_label = QLabel("🔒 Đổi mật khẩu")
        header_label.setObjectName("Title")  # Sẽ dùng style QLabel#Title từ GlobalStyle
        header_label.setFixedHeight(60)
        header_label.setAlignment(Qt.AlignCenter)

        header_layout.addWidget(header_label)

        subtext = QLabel("Vui lòng nhập thông tin để thay đổi mật khẩu của bạn")
        subtext.setAlignment(Qt.AlignCenter)
        subtext.setStyleSheet("color: #202E66; font-size: 14px;")

        header_layout.addWidget(subtext)
        layout.addWidget(header_frame)

        # Form fields
        self.create_username_field(layout, "Tên người dùng:", "username")
        self.create_password_field(layout, "Mật khẩu hiện tại:", "current_password", True)
        self.create_password_field(layout, "Mật khẩu mới:", "new_password", True)
        self.create_password_field(layout, "Xác nhận mật khẩu mới:", "confirm_password", True)

        # Password requirements
        self.add_password_requirements(layout)

        # Change Password button
        change_button = QPushButton("Đổi mật khẩu")
        change_button.setFixedWidth(256)
        change_button.setFixedHeight(60)
        change_button.clicked.connect(self.on_submit)
        button_wrapper = QHBoxLayout()
        button_wrapper.addStretch()
        button_wrapper.addWidget(change_button)
        button_wrapper.addStretch()
        layout.addLayout(button_wrapper)

        # Add spacer at bottom
        layout.addStretch()

    def create_username_field(self, parent_layout, label_text, object_name):
        field_frame = QFrame()
        field_frame.setFixedHeight(100)
        field_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QVBoxLayout(field_frame)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(5)

        label = QLabel(label_text)
        label.setFont(QFont("Be Vietnam", 14, QFont.Bold))
        layout.addWidget(label)

        text_field = QLineEdit()
        text_field.setObjectName(object_name)
        text_field.setFixedHeight(40)
        text_field.setFixedWidth(600)  # ⬅️ Thêm dòng này

        layout.addWidget(text_field)
        setattr(self, object_name + "_input", text_field)  # Gán để dễ truy cập
        parent_layout.addWidget(field_frame)

    def create_password_field(self, parent_layout, label_text, object_name, is_password=False):
        field_frame = QFrame()
        field_frame.setFixedHeight(100)
        field_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        layout = QVBoxLayout(field_frame)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(5)

        # Label
        label = QLabel(label_text)
        label.setFont(QFont("Be Vietnam", 14, QFont.Bold))
        #label.setStyleSheet("color: #202E66; border: none;")
        layout.addWidget(label)

        # Text field
        text_field = QLineEdit()
        text_field.setObjectName(object_name)
        #text_field.setFont(QFont("Be Vietnam", 12))
        text_field.setFixedHeight(40)
        setattr(self, object_name + "_input", text_field)

        if is_password:
            text_field.setEchoMode(QLineEdit.Password)

            # Add show/hide password toggle
            input_layout = QHBoxLayout()
            input_layout.setContentsMargins(0, 0, 0, 0)
            input_layout.setSpacing(0)

            input_layout.addWidget(text_field)

            toggle_btn = QPushButton("👁️")
            toggle_btn.setFixedWidth(40)
            toggle_btn.setStyleSheet("background-color: white")
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
            req_label.setFont(QFont("Be Vietnam", 8))
            req_label.setStyleSheet("color: #202E66; font-style: italic;")
            req_layout.addWidget(req_label)

        layout.addWidget(req_frame)

    def on_submit(self):
        username = self.username_input.text().strip()
        current_password = self.current_password_input.text()
        new_password = self.new_password_input.text()
        confirm_password = self.confirm_password_input.text()

        # Kiểm tra đầy đủ thông tin
        if not all([username, current_password, new_password, confirm_password]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return

        if not Validators.is_alpha_only(username.replace(" ", "")):
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập không hợp lệ (chỉ chứa chữ cái và không dấu).")
            return

        # Kiểm tra định dạng username
        if " " in username or len(username) < 4:
            QMessageBox.warning(self, "Lỗi",
                                "Tên đăng nhập không hợp lệ (không được có khoảng trắng và phải ≥ 4 ký tự).")
            return

        # Kiểm tra trùng khớp mật khẩu
        if new_password != confirm_password:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu mới và xác nhận không khớp.")
            return

        # Kiểm tra yêu cầu mật khẩu
        if not Validators.is_valid_password(new_password):
            QMessageBox.warning(self, "Lỗi", "Mật khẩu mới không đáp ứng yêu cầu bảo mật.")
            return

        if OTPService.check_change_password(username,current_password):  # Đây chỉ là giả lập, bạn nên thay bằng kiểm tra thật
            QMessageBox.critical(self, "Lỗi", "Mật khẩu hiện tại không đúng.")
            return

        LoginRepository.change_password_into_database(username,new_password)
        # Nếu mọi thứ đều hợp lệ
        #print("✅ Mật khẩu đã được thay đổi thành công.")
        QMessageBox.information(self, "Thành công", "Mật khẩu của bạn đã được thay đổi thành công!")

        if self.on_success_callback:
            self.on_success_callback()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChangePasswordView()
    window.show()
    sys.exit(app.exec_())