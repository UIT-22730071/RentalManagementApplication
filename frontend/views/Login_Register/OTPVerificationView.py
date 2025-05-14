from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QFrame, QApplication, QLineEdit, QSizePolicy, QMessageBox)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont, QRegExpValidator
import sys

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.ForgotPassword import ForgotPasswordView

#TODO cần tách ra xử lý lại từng phần ==> cho ô nhập OTP

class OTPVerificationView(QWidget):
    def __init__(self, email="phuctran@gmail.com"):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.setWindowTitle("Nhập mã OTP")
        #self.setStyleSheet("background-color: white; border-radius: 40px;")
        self.setMinimumSize(800, 700)

        self.email = email

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(100, 100, 100, 100)

        # Center content wrapper
        content_wrapper = QFrame()
        content_layout = QVBoxLayout(content_wrapper)
        content_layout.setAlignment(Qt.AlignCenter)
        content_layout.setSpacing(45)

        # Header section
        header_frame = QFrame()
        header_layout = QVBoxLayout(header_frame)
        header_layout.setSpacing(40)

        # Title
        title_label = QLabel("Nhập mã OTP")
        title_label.setObjectName("Title")
        #title_label.setStyleSheet("color: #202E66;")
        title_label.setAlignment(Qt.AlignCenter)

        # Subtitle section
        subtitle_frame = QFrame()
        subtitle_layout = QVBoxLayout(subtitle_frame)
        subtitle_layout.setSpacing(8)

        # "Chúng tôi đã gửi mã OTP vào"
        subtitle_label = QLabel("Chúng tôi đã gửi mã OPT vào")
        #subtitle_label.setFont(QFont("Be Vietnam", 14, QFont.Bold))
        subtitle_label.setStyleSheet("color: #202E66;")

        # Email info section
        email_frame = QFrame()
        email_layout = QHBoxLayout(email_frame)
        email_layout.setContentsMargins(0, 0, 0, 0)
        email_layout.setSpacing(21)

        email_type = QLabel("Email")
        email_type.setFont(QFont("Be Vietnam", 12))
        #email_type.setStyleSheet("color: #202E66;")

        email_address = QLabel(self.email)
        email_address.setFont(QFont("Be Vietnam", 12))
        #email_address.setStyleSheet("color: #202E66; font-style: italic;")

        email_layout.addWidget(email_type)
        email_layout.addWidget(email_address)
        email_layout.addStretch()

        # Add subtitle components
        subtitle_layout.addWidget(subtitle_label)
        subtitle_layout.addWidget(email_frame)

        # OTP Input fields
        self.otp_frame = QFrame()
        otp_layout = QHBoxLayout(self.otp_frame)
        otp_layout.setSpacing(24)
        otp_layout.setAlignment(Qt.AlignCenter)

        self.otp_fields = []
        for i in range(4):
            otp_digit = QLineEdit()
            otp_digit.setFixedSize(72, 72)
            otp_digit.setStyleSheet("""
                QLineEdit {
                    background-color: white;
                    color: #202E66;
                    font-family: 'Be Vietnam Pro';
                    font-size: 36px;
                    font-weight: bold;
                    border: 1.2px solid #202E66;
                    border-radius: 18px;
                    text-align: center;
                    box-shadow: 5px 5px 10.5px rgba(18, 16, 16, 0.35);
                }
                QLineEdit:focus {
                    border: 2px solid #2158B6;
                }
            """)
            otp_digit.setAlignment(Qt.AlignCenter)
            otp_digit.setMaxLength(1)

            # Only allow numbers
            validator = QRegExpValidator(QRegExp("[0-9]"))
            otp_digit.setValidator(validator)

            # Auto-focus next field when digit entered
            if i < 3:  # For first 3 fields
                otp_digit.textChanged.connect(lambda text, current=i: self.focus_next_field(text, current))

            self.otp_fields.append(otp_digit)
            otp_layout.addWidget(otp_digit)

        # Confirm button
        self.confirm_button = QPushButton("Xác nhận mã OTP")
        self.confirm_button.setFixedSize(300, 50)
        '''
        self.confirm_button.setStyleSheet("""
            QPushButton {
                background-color: #2158B6;
                color: white;
                border-radius: 9px;
                font-family: 'Be Vietnam Pro';
                font-size: 18px;
                font-weight: bold;
                padding: 9px;
            }
            QPushButton:hover {
                background-color: #1A4A9E;
            }
            QPushButton:pressed {
                background-color: #13397A;
            }
        """)
        '''
        self.confirm_button.clicked.connect(self.confirm_otp)

        # Resend OTP section
        resend_frame = QFrame()
        resend_layout = QHBoxLayout(resend_frame)
        resend_layout.setAlignment(Qt.AlignCenter)
        resend_layout.setSpacing(18)

        not_received = QLabel("Không nhận được OTP?")
        not_received.setFont(QFont("Be Vietnam", 12))
        #not_received.setStyleSheet("color: #202E66; font-style: italic;")

        resend = QPushButton("Gửi lại OTP")
        resend.setFlat(True)
        resend.setCursor(Qt.PointingHandCursor)
        resend.setFont(QFont("Be Vietnam", 14, QFont.Bold))
        resend.setStyleSheet("color: #2158B6; border: none; text-align: left;")
        resend.clicked.connect(self.resend_otp)

        resend_layout.addWidget(not_received)
        resend_layout.addWidget(resend)

        # Assemble the header section
        header_layout.addWidget(title_label)
        header_layout.addLayout(subtitle_layout)

        # Add all components to content layout
        content_layout.addWidget(header_frame)
        content_layout.addWidget(self.otp_frame)
        content_layout.addWidget(self.confirm_button, 0, Qt.AlignCenter)
        content_layout.addWidget(resend_frame, 0, Qt.AlignCenter)

        # Add content to main layout
        main_layout.addWidget(content_wrapper, 1, Qt.AlignCenter)

        # Set initial focus to the first OTP field
        self.otp_fields[0].setFocus()

    def focus_next_field(self, text, current_index):
        if text and current_index < len(self.otp_fields) - 1:
            self.otp_fields[current_index + 1].setFocus()

    def confirm_otp(self):
        otp = ''.join([field.text() for field in self.otp_fields])
        if len(otp) == 4:
            print(f"✅ OTP Submitted: {otp}")
            # TODO: xác minh OTP ở backend
            self.go_to_reset_password()
        else:
            QMessageBox.warning(self, "Thiếu mã", "⚠️ Vui lòng nhập đủ 4 chữ số của mã OTP")

    def resend_otp(self):
        print(f"🔄 Resending OTP to {self.email}")
        # Here you would trigger the OTP resend logic
        # For demo purposes, we'll just clear the fields
        for field in self.otp_fields:
            field.clear()
        self.otp_fields[0].setFocus()

    def go_to_reset_password(self):
        self.hide()
        self.reset_password_view = ResetPasswordView()
        self.reset_password_view.show()


# Demo code to connect the two screens
class PasswordRecoveryFlow:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.forgot_password_view = None
        self.otp_verification_view = None

    def start_flow(self):
          # Import your existing class
        self.forgot_password_view = ForgotPasswordView(on_success_callback=self.show_otp_screen)
        self.forgot_password_view.show()

        # Override the on_submit method to open OTP screen
        original_on_submit = self.forgot_password_view.on_submit

        def new_on_submit():
            selected_id = self.forgot_password_view.radio_group.checkedId()
            original_on_submit()  # Gọi hàm in log
            if selected_id in [1, 2]:
                # Giả sử bạn có lấy được email người dùng từ một input nào đó hoặc mặc định
                email = "phuctran@gmail.com"  # TODO: lấy email thật từ input người dùng
                self.show_otp_screen(email)

        self.forgot_password_view.on_submit = new_on_submit
        self.forgot_password_view.show()

    def show_otp_screen(self, email):
        self.otp_verification_view = OTPVerificationView(email=email)
        self.otp_verification_view.show()

    def run(self):
        sys.exit(self.app.exec_())

class ResetPasswordView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đặt lại mật khẩu")
        label = QLabel("🔐 Giao diện đặt lại mật khẩu")
        layout = QVBoxLayout(self)
        layout.addWidget(label)


# Khởi chạy toàn bộ luồng quên mật khẩu
if __name__ == "__main__":
    flow = PasswordRecoveryFlow()
    flow.start_flow()
    flow.run()
