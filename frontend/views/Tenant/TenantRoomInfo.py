from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QGroupBox, QSizePolicy, QScrollArea, \
    QFrame
from PyQt5.QtCore import Qt



class TenantRoomInfo(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # Improved styling with backgrounds for all information areas
        self.setStyleSheet("""
            QWidget {
                background-color: #E9FBFC;
                color: white;
                border-radius: 15px;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #3498db;
                border-radius: 10px;
                margin-top: 15px;
                padding-top: 15px;
                background-color: #E9FBFC;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #3498db;
                font-size: 16px;
            }
            QLabel {
                padding: 5px;
            }
            QLabel#sectionTitle {
                font-size: 18px;
                font-weight: bold;
                color: #3498db;
                padding: 10px 0px;
            }
            QLabel#valueLabel {
                font-size: 16px;
                font-weight: bold;
                color: white;
                background-color: rgba(52, 152, 219, 0.7);
                border-radius: 5px;
                padding: 8px;
                margin: 2px;
            }
            QLabel#keyLabel {
                font-size: 14px;
                color: #bdc3c7;
                padding-left: 10px;
            }
            QFrame#separator {
                background-color: #E9FBFC;
                min-height: 2px;
                max-height: 2px;
                margin: 10px 0px;
            }
            QScrollArea {
                border: none;
            }
        """)

        # Create main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Create scroll area for scrolling when content is too long
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setStyleSheet("background-color: transparent;")

        # Widget containing all content
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(20)

        # === Title ===
        title_label = QLabel("THÔNG TIN PHÒNG THUÊ")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: white; margin-bottom: 10px; padding: 15px; background-color: #2c3e50; border-radius: 10px;")
        content_layout.addWidget(title_label)

        # === Basic information ===
        basic_info_group = self.create_info_section("Thông tin cơ bản", "#E9FBFC")
        basic_grid = QGridLayout()
        basic_grid.setColumnStretch(1, 1)
        basic_grid.setSpacing(10)
        basic_grid.setContentsMargins(15, 15, 15, 15)

        # Populate basic info
        self.add_info_pair(basic_grid, 0, "Số phòng:", "A201")
        self.add_info_pair(basic_grid, 1, "Loại phòng:", "Standard (20m²)")
        self.add_info_pair(basic_grid, 2, "Ngày bắt đầu thuê:", "01/09/2024")
        self.add_info_pair(basic_grid, 3, "Tiền phòng:", "2.500.000 VNĐ/tháng")
        self.add_info_pair(basic_grid, 4, "Tiền cọc:", "5.000.000 VNĐ")
        self.add_info_pair(basic_grid, 5, "Ngày đến hạn thanh toán:", "05/04/2025")

        basic_info_group.setLayout(basic_grid)
        content_layout.addWidget(basic_info_group)

        # === Utility information ===
        utility_info_group = self.create_info_section("Chi tiết điện nước tháng hiện tại", "#E9FBFC")
        utility_grid = QGridLayout()
        utility_grid.setColumnStretch(1, 1)
        utility_grid.setSpacing(10)
        utility_grid.setContentsMargins(15, 15, 15, 15)

        # Populate utility info
        self.add_info_pair(utility_grid, 0, "Chỉ số điện cũ:", "1205 kWh (01/03/2025)")
        self.add_info_pair(utility_grid, 1, "Chỉ số điện mới:", "1267 kWh (31/03/2025)")
        self.add_info_pair(utility_grid, 2, "Tiêu thụ điện:", "62 kWh")
        self.add_info_pair(utility_grid, 3, "Đơn giá điện:", "3.500 VNĐ/kWh")
        self.add_info_pair(utility_grid, 4, "Thành tiền điện:", "217.000 VNĐ", highlight=True)

        # Separator
        separator = QFrame()
        separator.setObjectName("separator")
        utility_grid.addWidget(separator, 5, 0, 1, 2)

        self.add_info_pair(utility_grid, 6, "Chỉ số nước cũ:", "120 m³ (01/03/2025)")
        self.add_info_pair(utility_grid, 7, "Chỉ số nước mới:", "127 m³ (31/03/2025)")
        self.add_info_pair(utility_grid, 8, "Tiêu thụ nước:", "7 m³")
        self.add_info_pair(utility_grid, 9, "Đơn giá nước:", "25.000 VNĐ/m³")
        self.add_info_pair(utility_grid, 10, "Thành tiền nước:", "175.000 VNĐ", highlight=True)

        utility_info_group.setLayout(utility_grid)
        content_layout.addWidget(utility_info_group)

        # === Other services ===
        service_info_group = self.create_info_section("Dịch vụ khác", "#E9FBFC")
        service_grid = QGridLayout()
        service_grid.setColumnStretch(1, 1)
        service_grid.setSpacing(10)
        service_grid.setContentsMargins(15, 15, 15, 15)

        # Populate service info
        self.add_info_pair(service_grid, 0, "Internet:", "150.000 VNĐ/tháng")
        self.add_info_pair(service_grid, 1, "Phí quản lý:", "100.000 VNĐ/tháng")
        #self.add_info_pair(service_grid, 2, "Dịch vụ dọn phòng:", "200.000 VNĐ/tháng (2 lần/tháng)")
        self.add_info_pair(service_grid, 3, "Phí gửi xe:", "50.000 VNĐ/tháng/xe")

        service_info_group.setLayout(service_grid)
        content_layout.addWidget(service_info_group)

        # === Total costs for this month ===
        total_group = self.create_info_section("Tổng chi phí tháng 03/2025", "#E9FBFC")
        total_grid = QGridLayout()
        total_grid.setColumnStretch(1, 1)
        total_grid.setSpacing(10)
        total_grid.setContentsMargins(15, 15, 15, 15)

        self.add_info_pair(total_grid, 0, "Tiền phòng:", "2.500.000 VNĐ")
        self.add_info_pair(total_grid, 1, "Tiền điện:", "217.000 VNĐ")
        self.add_info_pair(total_grid, 2, "Tiền nước:", "175.000 VNĐ")
        self.add_info_pair(total_grid, 3, "Internet:", "150.000 VNĐ")
        self.add_info_pair(total_grid, 4, "Phí quản lý:", "100.000 VNĐ")
        self.add_info_pair(total_grid, 5, "Dịch vụ khác:", "250.000 VNĐ")

        # Separator
        separator2 = QFrame()
        separator2.setObjectName("separator")
        total_grid.addWidget(separator2, 6, 0, 1, 2)

        # Total cost
        total_label = QLabel("TỔNG CỘNG:")
        total_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50;")
        total_grid.addWidget(total_label, 7, 0)

        total_value = QLabel("3.392.000 VNĐ")
        total_value.setStyleSheet(
            "font-size: 18px; font-weight: bold; color: #2c3e50; background-color: #f39c12; border-radius: 5px; padding: 10px;")
        total_grid.addWidget(total_value, 7, 1)

        total_group.setLayout(total_grid)
        content_layout.addWidget(total_group)

        # === Landlord information ===
        landlord_info_group = self.create_info_section("Thông tin chủ trọ", "#E9FBFC")
        landlord_grid = QGridLayout()
        landlord_grid.setColumnStretch(1, 1)
        landlord_grid.setSpacing(10)
        landlord_grid.setContentsMargins(15, 15, 15, 15)

        self.add_info_pair(landlord_grid, 0, "Tên chủ trọ:", "Nguyễn Văn A")
        self.add_info_pair(landlord_grid, 1, "Số điện thoại:", "0901234567")
        self.add_info_pair(landlord_grid, 2, "Email:", "nguyenvana@gmail.com")
        self.add_info_pair(landlord_grid, 3, "Địa chỉ:", "123 Nguyễn Trãi, Quận 1, TP. HCM")

        landlord_info_group.setLayout(landlord_grid)
        content_layout.addWidget(landlord_info_group)

        # Terms and regulations
        rules_group = self.create_info_section("Quy định và lưu ý", "#fab1a0")
        rules_layout = QVBoxLayout()
        rules_layout.setContentsMargins(15, 15, 15, 15)

        rules_text = QLabel(
            "• Thanh toán tiền phòng trước ngày 10 hàng tháng\n"
            "• Giờ giới nghiêm: 23:00 - 05:00\n"
            "• Không gây ồn sau 22:00\n"
            "• Báo trước 30 ngày nếu muốn chấm dứt hợp đồng\n"
            "• Khách ở lại qua đêm cần đăng ký với quản lý\n"
            "• Không được tự ý sửa chữa, cải tạo phòng\n"
            "• Giữ gìn vệ sinh chung khu vực xung quanh"
        )
        rules_text.setWordWrap(True)
        rules_text.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 12px; font-size: 14px;")
        rules_layout.addWidget(rules_text)

        rules_group.setLayout(rules_layout)
        content_layout.addWidget(rules_group)

        # Complete the scroll area
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

    def create_info_section(self, title, background_color):
        """
        Create a styled GroupBox with specified background color
        """
        group_box = QGroupBox(title)
        group_box.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 10px;
                margin-top: 15px;
                padding-top: 15px;
                background-color: {background_color};
                color: #2c3e50;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px;
                color: #2c3e50;
                font-size: 16px;
                background-color: white;
                border-radius: 5px;
            }}
        """)
        return group_box

    def add_info_pair(self, grid, row, key, value, highlight=False):
        """
        Helper function to add key-value pairs to grid layouts
        with optional highlighting for important values
        """
        key_label = QLabel(key)
        key_label.setObjectName("keyLabel")
        key_label.setStyleSheet("color: #2c3e50; font-weight: bold;")
        grid.addWidget(key_label, row, 0, Qt.AlignLeft)

        value_label = QLabel(value)
        value_label.setObjectName("valueLabel")

        # Highlight important values if needed
        if highlight:
            value_label.setStyleSheet(
                "font-size: 16px; font-weight: bold; color: white; background-color: #e74c3c; border-radius: 5px; padding: 8px; margin: 2px;")
        else:
            value_label.setStyleSheet(
                "font-size: 16px; font-weight: bold; color: white; background-color: rgba(44, 62, 80, 0.6); border-radius: 5px; padding: 8px; margin: 2px;")

        grid.addWidget(value_label, row, 1, Qt.AlignLeft)