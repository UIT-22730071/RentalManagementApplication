from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
    QPushButton, QHBoxLayout, QHeaderView, QFrame
)

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
        self.setStyleSheet("""
            QWidget {
                background-color: #ecf0f1;
                color: white;
                font-family: Arial;
            }
            QPushButton {
                background-color: #1C0CFB;
                color: white;
                padding: 10px 10px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #d35400;
                background-color: #0056b3;
            }
            QTableWidget {
                background-color: #34495e;
                gridline-color: #ecf0f1;
                color: white;
                font-size: 14px;
                border: 2px solid #d35400;
                border-radius: 8px; 
            }
            QHeaderView::section {
                background-color: #FFA07A;
                color: white;
                font-weight: bold;
                padding: 6px;
                border-radius: 2px;
                border: 1px solid #d35400;
            }
        """)

        # Layout chính
        main_layout = QVBoxLayout()

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
        frame_layout = QVBoxLayout(frame)


        # Tạo bảng danh sách phòng
        self.table = QTableWidget()
        self.table.setColumnCount(8)  # 8 cột như yêu cầu
        self.table.setHorizontalHeaderLabels([
            "STT", "Tên phòng", "Người thuê", "Giá", "Diện tích", "Số nước", "Tình trạng hóa đơn", "Xem chi tiết"
        ])
        self.table.setRowCount(max(len(self.rooms), 10))  # Hiển thị ít nhất 10 dòng
        self.table.verticalHeader().setVisible(False)  # Ẩn cột index

        # Thiết lập cột tự động co dãn
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Điền dữ liệu vào bảng
        self.populate_table()

        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

    def populate_table(self):
        """Điền dữ liệu vào bảng"""
        for row, room in enumerate(self.rooms):
            self.table.setItem(row, 0, QTableWidgetItem(str(room["stt"])))
            self.table.setItem(row, 1, QTableWidgetItem(room["ten_phong"]))
            self.table.setItem(row, 2, QTableWidgetItem(room["nguoi_thue"]))
            self.table.setItem(row, 3, QTableWidgetItem(room["gia"]))
            self.table.setItem(row, 4, QTableWidgetItem(room["dien_tich"]))
            self.table.setItem(row, 5, QTableWidgetItem(room["so_nuoc"]))
            self.table.setItem(row, 6, QTableWidgetItem(room["hoa_don"]))

            # Thêm nút "Chi tiết"
            detail_btn = QPushButton("🔍 Chi tiết")
            detail_btn.clicked.connect(lambda _, r=row: self.show_room_details(r))
            self.table.setCellWidget(row, 7, detail_btn)

    def show_room_details(self, row):
        """Hiển thị chi tiết phòng khi bấm nút"""
        room = self.rooms[row]
        print(f"📌 Thông tin phòng {room['ten_phong']}: {room}")
        # TODO: Mở dialog chi tiết phòng tại đây nếu cần
