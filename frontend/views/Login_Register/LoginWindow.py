import sys

from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QFrame, QVBoxLayout, QPushButton, QLabel, QLineEdit, \
    QApplication

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.setWindowTitle("Login & Sign Up")
        self.setGeometry(200, 100, 300, 450)  # 📌 Ban đầu chỉ hiển thị frame trái
        #self.setStyleSheet("background-color: #202020; border-radius: 15px;")

        # Tạo widget chính
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout chính (chứa 2 phần trái + phải)
        self.main_layout = QHBoxLayout(self.central_widget)

        # 📌 1️⃣ Tạo Frame bên trái (Hiệu ứng nền + Nút)
        self.left_frame = QFrame()
        self.left_frame.setFixedWidth(300)
        self.left_frame.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF6B6B, stop:1 #FFA07A);
            border-radius: 15px;
        """)

        # Layout cho frame trái
        left_layout = QVBoxLayout(self.left_frame)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sign_in_btn = QPushButton("REGISTER")
        self.sign_in_btn.setFixedSize(250, 40)
        self.sign_in_btn.setStyleSheet("background-color: white; color: #FF6B6B; font-weight: bold; border-radius: 20px;")
        self.sign_in_btn.clicked.connect(self.expand_window)



        left_layout.addWidget(self.sign_in_btn)


        self.main_layout.addWidget(self.left_frame)

        # 📌 2️⃣ Tạo Frame bên phải (Form đăng nhập)
        self.right_frame = QFrame()
        #self.right_frame.setStyleSheet("background-color: white; border-radius: 15px;")
        self.right_frame.setVisible(False)  # 📌 Ẩn ban đầu
        right_layout = QVBoxLayout(self.right_frame)

        # Logo
        logo_label = QLabel("LOGIN")
        logo_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Ô nhập Email
        email_input = QLineEdit()
        email_input.setPlaceholderText("  Email")
        email_input.setFixedHeight(40)
        #email_input.setStyleSheet("border: 1px solid gray; border-radius: 20px; padding-left: 10px;")

        # Ô nhập Password
        password_input = QLineEdit()
        password_input.setPlaceholderText("  Password")
        password_input.setFixedHeight(40)
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        #password_input.setStyleSheet("border: 1px solid gray; border-radius: 20px; padding-left: 10px;")

        # Nút Forgot Password
        forgot_password = QLabel('<a href="#">Forgot Password?</a>')
        forgot_password.setStyleSheet("color: #FF6B6B; font-size: 12px;")
        forgot_password.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Nút Login
        login_btn = QPushButton("LOGIN")

        login_btn.setFixedHeight(40)
        login_btn.setStyleSheet("""
            background-color: #FF6B6B; color: white; font-weight: bold; 
            border-radius: 20px;""")

        #Nút thoát
        exist_btn = QPushButton("Exist")
        exist_btn.setFixedHeight(40)
        exist_btn.setStyleSheet("""
                    background-color: #4FBEEE; color: white; font-weight: bold; 
                    border-radius: 20px;""")

        # Thêm vào layout
        right_layout.addWidget(logo_label)
        right_layout.addWidget(email_input)
        right_layout.addWidget(password_input)
        right_layout.addWidget(forgot_password)
        right_layout.addWidget(login_btn)
        right_layout.addWidget(exist_btn)

        self.main_layout.addWidget(self.right_frame)

    def expand_window(self):
        """Khi nhấn vào LOGIN hoặc SIGN IN, cửa sổ mở rộng ra"""
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)  # Thời gian animation (ms)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        # Lấy vị trí & kích thước hiện tại
        current_geometry = self.geometry()
        new_width = 800  # Kích thước sau khi mở rộng

        # Định nghĩa animation mở rộng cửa sổ
        self.animation.setStartValue(current_geometry)
        self.animation.setEndValue(current_geometry.adjusted(0, 0, new_width - current_geometry.width(), 0))

        # Hiển thị khung phải sau animation
        self.animation.finished.connect(lambda: self.right_frame.setVisible(True))

        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
