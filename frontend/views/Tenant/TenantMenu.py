from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QPushButton
from torch.distributed.fsdp.wrap import lambda_auto_wrap_policy

from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository
from QLNHATRO.RentalManagementApplication.controller.AdminController.AdminController import AdminController
from QLNHATRO.RentalManagementApplication.controller.LandlordController.LandlordController import LandlordController
from QLNHATRO.RentalManagementApplication.controller.TenantController.TenantController import TenantController
from QLNHATRO.RentalManagementApplication.frontend.Component.ButtonUI import ButtonUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class TenantMenu(QWidget):
    def __init__(self, main_window=None, user_id = None):
        super().__init__()
        print("[DEBUG] TenantMenu khởi tạo")
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window
        self.current_page = None
        self.id_tenant = TenantRepository.get_tenant_id_from_user_id(user_id)

        self.main_window.setWindowTitle("Dashboard Người Thuê trọ")
        #self.main_window.setGeometry(300, 100, 1000, 600)
        self.main_window.resize(GlobalStyle.WINDOW_WIDTH, GlobalStyle.WINDOW_HEIGHT)
        self.main_window.setMinimumSize(GlobalStyle.WINDOW_WIDTH, GlobalStyle.WINDOW_HEIGHT)
        self.main_window.setMaximumSize(GlobalStyle.WINDOW_WIDTH, GlobalStyle.WINDOW_HEIGHT)

        '''
        self.main_window.setStyleSheet("""
                    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF6B6B, stop:1 #FFA07A);
                    border-radius: 15px;
                """)
        '''
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
        self.home_btn.clicked.connect(lambda: TenantController.go_to_home_page(self, self.id_tenant))

        self.info_btn = QPushButton("👤 Thông tin cá nhân")
        button_ui.apply_style(self.info_btn)
        self.info_btn.clicked.connect(lambda: TenantController.go_to_tenant_info_page(self, self.id_tenant))
        #TODO: fix xong repari call function
        self.room_info_btn = QPushButton("🚪 Thông tin phòng")
        button_ui.apply_style(self.room_info_btn)
        self.room_info_btn.clicked.connect(lambda: TenantController.go_to_tenant_room_infor_page(self,self.id_tenant))

        self.invoice_list_btn = QPushButton("🧾 Danh sách hóa đơn")
        button_ui.apply_style(self.invoice_list_btn)
        self.invoice_list_btn.clicked.connect(lambda: TenantController.go_to_tenant_invoice_list_page(self, self.id_tenant))

        self.find_new_room = QPushButton("💰 Tìm phòng trọ")
        button_ui.apply_style(self.find_new_room)
        self.find_new_room.clicked.connect(lambda: TenantController.go_to_tenant_find_new_room_page(self,self.id_tenant))

        self.maintenance_btn = QPushButton("🔧 Yêu cầu sửa chữa")
        button_ui.apply_style(self.maintenance_btn)
        self.maintenance_btn.clicked.connect(lambda: TenantController.go_to_tenant_maintenance_request(self, self.id_tenant))

        self.logout_btn = QPushButton("🚪 Đăng xuất")
        button_ui.apply_style(self.logout_btn)
        self.logout_btn.clicked.connect(lambda: LandlordController.handle_logout(self))

        self.exit_btn = QPushButton("❌ Thoát")
        button_ui.apply_style(self.exit_btn)
        self.exit_btn.clicked.connect(lambda: self.close_window_menu())

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
        #self.home_page = TenantHome(self.main_window)
        #self.right_layout.addWidget(self.set_right_frame(TenantHome))
        TenantController.go_to_home_page(self, self.id_tenant)
        # Add to main layout
        self.main_layout.addWidget(self.left_frame)
        self.main_layout.addWidget(self.right_frame)
        self.setLayout(self.main_layout)

    def set_right_frame(self, PageClass):
        if self.current_page:
            self.right_layout.removeWidget(self.current_page)
            self.current_page.setParent(None)

        try:
            if callable(PageClass):  # lambda trả về instance
                self.current_page = PageClass()
            else:
                self.current_page = PageClass(self.main_window, self.id_tenant)
        except TypeError as e:
            print(f"[⚠️ Cảnh báo] {PageClass.__name__} không nhận 2 tham số: {e}")
            self.current_page = PageClass(self.main_window)

        self.right_layout.addWidget(self.current_page)
        return self.current_page

    def close_window_menu(self):
        self.main_window.close()