from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QFrame
)


from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class RoomList(QWidget):
    def __init__(self, main_window,room_list,id_lanlord):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window
        self.id_lanlord = id_lanlord
        self.id_room = None
        if room_list is not None:
            self.room_list = room_list
        else:
            # Dummy data fallback (chỉ dùng khi không có room_list)
            self.room_list = [
                {"stt": 1, "ten_phong": "Phòng 101", "nguoi_thue": "Nguyễn Văn A", "gia": "3,000,000 VND",
                 "so_dien": "20KWH", "so_nuoc": "15m³", "hoa_don": "Đã thanh toán"},
                {"stt": 2, "ten_phong": "Phòng 102", "nguoi_thue": "Trần Thị B", "gia": "2,800,000 VND",
                 "so_dien": "20KWH", "so_nuoc": "12m³", "hoa_don": "Chưa thanh toán"},
            ]

        # Layout chính
        main_layout = QVBoxLayout()
        #self.setStyleSheet("background-color: #ecf0f1;")
        # Tiêu đề
        title = QLabel("🏠 Danh sách phòng trọ")
        #title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;")
        title.setObjectName("Title")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Tạo khung chứa bảng (bo tròn + bóng đổ)
        frame = QFrame()
        frame.setObjectName("tableCard")


        #frame_layout = QVBoxLayout(frame)


        # Tạo bảng danh sách phòng
        # Tạo bảng danh sách phòng
        headers = [
            "STT", "Tên phòng", "Người thuê", "Giá", "Số điện", "Số nước", "Tình trạng hóa đơn", "Xem chi tiết"
        ]
        self.table = TableUI(headers)

        header_to_key = {
            "STT": "stt",
            "Tên phòng": "ten_phong",
            "Người thuê": "nguoi_thue",
            "Giá": "gia",
            "Số điện": "so_dien",
            "Số nước": "so_nuoc",
            "Tình trạng hóa đơn": "hoa_don"
        }

        self.table.populate(self.room_list, has_button=True,
                            button_callback=self.show_room_details,
                            header_to_key=header_to_key)


        main_layout.addWidget(self.table)
        main_layout.addWidget(frame)
        #self.setLayout(frame_layout)
        self.setLayout(main_layout)

    ## TODO: cần viết lại hàm show_room_details khi có model
    def show_room_details(self, row):
        """Xử lý khi nhấn nút 'Xem chi tiết'"""
        room = self.room_list[row]
        self.id_room = room.get('id_room')

        if self.id_room:
            print(f"🔍 Mở chi tiết phòng: {room['ten_phong']} (ID: {self.id_room})")
            from QLNHATRO.RentalManagementApplication.controller.RoomController.RoomMenuController import \
                RoomMenuController
            RoomMenuController.go_to_room_management(self.id_room)
        else:
            print("❌ Không tìm thấy ID phòng trong dữ liệu.")

