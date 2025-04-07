from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from QLNHATRO.RentalManagementApplication.frontend.Component.ButtonUI import ButtonUI
from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.FindNewRoom import FindNewRoom

from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantHome import TenantHome
from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantInfo import TenantInfo
from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantRoomInfo import TenantRoomInfo
from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantInvoiceList import TenantInvoiceList
from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantPayment import TenantPayment
from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantMaintenanceRequest import TenantMaintenanceRequest


class TenantMenu(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.current_page = None

        self.main_layout = QHBoxLayout()

        # ------------ LEFT MENU FRAME ------------
        self.left_frame = QWidget()
        self.left_frame.setFixedWidth(250)
        self.left_frame.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4FC3F7, stop:1 #81D4FA);
            border-radius: 15px;
        """)

        left_layout = QVBoxLayout(self.left_frame)
        left_layout.setAlignment(Qt.AlignTop)

        # Button UI for consistent styling
        button_ui = ButtonUI.tenant_dashboard_button()

        # Create buttons with tenant-specific functionality
        self.home_btn = QPushButton("🏠 Trang chính")
        button_ui.apply_style(self.home_btn)
        self.home_btn.clicked.connect(lambda: self.set_right_frame(TenantHome))

        self.info_btn = QPushButton("👤 Thông tin cá nhân")
        button_ui.apply_style(self.info_btn)
        self.info_btn.clicked.connect(lambda: self.set_right_frame(TenantInfo))

        self.room_info_btn = QPushButton("🚪 Thông tin phòng")
        button_ui.apply_style(self.room_info_btn)
        self.room_info_btn.clicked.connect(lambda: self.set_right_frame(TenantRoomInfo))

        self.invoice_list_btn = QPushButton("🧾 Danh sách hóa đơn")
        button_ui.apply_style(self.invoice_list_btn)
        self.invoice_list_btn.clicked.connect(lambda: self.set_right_frame(TenantInvoiceList))

        self.find_new_room = QPushButton("💰 Tìm phòng trọ")
        button_ui.apply_style(self.find_new_room)
        self.find_new_room.clicked.connect(lambda: self.set_right_frame(FindNewRoom))

        self.maintenance_btn = QPushButton("🔧 Yêu cầu sửa chữa")
        button_ui.apply_style(self.maintenance_btn)
        self.maintenance_btn.clicked.connect(lambda: self.set_right_frame(TenantMaintenanceRequest))

        self.logout_btn = QPushButton("🚪 Đăng xuất")
        button_ui.apply_style(self.logout_btn)
        self.logout_btn.clicked.connect(lambda: print("Clicked Logout"))

        self.exit_btn = QPushButton("❌ Thoát")
        button_ui.apply_style(self.exit_btn)
        self.exit_btn.clicked.connect(lambda: self.main_window.go_to_exs(self.main_window))

        # Add buttons to layout
        left_layout.addWidget(self.home_btn)
        left_layout.addWidget(self.info_btn)
        left_layout.addWidget(self.room_info_btn)
        left_layout.addWidget(self.invoice_list_btn)
        left_layout.addWidget(self.find_new_room)
        left_layout.addWidget(self.maintenance_btn)
        left_layout.addWidget(self.logout_btn)
        left_layout.addWidget(self.exit_btn)

        # ----------- RIGHT FRAME (QStackedWidget) -----------
        self.right_frame = QWidget()
        self.right_layout = QVBoxLayout(self.right_frame)
        self.right_layout.setContentsMargins(0, 0, 0, 0)

        # Default page is Home page
        self.home_page = TenantHome(self.main_window)
        self.right_layout.addWidget(self.set_right_frame(TenantHome))

        # Add to main layout
        self.main_layout.addWidget(self.left_frame)
        self.main_layout.addWidget(self.right_frame)
        self.setLayout(self.main_layout)

    def set_right_frame(self, PageClass):
        """Remove current page and replace with new page"""
        if self.current_page:
            self.right_layout.removeWidget(self.current_page)
            self.current_page.setParent(None)  # Remove from memory

        self.current_page = PageClass(self.main_window)
        self.right_layout.addWidget(self.current_page)
        return self.current_page