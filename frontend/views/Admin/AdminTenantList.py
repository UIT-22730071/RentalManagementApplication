from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QMessageBox

from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class AdminTenantList(QWidget):
    def __init__(self, main_window, tenant_list=None):
        super().__init__()
        self.main_window = main_window
        self.tenant_list = tenant_list or [
            {
                "stt": 1,
                "name": "Lê Thị C",
                "cccd": "012345678900",
                "phone": "0934567890",
                "email": "letc@example.com",
                "ngay_thue": "01/01/2024"
            },
            {
                "stt": 2,
                "name": "Phạm Văn D",
                "cccd": "112233445566",
                "phone": "0923456789",
                "email": "phamd@example.com",
                "ngay_thue": "15/03/2024"
            }
        ]

        self.setStyleSheet(GlobalStyle.global_stylesheet() + """
            QWidget {
                background-color: #F7F9FC;
            }
            QLabel {
                color: #202E66;
            }
        """)

        main_layout = QVBoxLayout()

        title = QLabel("📋 Danh sách người thuê trọ")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                border: 1px solid #dcdcdc;
                padding: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }
        """)

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
            QMessageBox.information(
                self,
                "Chi tiết người thuê",
                f"👤 {tenant['name']}\n🆔 {tenant['cccd']}\n📞 {tenant['phone']}\n📬 {tenant['email']}"
            )
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể hiển thị chi tiết: {str(e)}")
