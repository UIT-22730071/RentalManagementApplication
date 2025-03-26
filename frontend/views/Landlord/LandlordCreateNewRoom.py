from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QComboBox, QPushButton,
    QVBoxLayout, QHBoxLayout, QFormLayout
)
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Component.InputTextUI import InputTextUI
from QLNHATRO.RentalManagementApplication.frontend.Component.LabelUI import LabelUI, LabelDarkUI


class CreateNewRoom(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.setStyleSheet("background-color: #d4a9a9; padding: 24px;")
        main_layout = QVBoxLayout(self)

        # NỀN TRẮNG CHỨA NỘI DUNG
        content = QWidget()
        content.setStyleSheet("background-color: white; border-radius: 16px; padding: 32px;")
        content_layout = QVBoxLayout(content)

        # TIÊU ĐỀ
        title = QLabel("🏠 Tạo phòng trọ mới")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        content_layout.addWidget(title)
        content_layout.addSpacing(20)

        # Thêm tiêu đề

        desc = QLabel("** Vui lòng điền đầy đủ thông tin để thêm phòng mới vào hệ thống.")
        desc.setStyleSheet("color: #666; font-size: 13px;")
        desc.setAlignment(Qt.AlignLeft)
        content_layout.addWidget(desc)

        # TẠO 2 FORM CỘT TRÁI & PHẢI
        form_row = QHBoxLayout()
        form_left = QFormLayout()
        form_right = QFormLayout()

        # Đặt style cho combo & input đồng bộ
        def style_input(widget):
            widget.setFixedHeight(34)
            widget.setFixedWidth(240)
            widget.setStyleSheet("""
                background-color: white;
                color: black;
                border: 1.5px solid #ccc;
                border-radius: 8px;
                padding: 4px 8px;
            """)
            return widget

        def create_input_with_unit(unit_text=None):
            layout = QHBoxLayout()
            input = style_input(QLineEdit())
            layout.addWidget(input)

            if unit_text:
                unit = QLabel(unit_text)
                unit.setFixedWidth(80)
                unit.setAlignment(Qt.AlignCenter)
                unit.setStyleSheet("""
                    background-color: #CCD2F4;
                    color: #333;
                    padding: 6px 8px;
                    font-size: 11px;
                    border-radius: 10px;
                """)
                layout.addWidget(unit)
            return input, layout

        # Input Widgets
        self.input_name_room = style_input(QLineEdit())
        self.input_code_room = style_input(QLineEdit())
        self.input_address_room = style_input(QLineEdit())

        self.input_type_room = QComboBox()
        self.input_type_room.addItems(["Phòng trọ", "Chung cư", "Nhà nguyên căn"])
        style_input(self.input_type_room)

        self.input_status_room = QComboBox()
        self.input_status_room.addItems(["Trống", "Đã thuê"])
        style_input(self.input_status_room)

        self.input_infor_more = style_input(QLineEdit())
        self.input_area, area_layout = create_input_with_unit("m²")
        self.input_price_room, price_room_layout = create_input_with_unit("VNĐ")
        self.input_price_electric, price_electric_layout = create_input_with_unit("VNĐ/kWh")
        self.input_price_water, price_water_layout = create_input_with_unit("VNĐ/m³")
        self.input_number_electric, number_electric_layout = create_input_with_unit("kWh")
        self.input_number_water, number_water_layout = create_input_with_unit("m³")

        # THÊM VÀO CỘT TRÁI
        form_left.addRow(LabelDarkUI("Tên phòng:"), self.input_name_room)
        form_left.addRow(LabelDarkUI("Mã phòng:"), self.input_code_room)
        form_left.addRow(LabelDarkUI("Địa chỉ:"), self.input_address_room)
        form_left.addRow(LabelDarkUI("Loại phòng:"), self.input_type_room)
        form_left.addRow(LabelDarkUI("Trạng thái:"), self.input_status_room)
        form_left.addRow(LabelDarkUI("Thông tin khác:"), self.input_infor_more)

        # THÊM VÀO CỘT PHẢI
        form_right.addRow(LabelDarkUI("Diện tích:"), area_layout)
        form_right.addRow(LabelDarkUI("Giá thuê:"), price_room_layout)
        form_right.addRow(LabelDarkUI("Giá điện:"), price_electric_layout)
        form_right.addRow(LabelDarkUI("Giá nước:"), price_water_layout)
        form_right.addRow(LabelDarkUI("Số điện:"), number_electric_layout)
        form_right.addRow(LabelDarkUI("Số nước:"), number_water_layout)

        # GỘP 2 FORM VÀO FORM ROW
        form_row.addLayout(form_left)
        form_row.addSpacing(50)
        form_row.addLayout(form_right)
        content_layout.addLayout(form_row)

        # BUTTON TẠO PHÒNG
        btn_create = QPushButton("Tạo phòng")

        btn_create.setFixedWidth(180)
        btn_create.setStyleSheet("""
            background-color: #233FF3;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s ;
        """)

        btn_create.clicked.connect(lambda : print("Clicked create room button"))
        content_layout.addSpacing(20)
        content_layout.addWidget(btn_create, alignment=Qt.AlignCenter)

        # Thêm nội dung vào main
        main_layout.addWidget(content)
