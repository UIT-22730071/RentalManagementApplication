import sys

from PyQt5.QtWidgets import QMessageBox
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QStackedWidget
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from QLNHATRO.RentalManagementApplication.controller.LoginRegister.LoginController import LoginController
from QLNHATRO.RentalManagementApplication.frontend.Component.InputTextUI import InputTextUI


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.login_controller = LoginController()

        self.setWindowTitle("Login & Sign Up")
        self.setGeometry(200, 100, 300, 620)  #Ban đầu chỉ hiển thị khung trái
        self.setStyleSheet("background-color: #202020; border-radius: 15px;")

        # Widget chính
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout chính (chứa 2 phần trái + phải)
        self.main_layout = QHBoxLayout(self.central_widget)

        # Tạo Frame bên trái (Hiệu ứng nền + Nút)
        self.left_frame = QFrame()
        self.left_frame.setFixedWidth(300)
        self.left_frame.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF6B6B, stop:1 #FFA07A);
            border-radius: 15px;
        """)

        # Layout cho frame trái
        left_layout = QVBoxLayout(self.left_frame)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sign_in_btn = QPushButton("SIGN IN")
        self.sign_in_btn.setFixedSize(120, 40)
        self.sign_in_btn.setStyleSheet("background-color: white; color: #FF6B6B; font-weight: bold; border-radius: 20px;")
        self.sign_in_btn.clicked.connect(lambda: self.expand_window(1))

        self.login_btn = QPushButton("LOGIN")
        self.login_btn.setFixedSize(120, 40)
        self.login_btn.setStyleSheet("background-color: white; color: #FF6B6B; font-weight: bold; border-radius: 20px;")
        self.login_btn.clicked.connect(lambda: self.expand_window(0))

        left_layout.addWidget(self.sign_in_btn)
        left_layout.addWidget(self.login_btn)

        self.main_layout.addWidget(self.left_frame)

        # Tạo Frame bên phải chứa StackedWidget
        self.right_frame = QFrame()
        self.right_frame.setStyleSheet("background-color: #FDD7D2; border-radius: 15px;")
        self.right_frame.setFixedWidth(500)
        self.right_frame.setVisible(False)  # Ẩn ban đầu
        self.right_layout = QVBoxLayout(self.right_frame)

        # **Tạo StackedWidget để chứa LOGIN và SIGN IN**
        self.stacked_widget = QStackedWidget()
        self.right_layout.addWidget(self.stacked_widget)

        # **Trang 1: Form Đăng nhập**
        login_page = QWidget()
        login_layout = QVBoxLayout(login_page)

        login_label = QLabel("LOGIN")
        login_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        login_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        email_input = QLineEdit()
        InputTextUI.default_input().apply_style(email_input)
        email_input.setPlaceholderText("  Email")
        email_input.setFixedHeight(40)


        password_input = QLineEdit()
        InputTextUI.default_input().apply_style(password_input)
        password_input.setPlaceholderText("  Password")
        password_input.setFixedHeight(40)
        password_input.setEchoMode(QLineEdit.EchoMode.Password)


        # Nút Forgot Password
        forgot_password = QLabel('<a href="#">Forgot Password?</a>')
        forgot_password.setStyleSheet("color: #FF6B6B; font-size: 12px;")
        forgot_password.setOpenExternalLinks(True)
        forgot_password.setAlignment(Qt.AlignmentFlag.AlignRight)
        #forgot_password.actionEvent("chuyển đén trang quên mật khẩu")


        login_btn = QPushButton("LOGIN")
        login_btn.setFixedHeight(40)
        login_btn.setStyleSheet(""" background-color: #FF6B6B; color: white; font-weight: bold;  border-radius: 20px;""")
        login_btn.clicked.connect(lambda: self.handle_login(email_input, password_input))



        # Nút thoát
        # Nút thoát cho LOGIN
        exist_btn_login = QPushButton("exist")
        exist_btn_login.setFixedHeight(40)
        exist_btn_login.setStyleSheet("""
            background-color: #4FBEEE; color: white; font-weight: bold; 
            border-radius: 20px;
        """)


        login_layout.addWidget(login_label)
        login_layout.addWidget(email_input)
        login_layout.addWidget(password_input)
        login_layout.addWidget(forgot_password)

        login_layout.addWidget(login_btn)
        login_layout.addWidget(exist_btn_login)

        self.stacked_widget.addWidget(login_page)

        # **Trang 2: Form Đăng ký**
        signup_page = QWidget()
        signup_layout = QVBoxLayout(signup_page)
        signup_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #signup_layout.setContentsMargins(0, 0, 0, 0)


        signup_label = QLabel("SIGN UP")
        signup_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        signup_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        name_username = QLineEdit()
        InputTextUI.default_input().apply_style(name_username)
        name_username.setPlaceholderText("  Họ và tên ")
        name_username.setAlignment(Qt.AlignmentFlag.AlignLeft)
        name_username.setFixedHeight(40)


        username_input = QLineEdit()
        InputTextUI.default_input().apply_style(username_input)
        username_input.setPlaceholderText("  Tên tài khoản")
        username_input.setAlignment(Qt.AlignmentFlag.AlignLeft)
        username_input.setFixedHeight(40)

        phone_input = QLineEdit()
        InputTextUI.default_input().apply_style(phone_input)
        phone_input.setPlaceholderText("  Số điện thoại")
        phone_input.setAlignment(Qt.AlignmentFlag.AlignLeft)
        phone_input.setFixedHeight(40)

        cccd_input = QLineEdit()
        InputTextUI.default_input().apply_style(cccd_input)
        cccd_input.setPlaceholderText("  Căn cước công dân")
        cccd_input.setAlignment(Qt.AlignmentFlag.AlignLeft)
        cccd_input.setFixedHeight(40)

        password_input = QLineEdit()
        InputTextUI.default_input().apply_style(password_input)
        password_input.setPlaceholderText("  Mật khẩu")
        password_input.setAlignment(Qt.AlignmentFlag.AlignLeft)
        password_input.setFixedHeight(40)
        password_input.setEchoMode(QLineEdit.EchoMode.Password)

        confirm_password_input = QLineEdit()
        InputTextUI.default_input().apply_style(confirm_password_input)
        confirm_password_input.setPlaceholderText("  Xác nhận mật khẩu")
        confirm_password_input.setFixedHeight(40)
        confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        confirm_password_input.setAlignment(Qt.AlignmentFlag.AlignLeft)


        signup_btn = QPushButton("SIGN UP")
        signup_btn.setFixedHeight(40)
        signup_btn.setStyleSheet(""" background-color: #FF6B6B; color: white; font-weight: bold;  border-radius: 20px;""")

        # Nút thoát cho SIGN UP
        exist_btn_signup = QPushButton("exist")
        exist_btn_signup.setFixedHeight(40)
        exist_btn_signup.setStyleSheet("""
            background-color: #4FBEEE; color: white; font-weight: bold; 
            border-radius: 20px;
        """)


        signup_layout.addWidget(signup_label)
        signup_layout.addStretch()
        signup_layout.addWidget(name_username)
        signup_layout.addWidget(phone_input)
        signup_layout.addWidget(cccd_input)
        signup_layout.addWidget(username_input)
        signup_layout.addWidget(password_input)
        signup_layout.addWidget(confirm_password_input)
        signup_layout.addStretch()
        signup_layout.addWidget(signup_btn)
        signup_layout.addWidget(exist_btn_signup)

        self.stacked_widget.addWidget(signup_page)

        self.main_layout.addWidget(self.right_frame)

    def expand_window(self, index):
        """Khi nhấn vào LOGIN hoặc SIGN IN, cửa sổ mở rộng ra"""
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        # Lấy vị trí & kích thước hiện tại
        current_geometry = self.geometry()
        new_width = 800  # Kích thước sau khi mở rộng

        # Định nghĩa animation mở rộng cửa sổ
        self.animation.setStartValue(current_geometry)
        self.animation.setEndValue(current_geometry.adjusted(0, 0, new_width - current_geometry.width(), 0))

        # Hiển thị khung phải và chọn trang sau animation
        self.animation.finished.connect(lambda: self.right_frame.setVisible(True))
        self.animation.finished.connect(lambda: self.stacked_widget.setCurrentIndex(index))

        self.animation.start()

    def handle_login(self,email_input, password_input):
        # Xử lý khi bấm login
        email = email_input.text()
        password = password_input.text()

        if not email or not password:
            QMessageBox.warning(self,"Lỗi"," Vui lòng nhập lại email và mật khẩu")
            return
        if self.login_controller.go_to_check_login(self,email, password):
            QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
            self.login_controller.go_to_open_workspace()
        else:
            QMessageBox.critical(self, "Thất bại", "Email hoặc mật khẩu không đúng.")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
