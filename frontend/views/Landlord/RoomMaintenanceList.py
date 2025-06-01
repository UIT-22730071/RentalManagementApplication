from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout, QPushButton, QMessageBox,
    QTableWidget, QTableWidgetItem, QHeaderView
)

from QLNHATRO.RentalManagementApplication.frontend.Component.ConfirmDialog import ConfirmDialog

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class RoomMaintenanceList(QWidget):
    def __init__(self, main_window, maintenance_requests=None, id_landlord=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window
        self.id_landlord = id_landlord

        # Dữ liệu yêu cầu bảo trì
        if maintenance_requests is not None:
            self.maintenance_requests = maintenance_requests
        else:
            # Dummy data fallback (chỉ dùng khi không có maintenance_requests)
            self.maintenance_requests = [
                {
                    "stt": 1,
                    "request_id": 101,
                    "room_id": 1,
                    "room_name": "Phòng 101",
                    "tenant_id": 10,
                    "tenant_name": "Nguyễn Văn A",
                    "tenant_phone": "0912345678",
                    "issue_type": "Điện",
                    "urgency_level": "Khẩn cấp",
                    "description": "Mất điện toàn bộ phòng",
                    "contact_phone": "0912345678",
                    "available_time": "08:00-12:00",
                    "discovery_date": "2025-06-01",
                    "image_path": "",
                    "status": "Pending",
                    "created_at": "2025-06-01T13:00:00"
                },
                {
                    "stt": 2,
                    "request_id": 102,
                    "room_id": 2,
                    "room_name": "Phòng 102",
                    "tenant_id": 2,
                    "tenant_name": "Nguyễn Văn C",
                    "tenant_phone": "0912345678",
                    "issue_type": "Điện",
                    "urgency_level": "Khẩn cấp",
                    "description": "Mất điện toàn bộ phòng",
                    "contact_phone": "0912345678",
                    "available_time": "08:00-12:00",
                    "discovery_date": "2025-06-01",
                    "image_path": "",
                    "status": "Pending",
                    "created_at": "2025-06-01T13:00:00"
                },
                {
                    "stt": 3,
                    "request_id": 103,
                    "room_id": 3,
                    "room_name": "Phòng 103",
                    "tenant_id": 3,
                    "tenant_name": "Nguyễn Văn C",
                    "tenant_phone": "0912345678",
                    "issue_type": "Điện",
                    "urgency_level": "Khẩn cấp",
                    "description": "Mất điện toàn bộ phòng",
                    "contact_phone": "0912345678",
                    "available_time": "08:00-12:00",
                    "discovery_date": "2025-06-01",
                    "image_path": "",
                    "status": "Pending",
                    "created_at": "2025-06-01T13:00:00"
                }
            ]

        self.setup_ui()

    def setup_ui(self):
        """Thiết lập giao diện"""
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)  # Tăng khoảng cách giữa các phần tử
        main_layout.setContentsMargins(20, 20, 20, 20)  # Thêm margin cho layout chính

        # Tiêu đề - sử dụng GlobalStyle
        title = QLabel("🔧 Danh sách yêu cầu bảo trì phòng trọ")
        title.setObjectName("Title")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Thống kê nhanh
        stats_widget = self.create_stats_section()
        main_layout.addWidget(stats_widget)

        # Khung chứa bảng - áp dụng tableCard style từ GlobalStyle
        table_frame = QFrame()
        table_frame.setObjectName("tableCard")
        table_layout = QVBoxLayout(table_frame)
        table_layout.setContentsMargins(15, 15, 15, 15)

        # Tạo bảng danh sách yêu cầu bảo trì trực tiếp với QTableWidget
        self.headers = [
            "STT", "Phòng", "Người thuê", "Loại sự cố", "Mức độ",
            "Trạng thái", "Ngày tạo", "SĐT liên hệ", "Chi tiết", "Xử lý"
        ]

        self.table = QTableWidget()
        self.setup_table()

        # Mapping header tới key trong data
        self.header_to_key = {
            "STT": "stt",
            "Phòng": "room_name",
            "Người thuê": "tenant_name",
            "Loại sự cố": "issue_type",
            "Mức độ": "urgency_level",
            "Trạng thái": "status",
            "Ngày tạo": "created_at",
            "SĐT liên hệ": "contact_phone"
        }

        # Populate dữ liệu vào bảng
        self.populate_table()

        table_layout.addWidget(self.table)
        main_layout.addWidget(table_frame)

        self.setLayout(main_layout)

    def create_stats_section(self):
        """Tạo section thống kê nhanh với GlobalStyle"""
        stats_frame = QFrame()
        stats_frame.setObjectName("tableCard")  # Sử dụng style card từ GlobalStyle
        stats_layout = QHBoxLayout(stats_frame)
        stats_layout.setContentsMargins(20, 15, 20, 15)
        stats_layout.setSpacing(15)

        # Đếm số lượng theo trạng thái
        pending_count = len([req for req in self.maintenance_requests if req['status'] in ['Pending']])
        in_progress_count = len(
            [req for req in self.maintenance_requests if req['status'] in ['Đang xử lý', 'In Progress']])
        urgent_count = len([req for req in self.maintenance_requests if req['urgency_level'] == 'Khẩn cấp'])

        # Tạo các label thống kê với style cải tiến
        stats_info = [
            (f"📋 Tổng yêu cầu: {len(self.maintenance_requests)}", GlobalStyle.PRIMARY_COLOR),
            (f"⏳ Chờ xử lý: {pending_count}", "#e74c3c"),
            (f"🔄 Đang xử lý: {in_progress_count}", "#f39c12"),
            (f"🚨 Khẩn cấp: {urgent_count}", "#e74c3c")
        ]

        for text, color in stats_info:
            label = QLabel(text)
            label.setObjectName("valueLabel")  # Sử dụng style từ GlobalStyle
            label.setStyleSheet(f"""
                QLabel#valueLabel {{
                    background-color: {color};
                    color: white;
                    font-size: 14px;
                    font-weight: 600;
                    padding: 12px 16px;
                    border-radius: 8px;
                    margin: 2px;
                    min-width: 120px;
                }}
            """)
            label.setAlignment(Qt.AlignCenter)
            stats_layout.addWidget(label)

        stats_layout.addStretch()
        return stats_frame

    def setup_table(self):
        """Thiết lập cấu hình cho bảng"""
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)
        self.table.setRowCount(len(self.maintenance_requests))

        # Cài đặt header và các thuộc tính chung
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.setShowGrid(True)
        self.table.verticalHeader().setDefaultSectionSize(50)

        # Áp dụng style từ GlobalStyle
        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: {GlobalStyle.MAIN_BG};
                color: {GlobalStyle.TEXT_COLOR};
                font-size: 14px;
                font-family: {GlobalStyle.FONT_FAMILY};
                border: 1px solid #EBEBF0;
                border-radius: 8px;
                gridline-color: #EBEBF0;
            }}

            QTableWidget QHeaderView::section {{
                background-color: {GlobalStyle.TABLE_HEADER_BG};
                color: {GlobalStyle.TABLE_TEXT_COLOR};
                font-size: 14px;
                font-weight: 500;
                font-family: {GlobalStyle.FONT_FAMILY};
                padding: 12px 8px;
                border: none;
                border-bottom: 2px solid #E5E5E5;
            }}

            QTableWidget::item {{
                padding: 8px;
                border-bottom: 1px solid #F0F0F0;
            }}

            QTableWidget::item:selected {{
                background-color: #EAF2FF;
                color: {GlobalStyle.TEXT_COLOR};
            }}

            QTableWidget::item:hover {{
                background-color: #F8FAFC;
            }}
        """)

    def populate_table(self):
        """Điền dữ liệu vào bảng"""
        for row, row_data in enumerate(self.maintenance_requests):
            for col, header in enumerate(self.headers):
                if header in ["Chi tiết", "Xử lý"]:
                    # Bỏ qua các cột button, sẽ xử lý riêng
                    continue

                # Lấy key tương ứng với header
                key = self.header_to_key.get(header, header)
                value = row_data.get(key, "")

                # Tạo item với style đặc biệt cho một số cột
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)

                # Style đặc biệt cho cột trạng thái
                if header == "Trạng thái":
                    if value == "Khẩn cấp" or value == "Pending":
                        item.setBackground(QColor("#FEF2F2"))
                        item.setForeground(QColor("#DC2626"))
                    elif value == "Đang xử lý":
                        item.setBackground(QColor("#FEF3C7"))
                        item.setForeground(QColor("#D97706"))

                # Style đặc biệt cho cột mức độ
                elif header == "Mức độ":
                    if value == "Khẩn cấp":
                        item.setBackground(QColor("#FEE2E2"))
                        item.setForeground(QColor("#DC2626"))

                self.table.setItem(row, col, item)

        # Thêm các button sau khi điền dữ liệu
        self.add_detail_buttons()
        self.add_action_buttons()

    def add_detail_buttons(self):
        """Thêm button 'Chi tiết' vào cột tương ứng"""
        detail_col = self.headers.index("Chi tiết")

        for row in range(len(self.maintenance_requests)):
            detail_btn = QPushButton("🔍 Chi tiết")
            detail_btn.setObjectName("detailBtn")
            detail_btn.setStyleSheet(f"""
                QPushButton#detailBtn {{
                    background-color: {GlobalStyle.PRIMARY_COLOR};
                    color: white;
                    font-size: 12px;
                    font-weight: 500;
                    font-family: {GlobalStyle.FONT_FAMILY};
                    padding: 8px 16px;
                    border-radius: 8px;
                    border: none;
                    margin: 2px;
                    min-width: 100px;
                }}
                QPushButton#detailBtn:hover {{
                    background-color: #1D4DA5;
                    transform: translateY(-1px);
                }}
                QPushButton#detailBtn:pressed {{
                    background-color: #1A4299;
                }}
            """)

            detail_btn.clicked.connect(lambda checked, r=row: self.show_request_details(r))
            self.table.setCellWidget(row, detail_col, detail_btn)

    def add_action_buttons(self):
        """Thêm button 'Xử lý' vào cột tương ứng"""
        action_col = self.headers.index("Xử lý")

        for row in range(len(self.maintenance_requests)):
            action_btn = QPushButton("🔧 Xử lý")
            action_btn.setObjectName("actionBtn")

            # Kiểm tra trạng thái để disable button nếu đã xử lý
            current_status = self.maintenance_requests[row].get('status', '')
            if current_status in ['Hoàn thành', 'Completed']:
                action_btn.setText("✅ Hoàn thành")
                action_btn.setEnabled(False)
                action_btn.setStyleSheet(f"""
                    QPushButton#actionBtn {{
                        background-color: #27AE60;
                        color: white;
                        font-size: 12px;
                        font-weight: 500;
                        font-family: {GlobalStyle.FONT_FAMILY};
                        padding: 8px 16px;
                        border-radius: 8px;
                        border: none;
                        margin: 2px;
                        min-width: 100px;
                    }}
                """)
            else:
                action_btn.setStyleSheet(f"""
                    QPushButton#actionBtn {{
                        background-color: {GlobalStyle.BUTTON_SPECIAL_COLOR};
                        color: white;
                        font-size: 12px;
                        font-weight: 500;
                        font-family: {GlobalStyle.FONT_FAMILY};
                        padding: 8px 16px;
                        border-radius: 8px;
                        border: none;
                        margin: 2px;
                        min-width: 100px;
                    }}
                    QPushButton#actionBtn:hover {{
                        background-color: #1E35CC;
                        transform: translateY(-1px);
                    }}
                    QPushButton#actionBtn:pressed {{
                        background-color: #162BB8;
                    }}
                """)

            action_btn.clicked.connect(lambda checked, r=row: self.handle_maintenance_request(r))

            self.table.setCellWidget(row, action_col, action_btn)

    def show_request_details(self, row):
        request_data = self.maintenance_requests[row]
        request_data["id_landlord"] = self.id_landlord
        from QLNHATRO.RentalManagementApplication.controller.MaintenanceController.MaintenanceController import \
            MaintenanceController
        MaintenanceController.go_to_maintenance_detail_page(self, request_data)

    def handle_maintenance_request(self, row):
        """Xử lý yêu cầu bảo trì với style MessageBox cải tiến"""
        request = self.maintenance_requests[row]
        request_id = request['request_id']

        # Hiển thị dialog xác nhận với style
        reply = QMessageBox.question(
            self,
            'Xác nhận xử lý',
            f"Bạn có muốn cập nhật trạng thái yêu cầu bảo trì của {request['room_name']} thành 'Đang xử lý'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        # Áp dụng style cho dialog xác nhận
        confirmed = ConfirmDialog.ask(self, f"Bạn có muốn cập nhật trạng thái yêu cầu bảo trì của {request['room_name']} thành 'Đang xử lý'?")

        if confirmed == QMessageBox.Yes:
            # Cập nhật trạng thái trong data
            self.maintenance_requests[row]['status'] = 'Đang xử lý'

            # Refresh lại bảng và stats
            self.refresh_table()
            self.refresh_stats()

            # Thông báo thành công
            success_msg = QMessageBox()
            success_msg.setIcon(QMessageBox.Information)
            success_msg.setWindowTitle("Thành công")
            success_msg.setText(f"Đã cập nhật trạng thái yêu cầu bảo trì của {request['room_name']} thành 'Đang xử lý'")
            # Style cho thông báo thành công

            success_msg.setStyleSheet(f"""
                QMessageBox {{
                    background-color: {GlobalStyle.MAIN_BG};
                    color: {GlobalStyle.TEXT_COLOR};
                    font-family: {GlobalStyle.FONT_FAMILY};
                }}
                QMessageBox QPushButton {{
                    background-color: #27AE60;
                    color: white;
                    font-size: 14px;
                    font-family: {GlobalStyle.FONT_FAMILY};
                    padding: 8px 20px;
                    border-radius: 6px;
                    min-width: 80px;
                }}
                QMessageBox QPushButton:hover {{
                    background-color: #229954;
                }}
            """)

            success_msg.exec_()

            # TODO: Gọi controller để cập nhật database
            # MaintenanceController.update_status(request_id, 'Đang xử lý')
            from QLNHATRO.RentalManagementApplication.services.MaintenanceService import MaintenanceService
            result = MaintenanceService.update_maintenance_status(request_id, 'Đang xử lý')

    def refresh_table(self):
        """Refresh lại bảng sau khi cập nhật dữ liệu"""
        # Xóa và thiết lập lại bảng
        self.table.setRowCount(0)
        self.table.setRowCount(len(self.maintenance_requests))

        # Populate lại dữ liệu
        self.populate_table()

    def refresh_stats(self):
        """Refresh lại section thống kê"""
        # Tìm và cập nhật lại stats section
        # Có thể implement cách refresh stats section tại đây
        pass

    def filter_by_status(self, status):
        """Lọc theo trạng thái"""
        if status == "all":
            filtered_requests = self.maintenance_requests
        else:
            filtered_requests = [req for req in self.maintenance_requests if req['status'] == status]

        # Cập nhật dữ liệu hiển thị
        self.current_filtered_data = filtered_requests
        self.table.setRowCount(len(filtered_requests))

        # Populate dữ liệu đã lọc
        for row, row_data in enumerate(filtered_requests):
            for col, header in enumerate(self.headers):
                if header in ["Chi tiết", "Xử lý"]:
                    continue

                key = self.header_to_key.get(header, header)
                value = row_data.get(key, "")

                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)

                # Style cho trạng thái
                if header == "Trạng thái":
                    if value == "Khẩn cấp" or value == "Pending":
                        item.setBackground(Qt.color("#FEF2F2"))
                        item.setForeground(Qt.color("#DC2626"))
                    elif value == "Đang xử lý":
                        item.setBackground(Qt.color("#FEF3C7"))
                        item.setForeground(Qt.color("#D97706"))

                self.table.setItem(row, col, item)

        # Thêm buttons cho dữ liệu đã lọc
        self.add_filtered_buttons(filtered_requests)

    def filter_by_urgency(self, urgency):
        """Lọc theo mức độ khẩn cấp"""
        if urgency == "all":
            filtered_requests = self.maintenance_requests
        else:
            filtered_requests = [req for req in self.maintenance_requests if req['urgency_level'] == urgency]

        # Tương tự như filter_by_status
        self.current_filtered_data = filtered_requests
        self.table.setRowCount(len(filtered_requests))

        for row, row_data in enumerate(filtered_requests):
            for col, header in enumerate(self.headers):
                if header in ["Chi tiết", "Xử lý"]:
                    continue

                key = self.header_to_key.get(header, header)
                value = row_data.get(key, "")

                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)

                if header == "Mức độ":
                    if value == "Khẩn cấp":
                        item.setBackground(Qt.color("#FEE2E2"))
                        item.setForeground(Qt.color("#DC2626"))

                self.table.setItem(row, col, item)

        self.add_filtered_buttons(filtered_requests)

    def add_filtered_buttons(self, filtered_data):
        """Thêm buttons cho dữ liệu đã lọc"""
        detail_col = self.headers.index("Chi tiết")
        action_col = self.headers.index("Xử lý")

        for row in range(len(filtered_data)):
            # Button Chi tiết
            detail_btn = QPushButton("🔍 Chi tiết")
            detail_btn.setObjectName("detailBtn")
            detail_btn.setStyleSheet(f"""
                QPushButton#detailBtn {{
                    background-color: {GlobalStyle.PRIMARY_COLOR};
                    color: white;
                    font-size: 12px;
                    font-weight: 500;
                    font-family: {GlobalStyle.FONT_FAMILY};
                    padding: 8px 16px;
                    border-radius: 8px;
                    min-width: 100px;
                }}
                QPushButton#detailBtn:hover {{
                    background-color: #1D4DA5;
                }}
            """)

            # Tìm index gốc của item này trong data chính
            original_index = self.maintenance_requests.index(filtered_data[row])
            detail_btn.clicked.connect(lambda checked, r=original_index: self.show_request_details(r))
            self.table.setCellWidget(row, detail_col, detail_btn)

            # Button Xử lý
            action_btn = QPushButton("🔧 Xử lý")
            action_btn.setObjectName("actionBtn")

            current_status = filtered_data[row].get('status', '')
            if current_status in ['Hoàn thành', 'Completed']:
                action_btn.setText("✅ Hoàn thành")
                action_btn.setEnabled(False)
                action_btn.setStyleSheet(f"""
                    QPushButton#actionBtn {{
                        background-color: #27AE60;
                        color: white;
                        font-size: 12px;
                        font-family: {GlobalStyle.FONT_FAMILY};
                        padding: 8px 16px;
                        border-radius: 8px;
                        min-width: 100px;
                    }}
                """)
            else:
                action_btn.setStyleSheet(f"""
                    QPushButton#actionBtn {{
                        background-color: {GlobalStyle.BUTTON_SPECIAL_COLOR};
                        color: white;
                        font-size: 12px;
                        font-weight: 500;
                        font-family: {GlobalStyle.FONT_FAMILY};
                        padding: 8px 16px;
                        border-radius: 8px;
                        min-width: 100px;
                    }}
                    QPushButton#actionBtn:hover {{
                        background-color: #1E35CC;
                    }}
                """)

            action_btn.clicked.connect(lambda checked, r=original_index: self.handle_maintenance_request(r))
            self.table.setCellWidget(row, action_col, action_btn)