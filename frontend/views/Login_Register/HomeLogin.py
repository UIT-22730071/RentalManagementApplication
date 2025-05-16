

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QVBoxLayout, QPushButton, QStackedWidget, QLabel, QLineEdit, \
    QRadioButton

from QLNHATRO.RentalManagementApplication.controller.LoginRegister.LoginController import LoginController
from QLNHATRO.RentalManagementApplication.controller.LoginRegister.RegisterController import RegisterController
from QLNHATRO.RentalManagementApplication.frontend.Component.InputTextUI import InputTextUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class LoginWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()


        self.setStyleSheet(GlobalStyle.global_stylesheet())

        self.main_window = main_window  # Lưu lại để dùng cho chuyển trang
        self.main_window.setFixedSize(825, 600)
        self.main_window.setMinimumSize(825, 600)
        self.main_window.setMaximumSize(1200, 600)
        self.setStyleSheet("background-color: #202020; border-radius: 15px;")
        # Layout chính (chứa 2 phần trái + phải)
        # Layout chính
        #self.login_controller = LoginController()
        self.main_layout = QHBoxLayout(self)  # Đặt layout chính cho LoginWindow

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

        self.sign_in_btn = QPushButton("REGISTER")
        self.sign_in_btn.setFixedSize(150, 40)
        self.sign_in_btn.setStyleSheet("background-color: white; color: #FF6B6B; font-weight: bold; border-radius: 20px;")
        self.sign_in_btn.clicked.connect(lambda: self.expand_window(1))

        self.login_btn = QPushButton("LOGIN")
        self.login_btn.setFixedSize(150, 40)
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

        self.right_frame.setLayout(self.right_layout)

        # **Tạo StackedWidget để chứa LOGIN và SIGN IN**
        self.stacked_widget = QStackedWidget()
        self.right_layout.addWidget(self.stacked_widget)

        # Gọi hàm để thêm trang LOGIN và SIGN UP vào stacked_widget
        self.Form_Login(self.main_window)
        #TODO: tương tự formlogin và fix sau
        self.Form_sign_up()

        self.main_layout.addWidget(self.right_frame)
        self.expand_window(0)  # Hiển thị ngay trang Login

    def Form_Login(self, main_window):
        """Trang 1: Form Đăng nhập"""
        login_page = QWidget()
        login_layout = QVBoxLayout(login_page)

        login_label = QLabel("Đăng nhập")
        login_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        login_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.email_input = QLineEdit()
        InputTextUI.default_input().apply_style(self.email_input)
        self.email_input.setPlaceholderText("  Email")
        self.email_input.setFixedHeight(40)

        self.password_input = QLineEdit()
        InputTextUI.default_input().apply_style(self.password_input)
        self.password_input.setPlaceholderText("  Password")
        self.password_input.setFixedHeight(40)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        forgot_password = QLabel('<a href="#">❓ Quên mật khẩu?</a>')
        forgot_password.setStyleSheet("color: #FF6B6B; font-size: 12px;")
        forgot_password.setTextInteractionFlags(Qt.TextBrowserInteraction)
        forgot_password.setOpenExternalLinks(False)
        forgot_password.setAlignment(Qt.AlignRight)
        forgot_password.linkActivated.connect(lambda: LoginController.go_to_forgot_password_view())

        change_password = QLabel('<a href="#">🔐 Đổi mật khẩu?</a>')
        change_password.setStyleSheet("color: #FF6B6B; font-size: 12px;")
        change_password.setTextInteractionFlags(Qt.TextBrowserInteraction)
        change_password.setOpenExternalLinks(False)
        change_password.setAlignment(Qt.AlignLeft)
        change_password.linkActivated.connect(lambda: LoginController.go_to_change_password_view())

        login_btn = QPushButton("Đăng nhập")
        login_btn.setFixedHeight(45)
        login_btn.setStyleSheet("background-color: #233FF3; color: white; font-weight: bold; border-radius: 20px;")

        #TODO đang xử lý lỗi ở đây

        #login_btn.clicked.connect(lambda: LoginController.go_to_check_login_window(main_window,self,email_input.text(), password_input.text()))
        login_btn.clicked.connect(self.on_click_btn_login)

        exist_btn_login = QPushButton("Thoát")
        exist_btn_login.setFixedHeight(40)
        exist_btn_login.setStyleSheet("background-color: #FF6B6B; color: white; font-weight: bold; border-radius: 20px;")
        exist_btn_login.clicked.connect(self.close)

        login_layout.addWidget(login_label)
        login_layout.addWidget(self.email_input)
        login_layout.addWidget(self.password_input)

        password_links_layout = QHBoxLayout()
        password_links_layout.addWidget(change_password)
        password_links_layout.addWidget(forgot_password)
        login_layout.addLayout(password_links_layout)

        login_layout.addWidget(login_btn)
        login_layout.addWidget(exist_btn_login)

        self.stacked_widget.addWidget(login_page)

    def Form_sign_up(self):
        """Trang 2: Form Đăng ký"""
        signup_page = QWidget()
        signup_layout = QVBoxLayout(signup_page)

        signup_label = QLabel("Đăng ký")
        signup_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        signup_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        username_input = QLineEdit()
        InputTextUI.default_input().apply_style(username_input)
        username_input.setPlaceholderText("  Tên tài khoản")
        username_input.setFixedHeight(40)

        password_input = QLineEdit()
        InputTextUI.default_input().apply_style(password_input)
        password_input.setPlaceholderText("  Mật khẩu")
        password_input.setFixedHeight(40)
        password_input.setEchoMode(QLineEdit.EchoMode.Password)

        confirm_password_input = QLineEdit()
        InputTextUI.default_input().apply_style(confirm_password_input)
        confirm_password_input.setPlaceholderText("  Xác nhận mật khẩu")
        confirm_password_input.setFixedHeight(40)
        confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.role_selection = QRadioButton("Chủ trọ")
        self.tenant_selection = QRadioButton("Người thuê trọ")
        self.tenant_selection.setChecked(True)

        signup_btn = QPushButton("Đăng ký")
        signup_btn.setFixedHeight(45)
        signup_btn.setStyleSheet("background-color: #233FF3; color: white; font-weight: bold; border-radius: 20px;")
        signup_btn.clicked.connect(lambda: RegisterController.register_tenant(
            username_input.text(),
            password_input.text(),
            confirm_password_input.text(),
            self.get_selected_role(),
            self.main_window
        ))

        #TODO: Xử lý lấy thông tin qua page Update thông tin
        #TODO: Cần thêm 1 hàm check correct password , check đúng mới cho chuyển page

        # TODO" đúng MVC  ==> qua controller ==> gọi hàm kiểm ở Backend ==> mở register
        '''
        def go_to_check_sign_up(self, username, password, password_confirm, role, main_window=None):    
        signup_btn.clicked.connect(lambda: self.login_controller.go_to_check_sign_up(
            username_input.text(),
            password_input.text(),
            confirm_password_input.text(),
            self.tenant_selection.isChecked(),
            self.main_window  # thêm dòng này!
        ))'''

        # chỉ cần kiểm tra tenant selection là True hoặc Fall


        self.exist_btn_signup = QPushButton("Thoát")
        self.exist_btn_signup.setFixedHeight(40)
        #self.exist_btn_signup.setObjectName("CancelBtn")
        self.exist_btn_signup.setStyleSheet("background-color: #FF6B6B; color: white; font-weight: bold; border-radius: 20px;")
        ## TODO: Xử lý nhẹ phương thức sau
        self.exist_btn_signup.clicked.connect(lambda: self.close_window_menu())



        signup_layout.addStretch()
        signup_layout.addWidget(signup_label)
        signup_layout.addStretch()
        signup_layout.addWidget(username_input)
        signup_layout.addWidget(password_input)
        signup_layout.addWidget(confirm_password_input)
        signup_layout.addWidget(self.role_selection)
        signup_layout.addWidget(self.tenant_selection)

        signup_layout.addStretch()
        signup_layout.addWidget(signup_btn)
        signup_layout.addWidget(self.exist_btn_signup)

        self.stacked_widget.addWidget(signup_page)

    def expand_window(self, index):
        """Khi nhấn vào LOGIN hoặc SIGN IN, cửa sổ mở rộng ra"""
        self.right_frame.setVisible(True)
        self.stacked_widget.setCurrentIndex(index)


    def on_click_btn_login(self):
        from QLNHATRO.RentalManagementApplication.controller.LoginRegister.LoginController import LoginController
        LoginController.on_click_btn_login_test_new(self.main_window, self.email_input.text(), self.password_input.text())

    def get_selected_role(self):
        return "Người thuê trọ" if self.tenant_selection.isChecked() else "Chủ trọ"

    def close_window_menu(self):
        self.main_window.close()