from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QVBoxLayout, QWidget, QScrollArea, QFrame,
                             QLabel, QHBoxLayout, QPushButton)

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Form.LandlordUpdateFormView import LandlordUpdateFormView
from QLNHATRO.RentalManagementApplication.frontend.views.Form.TenantUpdateFormView import TenantUpdateFormView


class UpdateInfoView(QWidget):
    # Define signals
    save_clicked = pyqtSignal()
    cancel_clicked = pyqtSignal()

    def __init__(self, role, username, save_callback=None, cancel_callback=None):
        super().__init__()
        # Trong __init__ (UpdateInfoView)
        self.setFixedSize(GlobalStyle.WINDOW_WIDTH, GlobalStyle.WINDOW_HEIGHT)
        self.setStyleSheet(GlobalStyle.global_stylesheet())

        #self.setFixedSize(800, 700)  # hoặc kích thước bạn muốn
        self.role = role
        self.username = username
        self.save_callback = save_callback
        self.cancel_callback = cancel_callback
        self.initUI()

        print("role", role)
    def initUI(self):
        # Create main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Thêm scroll
        scroll = QScrollArea()


        scroll.setWidgetResizable(True)

        # Create card container to hold card
        scroll_content = QWidget()


        scroll.setWidget(scroll_content)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(0)

        # Create card
        card = QFrame()
        card.setObjectName("InfoCard")  # áp dụng style riêng
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(20, 20, 20, 20)
        card_layout.setSpacing(20)

        # Header
        header_layout = QVBoxLayout()

        # Main title
        title_label = QLabel("Cập nhật thông tin")
        #title_label.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        #title_label.setStyleSheet("color: #FF6B6B;")
        title_label.setObjectName("Title")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Role
        role_label = QLabel(f"[{self.role}]") # TODO: đang lỗi hiển thij trong page giao diện
        #role_label.setFont(QFont("Arial", 14))
        #role_label.setStyleSheet("color: #555;")
        role_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # User info
        user_info_frame = QFrame()
        '''
        user_info_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        '''
        user_info_layout = QHBoxLayout(user_info_frame)

        username_label = QLabel(f"👤 Tên đăng nhập: {self.username}")
        #username_label.setFont(QFont("Arial", 10))
        #username_label.setStyleSheet("color: #333;")

        password_label = QLabel("🔑 Mật khẩu: ********")
        #password_label.setFont(QFont("Arial", 10))
        #password_label.setStyleSheet("color: #333;")

        user_info_layout.addWidget(username_label)
        user_info_layout.addWidget(password_label)

        # Add to header layout
        header_layout.addWidget(title_label)
        header_layout.addWidget(role_label)
        header_layout.addWidget(user_info_frame)

        # Create form based on role
        if self.role == "Người thuê trọ":
            self.form = TenantUpdateFormView()
        else:
            self.form = LandlordUpdateFormView()

        # Create button layout
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(50, 0, 50, 0)

        # Save button
        self.btn_save = QPushButton("💾 Lưu thông tin")
        #self.btn_save.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        '''
        self.btn_save.setStyleSheet("""
            QPushButton {
                background-color: #FF6B6B;
                color: white;
                border-radius: 20px;
                padding: 12px 20px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #ff5252;
            }
            QPushButton:pressed {
                background-color: #e04545;
            }
        """)
        '''
        self.btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        # Save button
        self.btn_save.clicked.connect(self.handle_save_clicked)

        self.btn_cancel = QPushButton("❌ Hủy")
        #self.btn_cancel.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        '''
        self.btn_cancel.setStyleSheet("""
            QPushButton {
                background-color: #4FBEEE;
                color: white;
                border-radius: 20px;
                padding: 12px 20px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #3ba8d8;
            }
            QPushButton:pressed {
                background-color: #2b93c3;
            }
        """)
        '''
        self.btn_cancel.setCursor(Qt.CursorShape.PointingHandCursor)
        # Cancel button
        self.btn_cancel.clicked.connect(self.handle_cancel_clicked)
        #self.btn_cancel.clicked.connect(lambda: self.cancel_clicked.emit())

        # Add buttons to layout
        button_layout.addWidget(self.btn_save)
        button_layout.addWidget(self.btn_cancel)

        # Add everything to card layout
        card_layout.addLayout(header_layout)
        card_layout.addWidget(self.form)
        card_layout.addLayout(button_layout)

        # Add card to scroll layout
        scroll_layout.addWidget(card)

        # Add card to main layout
        main_layout.addWidget(scroll)

    def get_form_data(self):
        """Get form data from the form view"""
        return self.form.get_form_data()

    #TODO: Ở đây sẽ tạo 1 liên kết khi Save rồi sẽ trả về màn login
    def handle_save_clicked(self):
        if self.save_callback:
            self.save_callback()

    def handle_cancel_clicked(self):
        if self.cancel_callback:
            self.cancel_callback()
