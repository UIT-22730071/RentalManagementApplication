from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QGroupBox, QScrollArea, \
    QFrame
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class TenantRoomInfo(QWidget):
    def __init__(self, main_window,data_room, id_tenant):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())

        self.main_window = main_window
        self.data_room = data_room or {}
        self.id_tenant = id_tenant

        # Improved styling with backgrounds for all information areas

        # Create main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Create scroll area for scrolling when content is too long
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        #scroll_area.setStyleSheet("background-color: transparent;")

        # Widget containing all content
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(20)

        # === Title ===
        title_label = QLabel("THÔNG TIN PHÒNG THUÊ")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("Title")
        title_label.setFixedHeight(60)
        content_layout.addWidget(title_label)

        # === Basic information ===
        basic_info_group = self.create_info_section("Thông tin cơ bản", "#E9FBFC")
        basic_grid = QGridLayout()
        basic_grid.setColumnStretch(1, 1)
        basic_grid.setSpacing(10)
        basic_grid.setContentsMargins(15, 15, 15, 15)

        # Populate basic info
        self.add_info_pair(basic_grid, 0, "Số phòng:", self.data_room.get("Số phòng", "---"))
        self.add_info_pair(basic_grid, 1, "Loại phòng:", self.data_room.get("Loại phòng", "---"))
        self.add_info_pair(basic_grid, 2, "Ngày bắt đầu thuê:", self.data_room.get("Ngày bắt đầu thuê", "---"))
        self.add_info_pair(basic_grid, 3, "Tiền phòng:", self.data_room.get("Tiền phòng", "---"))
        self.add_info_pair(basic_grid, 4, "Tiền cọc:", self.data_room.get("Tiền cọc", "---"))
        self.add_info_pair(basic_grid, 5, "Ngày đến hạn thanh toán:",
                           self.data_room.get("Ngày đến hạn thanh toán", "---"))
        self.add_info_pair(basic_grid, 6, "Diện tích:", self.data_room.get("Diện tích", "---"),)
        basic_info_group.setLayout(basic_grid)
        content_layout.addWidget(basic_info_group)

        # === Utility information ===
        utility_info_group = self.create_info_section("Chi tiết điện nước tháng hiện tại", "#E9FBFC")
        utility_grid = QGridLayout()
        utility_grid.setColumnStretch(1, 1)
        utility_grid.setSpacing(10)
        utility_grid.setContentsMargins(15, 15, 15, 15)

        # Populate utility info
        self.add_info_pair(utility_grid, 0, "Chỉ số điện cũ:", self.data_room.get("Chỉ số điện cũ", "---"))
        self.add_info_pair(utility_grid, 1, "Chỉ số điện mới:", self.data_room.get("Chỉ số điện mới", "---"))
        self.add_info_pair(utility_grid, 2, "Tiêu thụ điện:", self.data_room.get("Tiêu thụ điện", "---"))
        self.add_info_pair(utility_grid, 3, "Đơn giá điện:", self.data_room.get("Đơn giá điện", "---"))
        self.add_info_pair(utility_grid, 4, "Thành tiên điện:", self.data_room.get("Thành tiên điện", "---"),
                           highlight=True)

        # Separator
        separator = QFrame()
        separator.setObjectName("separator")
        utility_grid.addWidget(separator, 5, 0, 1, 2)

        self.add_info_pair(utility_grid, 6, "Chỉ số nước cũ:", self.data_room.get("Chỉ số nước cũ:", "---"))
        self.add_info_pair(utility_grid, 7, "Chỉ số nước mới:", self.data_room.get("Chỉ số nước mới", "---"))
        self.add_info_pair(utility_grid, 8, "Tiêu thụ nước:", self.data_room.get("Tiêu thụ nước", "---"))
        self.add_info_pair(utility_grid, 9, "Đơn giá nước:", self.data_room.get("Đơn giá nước", "---"))
        self.add_info_pair(utility_grid, 10, "Thành tiên nước:", self.data_room.get("Thành tiên nước", "---"),
                           highlight=True)

        utility_info_group.setLayout(utility_grid)
        content_layout.addWidget(utility_info_group)

        # === Other services ===
        service_info_group = self.create_info_section("Dịch vụ khác", "#E9FBFC")
        service_grid = QGridLayout()
        service_grid.setColumnStretch(1, 1)
        service_grid.setSpacing(10)
        service_grid.setContentsMargins(15, 15, 15, 15)

        # Populate service info
        self.add_info_pair(service_grid, 0, "Chi phí khác:", self.data_room.get("Chi phí khác", "---"))
        #self.add_info_pair(service_grid, 1, "Phí quản lý:", "100.000 VNĐ/tháng")
        #self.add_info_pair(service_grid, 2, "Dịch vụ dọn phòng:", "200.000 VNĐ/tháng (2 lần/tháng)")
        #self.add_info_pair(service_grid, 3, "Phí gửi xe:", "50.000 VNĐ/tháng/xe")

        service_info_group.setLayout(service_grid)
        content_layout.addWidget(service_info_group)

        # === Total costs for this month ===
        total_group = self.create_info_section("Tổng chi phí tháng 03/2025", "#E9FBFC")
        total_grid = QGridLayout()
        total_grid.setColumnStretch(1, 1)
        total_grid.setSpacing(10)
        total_grid.setContentsMargins(15, 15, 15, 15)

        self.add_info_pair(total_grid, 0, "Tiền phòng:", self.data_room.get("Tiền phòng", "---"))
        self.add_info_pair(total_grid, 1, "Tiền điện:", self.data_room.get("Thành tiên điện", "---"))
        self.add_info_pair(total_grid, 2, "Tiền nước:", self.data_room.get("Thành tiên nước", "---"))
        self.add_info_pair(total_grid, 3, "Internet:", self.data_room.get("Internet", "---"))
        self.add_info_pair(total_grid, 4, "Tiền rác:", self.data_room.get("Tiền rác", "---"))
        self.add_info_pair(total_grid, 5, "Dịch vụ khác:", self.data_room.get("Chi phí khác", "---"))



        # Separator
        separator2 = QFrame()
        separator2.setObjectName("separator")
        total_grid.addWidget(separator2, 6, 0, 1, 2)

        # Total cost
        total_label = QLabel("TỔNG CỘNG:")
        total_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50;")
        total_grid.addWidget(total_label, 7, 0)

        total_value = QLabel()
        total_value.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50; background-color: #f39c12; border-radius: 5px; padding: 10px;")
        total_value.setText(self.data_room.get("Tổng cộng", "---"))
        total_grid.addWidget(total_value, 7, 1)

        total_group.setLayout(total_grid)
        content_layout.addWidget(total_group)

        # === Landlord information ===
        landlord_info_group = self.create_info_section("Thông tin chủ trọ", "#E9FBFC")
        landlord_grid = QGridLayout()
        landlord_grid.setColumnStretch(1, 1)
        landlord_grid.setSpacing(10)
        landlord_grid.setContentsMargins(15, 15, 15, 15)

        self.add_info_pair(landlord_grid, 0, "Tên chủ trọ:", self.data_room.get("Tên chủ trọ", "---"))
        self.add_info_pair(landlord_grid, 1, "Số điện thoại:", self.data_room.get("Số điện thoại", "---"))
        self.add_info_pair(landlord_grid, 2, "Email:", self.data_room.get("Email", "---"))
        self.add_info_pair(landlord_grid, 3, "Địa chỉ:", self.data_room.get("Địa chỉ", "---"))

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
        rules_text.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 12px; font-size: 14px;")
        rules_layout.addWidget(rules_text)

        rules_group.setLayout(rules_layout)
        content_layout.addWidget(rules_group)

        # Complete the scroll area
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

    def create_info_section(self, title, background_color):
        group_box = QGroupBox(title)
        group_box.setProperty("theme", "blue")
        return group_box

    def add_info_pair(self, grid, row, key, value, highlight=False):
        """
        Helper function to add key-value pairs to grid layouts
        with optional highlighting for important values
        """
        key_label = QLabel(key)
        key_label.setObjectName("keyLabel")

        #key_label.setStyleSheet("color: #2c3e50; font-weight: bold;")
        grid.addWidget(key_label, row, 0, Qt.AlignLeft)

        value_label = QLabel(value)
        value_label.setObjectName("valueLabel")

        # Highlight important values if needed
        if highlight:
            value_label.setProperty("highlight", True)
        grid.addWidget(value_label, row, 1, Qt.AlignLeft)