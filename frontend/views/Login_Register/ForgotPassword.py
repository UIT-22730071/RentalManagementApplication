from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QFrame, QApplication, QButtonGroup, QRadioButton, QSizePolicy, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

from QLNHATRO.RentalManagementApplication.Repository.LoginRepository import LoginRepository
from QLNHATRO.RentalManagementApplication.frontend.Component.ErrorDialog import ErrorDialog
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.ChangePassword import ChangePasswordView
from QLNHATRO.RentalManagementApplication.utils.Validators import Validators


class ForgotPasswordView(QWidget):
    def __init__(self, on_success_callback=None):
        super().__init__()

        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.setWindowTitle("Quên mật khẩu")
        self.setMinimumSize(850, 500)
        self.on_success_callback = on_success_callback

        layout = QVBoxLayout(self)
        layout.setContentsMargins(84, 24, 84, 24)
        layout.setSpacing(10)

        # --- Header ---
        header_frame = QFrame()
        header_layout = QVBoxLayout(header_frame)
        header_layout.setSpacing(1)  # hoặc 2 nếu bạn muốn sát hơn
        header_layout.setContentsMargins(0, 0, 0, 0)

        title_label = QLabel("🔒 Bạn quên mật khẩu ?")
        title_label.setObjectName("Title")
        title_label.setMaximumHeight(45)
        title_label.setAlignment(Qt.AlignCenter)

        header_layout.addWidget(title_label)

        subtext = QLabel("🔍 Vui lòng chọn phương thức lấy lại mật khẩu")
        subtext.setAlignment(Qt.AlignCenter)
        subtext.setFont(QFont("Be Vietnam", 12))
        subtext.setMaximumHeight(28)
        header_layout.addWidget(subtext)

        layout.addWidget(header_frame)

        self.create_username_field(layout, "Tên người dùng:", "username")

        # Recovery Options with selection
        self.radio_group = QButtonGroup(self)
        self.sms_box = self.create_option_box("Khôi phục bằng SMS",
                                          "Mật khẩu sẽ được gửi đến số điện thoại bạn dùng để đăng ký tài khoản",
                                          option_id=1)
        self.email_box = self.create_option_box("Khôi phục bằng Email",
                                            "Mật khẩu sẽ được gửi đến địa chỉ Email bạn dùng để đăng ký tài khoản",
                                            option_id=2)

        layout.addWidget(self.sms_box)
        layout.addWidget(self.email_box)

        # OTP button
        otp_button = QPushButton("Nhận OTP")
        otp_button.setFixedSize(256, 45)

        otp_button.clicked.connect(self.on_submit) # xử lý button nhận OTP chuyển sang page nhập OTP

        otp_wrapper = QHBoxLayout()
        otp_wrapper.addStretch()
        otp_wrapper.addWidget(otp_button)
        otp_wrapper.addStretch()
        layout.addLayout(otp_wrapper)

        # Resend OTP
        resend_layout = QHBoxLayout()
        not_received = QLabel("Không nhận được OTP?")
        not_received.setFont(QFont("Be Vietnam", 12))
        #.setStyleSheet("color: #202E66; font-style: italic;")

        resend = QPushButton("Gửi lại OTP")
        resend.setFlat(True)
        resend.setCursor(Qt.PointingHandCursor)
        resend.setFont(QFont("Be Vietnam", 14, QFont.Bold))
        #resend.setStyleSheet("color: #2158B6; border: none; text-align: left;")
        resend.clicked.connect(self.resend_otp)

        resend.setFont(QFont("Be Vietnam", 14, QFont.Bold))
        #resend.setStyleSheet("color: #2158B6;")

        resend_layout.addStretch()
        resend_layout.addWidget(not_received)
        resend_layout.addSpacing(10)
        resend_layout.addWidget(resend)
        resend_layout.addStretch()

        layout.addLayout(resend_layout)

    def create_option_box(self, title, description, option_id):
        wrapper = QFrame()
        #wrapper.setStyleSheet("QFrame { background-color: white; border-radius: 16px; }")
        wrapper.setFixedHeight(100)
        wrapper.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        radio = QRadioButton()
        #radio.setStyleSheet("QRadioButton { margin-left: 10px; }")
        self.radio_group.addButton(radio, option_id)

        layout = QHBoxLayout(wrapper)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(20)

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(5)
        content_layout.setAlignment(Qt.AlignLeft)

        title_lbl = QLabel(title)
        title_lbl.setFont(QFont("Be Vietnam", 14, QFont.Bold))
        #title_lbl.setStyleSheet("color: #202E66;")
        title_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        desc_lbl = QLabel(description)
        desc_lbl.setFont(QFont("Be Vietnam", 12))
        #desc_lbl.setStyleSheet("color: #202E66; font-style: italic;")
        desc_lbl.setWordWrap(True)
        desc_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        content_layout.addWidget(title_lbl)
        content_layout.addWidget(desc_lbl)

        layout.addWidget(radio)
        layout.addLayout(content_layout)

        return wrapper

    from QLNHATRO.RentalManagementApplication.utils.Validators import Validators
    from QLNHATRO.RentalManagementApplication.frontend.Component.ErrorDialog import ErrorDialog

    def on_submit(self):
        username = self.username_input.text().strip()

        if not Validators.is_valid_input(username, allow_spaces=False, min_length=4):
            ErrorDialog.show_error("⚠️ Vui lòng nhập tên người dùng hợp lệ.", self)
            return

            # ✅ Kiểm tra username có tồn tại trong CSDL
        if not LoginRepository.is_username_exists(username):
            ErrorDialog.show_error("❌ Tên người dùng không tồn tại trong hệ thống.", self)
            return

        selected_id = self.radio_group.checkedId()

        if selected_id == 1:
            from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.OTPVerificationView import \
                OTPVerificationView
            sdt = LoginRepository.get_sdt_from_username(username)
            if not sdt:
                ErrorDialog.show_error("⚠️ Không tìm thấy số điện thoại cho tên người dùng này.", self)
                return
            otp_window = OTPVerificationView(email=sdt, username=username)
            otp_window.show()

        elif selected_id == 2:
            from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.OTPVerificationView import \
                OTPVerificationView
            email = LoginRepository.get_email_from_username(username)
            if not email:
                ErrorDialog.show_error("⚠️ Không tìm thấy email cho tên người dùng này.", self)
                return
            otp_window = OTPVerificationView(email=email, username=username)
            otp_window.show()

        else:
            ErrorDialog.show_error("⚠️ Vui lòng chọn 1 phương thức để nhận OTP.", self)

    def resend_otp(self):
        selected_id = self.radio_group.checkedId()
        if selected_id == 1:
            print("🔄 Gửi lại OTP đến SĐT")
        elif selected_id == 2:
            print("🔄 Gửi lại OTP đến Email")
        else:
            print("⚠️ Vui lòng chọn phương thức để gửi lại OTP")

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

