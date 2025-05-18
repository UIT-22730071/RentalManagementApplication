from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QFrame, QApplication, QLineEdit, QSizePolicy, QMessageBox)
from PyQt5.QtCore import Qt, QRegExp, QTimer
from PyQt5.QtGui import QFont, QRegExpValidator
import sys

from QLNHATRO.RentalManagementApplication.controller.OTPController.OTPController import OTPController
from QLNHATRO.RentalManagementApplication.frontend.Component.ErrorDialog import ErrorDialog
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.ForgotPassword import ForgotPasswordView



#TODO cần tách ra xử lý lại từng phần ==> cho ô nhập OTP

class OTPVerificationView(QWidget):
    def __init__(self, email=None,username=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.setWindowTitle("Nhập mã OTP")
        #self.setStyleSheet("background-color: white; border-radius: 40px;")
        self.setMinimumSize(400, 300)
        self.email = email
        self.username = username


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

        # Timer
        self.remaining_seconds = 120
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

        # Thêm label hiển thị thời gian còn lại
        self.timer_label = QLabel("⏳ Thời gian còn lại: 02:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("color: red; font-size: 14px; font-weight: bold;")
        content_layout.addWidget(self.timer_label)

        # Thiết lập thời gian đếm ngược
        self.remaining_seconds = 120
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # 1 giây

        # Confirm button
        self.confirm_button = QPushButton("Xác nhận mã OTP")
        self.confirm_button.setFixedSize(300, 50)
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
        #resend.setFont(QFont("Be Vietnam", 14, QFont.Bold))
        #resend.setStyleSheet("color: #2158B6; border: none; text-align: left;")
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
        OTPController.verify_otp(otp, self.username, self)

    def resend_otp(self):
        self.remaining_seconds = 120
        self.timer_label.setText("⏳ Thời gian còn lại: 02:00")
        self.timer.start(1000)
        self.reset_otp_fields()
        OTPController.resend_otp(self.username, self.email, self)



    def reset_otp_fields(self):
        for field in self.otp_fields:
            field.clear()
        self.otp_fields[0].setFocus()

    def update_timer(self):
        self.remaining_seconds -= 1
        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60
        self.timer_label.setText(f"⏳ Thời gian còn lại: {minutes:02}:{seconds:02}")

        if self.remaining_seconds <= 0:
            self.timer.stop()
            QMessageBox.warning(self, "Hết thời gian", "⏰ Hết thời gian nhập mã OTP. Vui lòng thử lại.")
            self.close()


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
        self.otp_verification_view = OTPVerificationView(email=email,username = self.username)
        self.otp_verification_view.show()

    def run(self):
        sys.exit(self.app.exec_())



