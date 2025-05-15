from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QComboBox, QPushButton,
    QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
)
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.controller.RoomController.RoomMenuController import RoomMenuController
from QLNHATRO.RentalManagementApplication.frontend.Component.LabelUI import LabelDarkUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.services.RoomService import RoomService


class CreateNewRoom(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.create_data_for_update ={}
        self.id_lanlord = None

        main_layout = QVBoxLayout(self)

        # NỀN TRẮNG CHỨA NỘI DUNG
        content = QWidget()
        #content.setStyleSheet("background-color: white; border-radius: 16px; padding: 32px;")
        content_layout = QVBoxLayout(content)

        # TIÊU ĐỀ
        title = QLabel("🏠 Tạo phòng trọ mới")
        title.setAlignment(Qt.AlignCenter)
        #title.setStyleSheet("font-size: 24px; font-weight: bold;")
        title.setObjectName("Title")  # ✅ sẽ dùng style của QLabel#Title
        title.setFixedHeight(60)
        content_layout.addWidget(title)
        content_layout.addSpacing(20)

        # Thêm tiêu đề

        desc = QLabel("** Vui lòng điền đầy đủ thông tin để thêm phòng mới vào hệ thống.")
        #desc.setStyleSheet("color: #666; font-size: 13px;")
        desc.setAlignment(Qt.AlignLeft)
        content_layout.addWidget(desc)

        # TẠO 2 FORM CỘT TRÁI & PHẢI
        form_row = QHBoxLayout()
        form_left = QFormLayout()
        form_right = QFormLayout()

        # Đặt style cho combo & input đồng bộ
        def style_input(widget):
            widget.setFixedHeight(36)
            widget.setFixedWidth(240)
            return widget

        def create_input_with_unit(unit_text=None):
            layout = QHBoxLayout()
            input = style_input(QLineEdit())
            layout.addWidget(input)

            if unit_text:
                unit = QLabel(unit_text)
                unit.setFixedWidth(80)
                unit.setAlignment(Qt.AlignLeft)
                layout.addWidget(unit)
            return input, layout

        # Input Widgets
        self.input_name_room = style_input(QLineEdit())
        self.input_number_people_room = style_input(QLineEdit())
        self.input_address_room = style_input(QLineEdit())

        self.input_type_room = QComboBox()
        self.input_type_room.addItems(["Phòng trọ", "Chung cư", "Nhà nguyên căn","Khác"])
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
        form_left.addRow(LabelDarkUI("Số nguoif tối đa:"), self.input_number_people_room)
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



        btn_create.clicked.connect(self.handle_create_room)
        content_layout.addSpacing(20)
        content_layout.addWidget(btn_create, alignment=Qt.AlignCenter)

        # Thêm nội dung vào main
        main_layout.addWidget(content)

    def handle_create_room(self):
        create_data = RoomService.collect_data_create_room(
                id_landlord=self.id_lanlord,
                room_name=self.input_name_room.text(),
                number_people=self.input_number_people_room.text(),
                address=self.input_address_room.text(),
                type_room=self.input_type_room.currentText(),
                status=self.input_status_room.currentText(),
                other_infor=self.input_infor_more.text(),
                area=self.input_area.text(),
                price_rent=self.input_price_room.text(),
                electric_price=self.input_price_electric.text(),
                water_price=self.input_price_water.text(),
                num_electric=self.input_number_electric.text(),
                num_water=self.input_number_water.text(),
            )

        print("[DEBUG] Dữ liệu tạo phòng:", create_data)
        RoomMenuController.go_to_handel_data_for_create_room(self.id_lanlord, create_data)
        # Xuất hộp thoại thông báo
        QMessageBox.information(
            self,
            "Tạo phòng thành công",
            "Phòng trọ đã được thêm vào hệ thống thành công!",
            QMessageBox.StandardButton.Ok
        )