from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QSizePolicy, QLineEdit
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.Repository.LoginRepository import LoginRepository
from QLNHATRO.RentalManagementApplication.utils.Validators import Validators
from QLNHATRO.RentalManagementApplication.frontend.Component.ErrorDialog import ErrorDialog
from QLNHATRO.RentalManagementApplication.frontend.Component.SuccessDialog import SuccessDialog
from QLNHATRO.RentalManagementApplication.frontend.Component.LabelUI import LabelUI


class ResetPasswordView(QWidget):
    def __init__(self, username=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.setWindowTitle("Đặt lại mật khẩu")
        self.setMinimumSize(650, 400)
        self.username = username

        layout = QVBoxLayout(self)
        layout.setContentsMargins(84, 24, 84, 24)
        layout.setSpacing(20)

        # Tiêu đề
        title = QLabel("🔐 Đặt lại mật khẩu mới")
        title.setObjectName("Title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Trường nhập mật khẩu
        self.create_password_field(layout, "Mật khẩu mới:", "new_password")
        self.create_password_field(layout, "Xác nhận mật khẩu mới:", "confirm_password")

        # Nút xác nhận
        submit_btn = QPushButton("Xác nhận thay đổi mật khẩu")
        submit_btn.setFixedSize(350, 50)
        submit_btn.clicked.connect(self.on_submit)

        btn_wrapper = QHBoxLayout()
        btn_wrapper.addStretch()
        btn_wrapper.addWidget(submit_btn)
        btn_wrapper.addStretch()
        layout.addLayout(btn_wrapper)

    def on_submit(self):
        new_password = self.new_password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not new_password or not confirm_password:
            ErrorDialog.show_error("⚠️ Vui lòng nhập đầy đủ mật khẩu mới và xác nhận.", self)
            return

        if not Validators.is_valid_password(new_password):
            ErrorDialog.show_error("❌ Mật khẩu chưa đủ mạnh.\n• Tối thiểu 8 ký tự\n• Chữ hoa, số và ký tự đặc biệt.", self)
            return

        if new_password != confirm_password:
            ErrorDialog.show_error("❌ Mật khẩu xác nhận không khớp với mật khẩu mới.", self)
            return

        LoginRepository.change_password_into_database(self.username, new_password)
        SuccessDialog.show_success("✅ Mật khẩu đã được đặt lại thành công!", "", self)
        self.close()

    def create_password_field(self, parent_layout, label_text, object_name):
        field_frame = QFrame()
        field_frame.setFixedHeight(100)
        field_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QVBoxLayout(field_frame)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(5)

        label = QLabel(label_text)
        label.setFont(QFont("Be Vietnam", 16, QFont.Bold))
        layout.addWidget(label)

        password_field = QLineEdit()
        password_field.setObjectName(object_name)
        password_field.setFixedHeight(40)
        password_field.setFixedWidth(600)
        password_field.setEchoMode(QLineEdit.Password)

        layout.addWidget(password_field)
        setattr(self, object_name + "_input", password_field)
        parent_layout.addWidget(field_frame)
