from Demos.win32ts_logoff_disconnected import username
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QMessageBox

from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository
from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle



class AdminTenantList(QWidget):
    def __init__(self, main_window, tenant_list=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window
        self.tenant_list = tenant_list or [
            {
                "stt": 0,
                "name": "Chưa có ",
                "cccd": "00000000000",
                "phone": "000000000",
                "email": "00000000@example.com",
                "ngay_thue": "00/00/1901",
                "username":"tenant"
            }
        ]

        main_layout = QVBoxLayout()

        title = QLabel("📋 Danh sách người thuê trọ")
        title.setObjectName("Title")
        #title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;")
        title.setFixedHeight(60)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        frame = QFrame()
        '''
        frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                border: 1px solid #dcdcdc;
                padding: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }
        """)
        '''
        headers = ["STT", "Họ tên", "CCCD", "Số điện thoại", "Email", "Ngày bắt đầu thuê", "Xem chi tiết"]
        header_to_key = {
            "STT": "stt",
            "Họ tên": "name",
            "CCCD": "cccd",
            "Số điện thoại": "phone",
            "Email": "email",
            "Ngày bắt đầu thuê": "ngay_thue"
        }

        self.table = TableUI(headers)
        self.table.populate(self.tenant_list, has_button=True, button_callback=self.show_detail,
                            header_to_key=header_to_key)

        main_layout.addWidget(self.table)
        main_layout.addWidget(frame)
        self.setLayout(main_layout)

    def show_detail(self, row):
        try:
            tenant = self.tenant_list[row]
            username = tenant['username']
            id_tenant = TenantRepository.get_tenant_id_from_user_name(username)

            # Tạo và hiển thị dashboard người thuê trong cửa sổ mới
            from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.MainWindowTenant import MainWindowTenant
            dashboard = MainWindowTenant(id_tenant)
            dashboard.show()

            # Lưu lại tham chiếu để cửa sổ không bị thu hồi bộ nhớ
            if not hasattr(self, "_opened_windows"):
                self._opened_windows = []
            self._opened_windows.append(dashboard)
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể hiển thị chi tiết: {str(e)}")
