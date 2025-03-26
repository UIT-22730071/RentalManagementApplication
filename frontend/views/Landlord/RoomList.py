from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
    QPushButton, QHBoxLayout, QHeaderView, QFrame
)

from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI


class RoomList(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.rooms = [
            # Dummy data mẫu
            {"stt": 1, "ten_phong": "Phòng 101", "nguoi_thue": "Nguyễn Văn A", "gia": "3,000,000 VND",
             "dien_tich": "20m²", "so_nuoc": "15m³", "hoa_don": "Đã thanh toán"},
            {"stt": 2, "ten_phong": "Phòng 102", "nguoi_thue": "Trần Thị B", "gia": "2,800,000 VND",
             "dien_tich": "18m²", "so_nuoc": "12m³", "hoa_don": "Chưa thanh toán"},
            # Có thể thêm nhiều phòng khác...
        ]

        # Layout chính
        main_layout = QVBoxLayout()
        self.setStyleSheet("background-color: #ecf0f1;")
        # Tiêu đề
        title = QLabel("🏠 Danh sách phòng trọ")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Tạo khung chứa bảng (bo tròn + bóng đổ)
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
        #frame_layout = QVBoxLayout(frame)


        # Tạo bảng danh sách phòng
        headers=[
            "STT", "Tên phòng", "Người thuê", "Giá", "Diện tích", "Số nước", "Tình trạng hóa đơn", "Xem chi tiết"
        ]
        self.table = TableUI(headers)
        self.table.populate(self.rooms, has_button=True, button_callback=self.show_room_details)

        main_layout.addWidget(self.table)
        main_layout.addWidget(frame)
        #self.setLayout(frame_layout)
        self.setLayout(main_layout)

    ## TODO: cần viết lại hàm show_room_details khi có model
    def show_room_details(self, row):
        """Hiển thị chi tiết phòng khi bấm nút"""
        room = self.rooms[row]
        print(f"📌 Thông tin phòng {room['ten_phong']}: {room}")
        # TODO: Mở dialog chi tiết phòng tại đây nếu cần
