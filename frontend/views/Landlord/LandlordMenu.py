from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from QLNHATRO.RentalManagementApplication.frontend.Component.ButtonUI import ButtonUI
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordHome import LandlordHome


class LandlordMenu(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.current_page = None

        self.main_layout = QHBoxLayout()

        # ------------ LEFT MENU FRAME ------------
        self.left_frame = QWidget()
        self.left_frame.setFixedWidth(250)
        self.left_frame.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF6B6B, stop:1 #FFA07A);
            border-radius: 15px;
        """)

        left_layout = QVBoxLayout(self.left_frame)
        left_layout.setAlignment(Qt.AlignTop)

        # Label chào mừng
        self.label_landlord = QLabel("👋 Chào mừng đến với DASHBOARD Chủ trọ: Nguyễn Văn A")
        self.label_landlord.setStyleSheet("color: white; font-weight: bold; padding: 10px;")
        #left_layout.addWidget(self.label_landlord)

        # Tạo nút và áp dụng style
        button_ui = ButtonUI.landlord_dashboard_button()
        # TODO: Khi có đối tượng tạo và truy xuất đối tượng và các hàm liên quan thay cho lambda


        self.home_btn = QPushButton("🏠 Trang chính")
        button_ui.apply_style(self.home_btn)
        self.home_btn.clicked.connect(lambda : self.set_right_frame(LandlordHome))

        self.info_btn = QPushButton("👤 Thông tin chủ trọ")
        button_ui.apply_style(self.info_btn)
        self.info_btn.clicked.connect(lambda: print("clicked Thông tin chủ trọ"))

        self.infor_list_room_btn = QPushButton("📂 Danh sách phòng trọ")
        button_ui.apply_style(self.infor_list_room_btn)
        self.infor_list_room_btn.clicked.connect(lambda: print("clicked Danh sách phòng trọ"))

        self.create_new_room_btn = QPushButton("➕ Tạo phòng trọ mới")
        button_ui.apply_style(self.create_new_room_btn)
        self.create_new_room_btn.clicked.connect(lambda: print("clicked Tạo phòng trọ mới"))

        self.infor_list_invoice_btn = QPushButton("🧾 Danh sách hóa đơn")
        button_ui.apply_style(self.infor_list_invoice_btn)
        self.infor_list_invoice_btn.clicked.connect(lambda: print("clicked Danh sách hóa đơn"))

        self.add_adv_find_tenant_btn = QPushButton("🔍 Tìm người thuê mới")
        button_ui.apply_style(self.add_adv_find_tenant_btn)
        self.add_adv_find_tenant_btn.clicked.connect(lambda: print("clicked Tìm người thuê mới"))

        self.logout_btn = QPushButton("🚪 Đăng xuất")
        button_ui.apply_style(self.logout_btn)
        self.logout_btn.clicked.connect(lambda: print("clicked Đăng xuất"))

        self.exist_btn = QPushButton("❌ Thoát")
        button_ui.apply_style(self.exist_btn)
        self.exist_btn.clicked.connect(lambda: print("clicked Thoát"))

        # Thêm tất cả các button vào layout
        left_layout.addWidget(self.home_btn)
        left_layout.addWidget(self.info_btn)
        left_layout.addWidget(self.infor_list_room_btn)
        left_layout.addWidget(self.create_new_room_btn)
        left_layout.addWidget(self.infor_list_invoice_btn)
        left_layout.addWidget(self.add_adv_find_tenant_btn)
        left_layout.addWidget(self.logout_btn)
        left_layout.addWidget(self.exist_btn)

        # ----------- RIGHT FRAME (QStackedWidget) -----------
        self.right_frame = QWidget()
        self.right_layout = QVBoxLayout(self.right_frame)
        self.right_layout.setContentsMargins(0, 0, 0, 0)

        # Trang mặc định hiển thị Home page
        self.home_page = LandlordHome(self.main_window)
        self.right_layout.addWidget(self.set_right_frame(LandlordHome))  # page

        # Thêm vào layout chính
        self.main_layout.addWidget(self.left_frame)
        self.main_layout.addWidget(self.right_frame)
        self.setLayout(self.main_layout)


    def set_right_frame(self, PageClass):
        """Xóa trang hiện tại và thay bằng trang mới"""
        if self.current_page:
            self.right_layout.removeWidget(self.current_page)
            self.current_page.setParent(None)  # Xóa khỏi bộ nhớ

        self.current_page = PageClass(self.main_window)
        self.right_layout.addWidget(self.current_page)
