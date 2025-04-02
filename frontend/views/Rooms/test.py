from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QGroupBox, QScrollArea, QFrame, QPushButton, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

'''
class RoomsInfor(QWidget):
    def __init__(self, main_window, room_id):
        super().__init__()
        self.main_window = main_window
        self.room_id = room_id
        self.room_data = None  # Will be populated when data is loaded

        # Set up styling
        self.setup_styling()

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
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(20)

        # === Title ===
        title_label = QLabel(f"THÔNG TIN CHI TIẾT PHÒNG {self.room_id}")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: white; margin-bottom: 10px; "
            "padding: 15px; background-color: #2c3e50; border-radius: 10px;"
        )
        self.content_layout.addWidget(title_label)

        # Initially display a message when no data is available
        self.no_data_label = QLabel("Chưa có thông tin phòng. Vui lòng cập nhật.")
        self.no_data_label.setAlignment(Qt.AlignCenter)
        self.no_data_label.setStyleSheet(
            "font-size: 18px; color: #7f8c8d; padding: 50px; "
            "background-color: rgba(236, 240, 241, 0.8); border-radius: 10px;"
        )
        self.content_layout.addWidget(self.no_data_label)

        # Update button
        update_button = QPushButton("Cập nhật thông tin")
        update_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #3498db;"
            "   color: white;"
            "   font-size: 16px;"
            "   font-weight: bold;"
            "   padding: 12px 20px;"
            "   border-radius: 8px;"
            "   border: none;"
            "}"
            "QPushButton:hover {"
            "   background-color: #2980b9;"
            "}"
            "QPushButton:pressed {"
            "   background-color: #1f618d;"
            "}"
        )
        update_button.clicked.connect(self.update_room_info)

        # Add the scroll area and update button to the main layout
        scroll_area.setWidget(self.content_widget)
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(update_button, alignment=Qt.AlignCenter)

        # Placeholder for room content sections
        self.basic_info_group = None
        self.features_group = None
        self.price_group = None
        self.contact_group = None
        self.image_label = None

        # Load initial data (if available)
        self.load_room_data()

    def setup_styling(self):
        """Set up the widget styling"""
        self.setStyleSheet("""
            QWidget {
                background-color: #E9FBFC;
                color: #2c3e50;
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
                background-color: white;
                border-radius: 5px;
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
                background-color: rgba(44, 62, 80, 0.6);
                border-radius: 5px;
                padding: 8px;
                margin: 2px;
            }
            QLabel#keyLabel {
                font-size: 14px;
                color: #2c3e50;
                font-weight: bold;
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

    def load_room_data(self):
        """Load room data if available, otherwise keep the placeholder message"""
        # Here you would typically fetch data from a database or file
        # For now, we'll use the sample data if available, otherwise keep placeholder

        # Example of loading data (in real use, this would come from database)
        # Uncomment to test with sample data
        # self.room_data = sample_room_data
        # self.display_room_info()
        pass

    def update_room_info(self):
        """Handle update button click - for demo purposes, just load sample data"""
        # In a real application, this would open a form to update room information
        # For this example, we'll just use the sample data
        self.room_data = {
            "id": "P101",
            "address": "123 Đường ABC, Phường XYZ, Quận Bình Thạnh, TP. Hồ Chí Minh",
            "type": "Phòng trọ trong dãy trọ",
            "status": "Còn trống",
            "area": 25.5,  # m²
            "floor": 1,  # Tầng 1 (trệt)
            "has_mezzanine": True,  # Có gác lửng
            "bathroom": "Riêng trong phòng",
            "kitchen": "Khu bếp riêng",
            "balcony": True,
            "basic_furniture": ["Giường", "Tủ quần áo", "Bàn học"],
            "appliances": ["Điều hòa", "Máy nước nóng"],
            "amenities": ["Wifi tốc độ cao", "Chỗ để xe miễn phí (1 xe)", "Camera an ninh", "Giờ giấc tự do"],
            "rent_price": 3500000,  # VNĐ
            "deposit": 3500000,  # VNĐ
            "electricity_price": 3800,  # VNĐ/kWh
            "water_price": 100000,  # VNĐ/người/tháng
            "internet_price": 100000,  # VNĐ/phòng/tháng
            "other_fees": ["Phí vệ sinh: 20,000 VNĐ/tháng"],
            "max_occupancy": 2,
            "pets_allowed": False,
            "contact_name": "Cô Ba Chủ Trọ",
            "contact_phone": "090x xxx xxx",
            "available_date": "2025-04-05",
            "image_path": "placeholder_room.png"  # Đường dẫn tới ảnh phòng trọ (thay bằng ảnh thật)
        }

        self.display_room_info()

    def display_room_info(self):
        """Display room information when data is available"""
        if not self.room_data:
            return

        # Hide the placeholder message
        self.no_data_label.setVisible(False)

        # Clear any existing content (except title)
        for i in reversed(range(1, self.content_layout.count())):
            widget = self.content_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # === Room Image ===
        if self.room_data.get("image_path"):
            image_group = self.create_info_section("Hình ảnh phòng", "#E9FBFC")
            image_layout = QVBoxLayout()

            self.image_label = QLabel()
            pixmap = QPixmap(self.room_data["image_path"])
            if not pixmap.isNull():
                pixmap = pixmap.scaled(600, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.image_label.setPixmap(pixmap)
                self.image_label.setAlignment(Qt.AlignCenter)
            else:
                self.image_label.setText("Không thể tải hình ảnh")
                self.image_label.setAlignment(Qt.AlignCenter)
                self.image_label.setStyleSheet("color: #e74c3c; font-size: 16px;")

            image_layout.addWidget(self.image_label)
            image_group.setLayout(image_layout)
            self.content_layout.addWidget(image_group)

        # === Basic Information ===
        self.basic_info_group = self.create_info_section("Thông tin cơ bản", "#E9FBFC")
        basic_grid = QGridLayout()
        basic_grid.setColumnStretch(1, 1)
        basic_grid.setSpacing(10)
        basic_grid.setContentsMargins(15, 15, 15, 15)

        # Add basic info fields
        row = 0
        self.add_info_pair(basic_grid, row, "Mã phòng:", self.room_data["id"]);
        row += 1
        self.add_info_pair(basic_grid, row, "Địa chỉ:", self.room_data["address"]);
        row += 1
        self.add_info_pair(basic_grid, row, "Loại phòng:", self.room_data["type"]);
        row += 1
        self.add_info_pair(basic_grid, row, "Trạng thái:", self.room_data["status"]);
        row += 1
        self.add_info_pair(basic_grid, row, "Diện tích:", f"{self.room_data['area']} m²");
        row += 1
        self.add_info_pair(basic_grid, row, "Vị trí tầng:", f"Tầng {self.room_data['floor']}");
        row += 1
        self.add_info_pair(basic_grid, row, "Gác lửng:", "Có" if self.room_data["has_mezzanine"] else "Không");
        row += 1
        self.add_info_pair(basic_grid, row, "Ngày có thể thuê:", self.room_data["available_date"]);
        row += 1

        self.basic_info_group.setLayout(basic_grid)
        self.content_layout.addWidget(self.basic_info_group)

        # === Features and Amenities ===
        self.features_group = self.create_info_section("Tiện nghi và nội thất", "#E9FBFC")
        features_grid = QGridLayout()
        features_grid.setColumnStretch(1, 1)
        features_grid.setSpacing(10)
        features_grid.setContentsMargins(15, 15, 15, 15)

        row = 0
        self.add_info_pair(features_grid, row, "Phòng tắm:", self.room_data["bathroom"]);
        row += 1
        self.add_info_pair(features_grid, row, "Nhà bếp:", self.room_data["kitchen"]);
        row += 1
        self.add_info_pair(features_grid, row, "Ban công:", "Có" if self.room_data["balcony"] else "Không");
        row += 1

        # Add furniture list
        if self.room_data["basic_furniture"]:
            furniture_text = ", ".join(self.room_data["basic_furniture"])
            self.add_info_pair(features_grid, row, "Nội thất cơ bản:", furniture_text);
            row += 1

        # Add appliances list
        if self.room_data["appliances"]:
            appliances_text = ", ".join(self.room_data["appliances"])
            self.add_info_pair(features_grid, row, "Thiết bị điện:", appliances_text);
            row += 1

        # Add amenities list
        if self.room_data["amenities"]:
            amenities_text = ", ".join(self.room_data["amenities"])
            self.add_info_pair(features_grid, row, "Tiện ích:", amenities_text);
            row += 1

        self.add_info_pair(features_grid, row, "Số người ở tối đa:", str(self.room_data["max_occupancy"]));
        row += 1
        self.add_info_pair(features_grid, row, "Cho phép thú cưng:",
                           "Có" if self.room_data["pets_allowed"] else "Không");
        row += 1

        self.features_group.setLayout(features_grid)
        self.content_layout.addWidget(self.features_group)

        # === Price and Fees ===
        self.price_group = self.create_info_section("Giá thuê và phí dịch vụ", "#E9FBFC")
        price_grid = QGridLayout()
        price_grid.setColumnStretch(1, 1)
        price_grid.setSpacing(10)
        price_grid.setContentsMargins(15, 15, 15, 15)

        row = 0
        self.add_info_pair(price_grid, row, "Giá thuê:", f"{self.format_price(self.room_data['rent_price'])} VNĐ/tháng",
                           highlight=True);
        row += 1
        self.add_info_pair(price_grid, row, "Tiền đặt cọc:", f"{self.format_price(self.room_data['deposit'])} VNĐ");
        row += 1
        self.add_info_pair(price_grid, row, "Giá điện:",
                           f"{self.format_price(self.room_data['electricity_price'])} VNĐ/kWh");
        row += 1
        self.add_info_pair(price_grid, row, "Giá nước:",
                           f"{self.format_price(self.room_data['water_price'])} VNĐ/người/tháng");
        row += 1
        self.add_info_pair(price_grid, row, "Phí internet:",
                           f"{self.format_price(self.room_data['internet_price'])} VNĐ/tháng");
        row += 1

        # Add other fees
        if self.room_data["other_fees"]:
            fees_text = ", ".join(self.room_data["other_fees"])
            self.add_info_pair(price_grid, row, "Phí khác:", fees_text);
            row += 1

        self.price_group.setLayout(price_grid)
        self.content_layout.addWidget(self.price_group)

        # === Contact Information ===
        self.contact_group = self.create_info_section("Thông tin liên hệ", "#E9FBFC")
        contact_grid = QGridLayout()
        contact_grid.setColumnStretch(1, 1)
        contact_grid.setSpacing(10)
        contact_grid.setContentsMargins(15, 15, 15, 15)

        row = 0
        self.add_info_pair(contact_grid, row, "Tên chủ trọ:", self.room_data["contact_name"]);
        row += 1
        self.add_info_pair(contact_grid, row, "Số điện thoại:", self.room_data["contact_phone"]);
        row += 1

        self.contact_group.setLayout(contact_grid)
        self.content_layout.addWidget(self.contact_group)

        # Add update button at the end
        update_button = QPushButton("Lưu thông tin")
        update_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #3498db;"
            "   color: white;"
            "   font-size: 16px;"
            "   font-weight: bold;"
            "   padding: 12px 20px;"
            "   border-radius: 8px;"
            "   border: none;"
            "}"
            "QPushButton:hover {"
            "   background-color: #2980b9;"
            "}"
            "QPushButton:pressed {"
            "   background-color: #1f618d;"
            "}"
        )
        update_button.clicked.connect(self.update_room_info)
        self.content_layout.addWidget(update_button, alignment=Qt.AlignCenter)

    def create_info_section(self, title, background_color):
        """Create a styled GroupBox with specified background color"""
        group_box = QGroupBox(title)
        group_box.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                border: 1px solid rgba(52, 152, 219, 0.5);
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
                background-color: while;
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
        grid.addWidget(key_label, row, 0, Qt.AlignLeft)

        value_label = QLabel(value)
        value_label.setObjectName("valueLabel")
        value_label.setWordWrap(True)

        # Highlight important values if needed
        if highlight:
            value_label.setStyleSheet(
                "font-size: 16px; font-weight: bold; color: white; "
                "background-color: #e74c3c; border-radius: 5px; padding: 8px; margin: 2px;"
            )

        grid.addWidget(value_label, row, 1, Qt.AlignLeft)

    def format_price(self, price):
        """Format price with thousands separator"""
        return "{:,}".format(price).replace(",", ".")

'''