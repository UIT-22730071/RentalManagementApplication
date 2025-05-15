from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QMessageBox

from QLNHATRO.RentalManagementApplication.Repository.LandlordRepository import LanlordRepository
from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle



class AdminLandlordList(QWidget):
    def __init__(self, main_window, landlord_list=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window
        self._opened_windows = []
        self.landlord_list = landlord_list or [
            {
                "stt": 1,
                "name": "Nguyễn Văn A",
                "cccd": "123456789012",
                "phone": "0901234567",
                "email": "nguyenvana@example.com",
                "so_phong": 5
            },
            {
                "stt": 2,
                "name": "Trần Thị B",
                "cccd": "987654321098",
                "phone": "0912345678",
                "email": "tranthib@example.com",
                "so_phong": 3
            }
        ]



        main_layout = QVBoxLayout()

        title = QLabel("📋 Danh sách chủ trọ")
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
        headers = [
            "STT", "Họ tên", "CCCD", "Số điện thoại", "Email", "Số lượng phòng", "Xem chi tiết"
        ]
        header_to_key = {
            "STT": "stt",
            "Họ tên": "name",
            "CCCD": "cccd",
            "Số điện thoại": "phone",
            "Email": "email",
            "Số lượng phòng": "so_phong"
        }

        self.table = TableUI(headers)
        self.table.populate(self.landlord_list, has_button=True, button_callback=self.show_detail,
                            header_to_key=header_to_key)

        main_layout.addWidget(self.table)
        main_layout.addWidget(frame)
        self.setLayout(main_layout)

    def show_detail(self, row):
        try:
            landlord = self.landlord_list[row]
            username = landlord['username']
            id_landlord = LanlordRepository.get_id_landlord_from_user_id(username)

            # Mở Dashboard của chủ trọ trong cửa sổ mới
            from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.MainWindowLandlord import \
                MainWindowLandlord
            dashboard = MainWindowLandlord(id_landlord)
            dashboard.show()

            # Lưu lại tham chiếu để cửa sổ không bị thu hồi bộ nhớ
            if not hasattr(self, "_opened_windows"):
                self._opened_windows = []
            self._opened_windows.append(dashboard)
            #QMessageBox.information(self, "Chi tiết", f"👤 {landlord['name']}\n📞 {landlord['phone']}\n📬 {landlord['email']}")
            # Hoặc gọi controller mở chi tiết nếu có sẵn:
            # AdminController.open_landlord_detail(landlord['id_landlord'])

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể hiển thị chi tiết: {str(e)}")
