from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QFrame, QApplication, QButtonGroup, QRadioButton, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys


class ForgotPasswordView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quên mật khẩu")
        self.setStyleSheet("background-color: white; border-radius: 40px;")
        self.setMinimumSize(800, 700)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(84, 24, 84, 24)
        layout.setSpacing(30)

        # Header
        header_frame = QFrame()
        header_layout = QVBoxLayout(header_frame)
        header_label = QLabel("Bạn quên mật khẩu ?")
        header_label.setFont(QFont("Be Vietnam Pro", 24, QFont.Bold))
        header_label.setStyleSheet("color: white; background-color: #2158B6; border-radius: 12px; padding: 10px; border: 1px solid #202E66;")
        header_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(header_label)

        subtext = QLabel("🔍 Vui lòng chọn phương thức lấy lại mật khẩu")
        subtext.setFont(QFont("Be Vietnam", 12))
        subtext.setStyleSheet("color: #202E66; font-weight: 500;")
        subtext.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(subtext)

        layout.addWidget(header_frame)

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
        otp_button.setStyleSheet("background-color: #2158B6; color: white; border-radius: 9px; font-size: 14px; padding: 12px 38px;")
        otp_button.setFixedWidth(256)
        otp_button.setFixedHeight(45)
        otp_button.clicked.connect(self.on_submit)
        otp_wrapper = QHBoxLayout()
        otp_wrapper.addStretch()
        otp_wrapper.addWidget(otp_button)
        otp_wrapper.addStretch()
        layout.addLayout(otp_wrapper)

        # Resend OTP
        resend_layout = QHBoxLayout()
        not_received = QLabel("Không nhận được OTP?")
        not_received.setFont(QFont("Be Vietnam", 12))
        not_received.setStyleSheet("color: #202E66; font-style: italic;")

        resend = QLabel("Gửi lại OTP")
        resend.setFont(QFont("Be Vietnam", 14, QFont.Bold))
        resend.setStyleSheet("color: #2158B6;")

        resend_layout.addStretch()
        resend_layout.addWidget(not_received)
        resend_layout.addSpacing(10)
        resend_layout.addWidget(resend)
        resend_layout.addStretch()

        layout.addLayout(resend_layout)

    def create_option_box(self, title, description, option_id):
        wrapper = QFrame()
        wrapper.setStyleSheet("QFrame { background-color: white; border: 1px solid #F5D8D8; border-radius: 16px; }")
        wrapper.setFixedHeight(100)
        wrapper.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        radio = QRadioButton()
        radio.setStyleSheet("QRadioButton { margin-left: 10px; }")
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
        title_lbl.setStyleSheet("color: #202E66;")
        title_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        desc_lbl = QLabel(description)
        desc_lbl.setFont(QFont("Be Vietnam", 12))
        desc_lbl.setStyleSheet("color: #202E66; font-style: italic;")
        desc_lbl.setWordWrap(True)
        desc_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        content_layout.addWidget(title_lbl)
        content_layout.addWidget(desc_lbl)

        layout.addWidget(radio)
        layout.addLayout(content_layout)

        return wrapper

    def on_submit(self):
        selected_id = self.radio_group.checkedId()
        if selected_id == 1:
            print("✅ Gửi OTP đến SĐT")
        elif selected_id == 2:
            print("✅ Gửi OTP đến Email")
        else:
            print("⚠️ Vui lòng chọn 1 phương thức để nhận OTP")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ForgotPasswordView()
    window.show()
    sys.exit(app.exec_())
