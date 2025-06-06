from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QMessageBox

from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle



class AdminRoomList(QWidget):
    def __init__(self, main_window, room_list=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window
        self.room_list = room_list


        main_layout = QVBoxLayout()

        title = QLabel("🏠 Danh sách phòng trọ")
        title.setObjectName("Title")
        title.setFixedHeight(60)
        #title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;")
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
        # File: AdminRoomList.py (đoạn quan trọng)
        headers = ["STT", "Tên phòng", "Loại phòng", "Chủ trọ", "Người thuê", "Địa chỉ", "Xem chi tiết"]
        header_to_key = {
            "STT": "STT",  # sẽ đính số thứ tự ở view
            "Tên phòng": "room_name",
            "Loại phòng": "room_style",
            "Chủ trọ": "landlord_name",
            "Người thuê": "tenant_name",
            "Địa chỉ": "address"
        }

        # Khi populate, tableUI sẽ đọc đúng các key bên trên.
        # Đối với khóa "Xem chi tiết", button_callback sẽ dùng key "room_id" để mở chi tiết.

        self.table = TableUI(headers)
        self.table.populate(self.room_list, has_button=True, button_callback=self.show_detail, header_to_key=header_to_key)

        main_layout.addWidget(self.table)
        main_layout.addWidget(frame)
        self.setLayout(main_layout)

    def show_detail(self, row):
        try:
            room = self.room_list[row]
            id_room = room['room_id']

            # Mở Dashboard Room trong một cửa sổ mới
            from QLNHATRO.RentalManagementApplication.frontend.views.Rooms.MainWindowRoom import MainWindowRoom
            dashboard = MainWindowRoom(id_room)
            dashboard.show()

            # Giữ tham chiếu để cửa sổ không bị đóng do garbage collection
            if not hasattr(self, "_opened_windows"):
                self._opened_windows = []
            self._opened_windows.append(dashboard)

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể hiển thị chi tiết: {str(e)}")
