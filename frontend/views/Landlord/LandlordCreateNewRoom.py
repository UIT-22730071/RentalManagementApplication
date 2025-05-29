from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QGroupBox,
    QVBoxLayout, QHBoxLayout, QMessageBox,
    QCheckBox, QGridLayout, QScrollArea, QFrame
)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator

from QLNHATRO.RentalManagementApplication.controller.RoomController.RoomMenuController import RoomMenuController
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.services.RoomService import RoomService


class CreateNewRoom(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.create_data_for_update = {}
        self.id_landlord = None
        self.main_window = main_window

        # Thiết lập khu vực cuộn cho trường hợp form dài
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(20, 20, 20, 20)
        scroll_layout.setSpacing(15)

        # NỀN TRẮNG CHỨA NỘI DUNG
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # TIÊU ĐỀ
        header_widget = QWidget()
        header_layout = QVBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)

        title = QLabel("🏠 Tạo phòng trọ mới")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("Title")
        title.setFixedHeight(60)
        header_layout.addWidget(title)

        # Thông tin hướng dẫn
        desc_box = QGroupBox("Hướng dẫn")
        desc_box.setProperty("theme", "blue")
        desc_layout = QVBoxLayout(desc_box)

        desc = QLabel("• Vui lòng điền đầy đủ thông tin để thêm phòng mới vào hệ thống.")
        desc.setObjectName("sectionLabel")
        desc.setAlignment(Qt.AlignLeft)

        desc_1 = QLabel("• Các trường đánh dấu (*) là bắt buộc phải nhập.")
        desc_1.setObjectName("infoLabel")
        desc_1.setAlignment(Qt.AlignLeft)

        desc_2 = QLabel("• Đảm bảo nhập đúng định dạng số cho các trường giá tiền và diện tích.")
        desc_2.setObjectName("infoLabel")
        desc_2.setAlignment(Qt.AlignLeft)

        desc_layout.addWidget(desc)
        desc_layout.addWidget(desc_1)
        desc_layout.addWidget(desc_2)

        scroll_layout.addWidget(header_widget)
        scroll_layout.addWidget(desc_box)

        # THÔNG TIN CƠ BẢN VỀ PHÒNG
        basic_info_box = QGroupBox("Thông tin cơ bản")
        basic_info_box.setProperty("theme", "blue")
        basic_info_layout = QGridLayout(basic_info_box)

        # Đặt style cho combo & input đồng bộ
        def style_input(widget):
            widget.setFixedHeight(36)
            widget.setStyleSheet("padding-left: 5px;")
            return widget

        def create_input_with_unit(unit_text=None, placeholder="", validator=None):
            container = QWidget()
            layout = QHBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)

            input = QLineEdit()
            input.setPlaceholderText(placeholder)
            style_input(input)

            if validator:
                input.setValidator(validator)

            layout.addWidget(input)

            if unit_text:
                unit = QLabel(unit_text)
                unit.setObjectName("keyLabel")
                unit.setFixedWidth(80)
                unit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                layout.addWidget(unit)

            return input, container

        # Validators
        number_validator = QRegExpValidator(QRegExp(r"[0-9]+"))
        decimal_validator = QRegExpValidator(QRegExp(r"[0-9]+(\.[0-9]+)?"))

        # Input Widgets
        room_name_label = QLabel("Tên phòng: *")
        room_name_label.setObjectName("keyLabel")
        self.input_name_room = style_input(QLineEdit())
        self.input_name_room.setPlaceholderText("Nhập tên phòng (vd: Phòng 101)")

        people_label = QLabel("Số người tối đa: *")
        people_label.setObjectName("keyLabel")
        self.input_number_people_room = style_input(QLineEdit())
        self.input_number_people_room.setPlaceholderText("Nhập số người tối đa")
        self.input_number_people_room.setValidator(number_validator)

        address_label = QLabel("Địa chỉ: *")
        address_label.setObjectName("keyLabel")
        self.input_address_room = style_input(QLineEdit())
        self.input_address_room.setPlaceholderText("Nhập địa chỉ chi tiết")

        type_label = QLabel("Loại phòng: *")
        type_label.setObjectName("keyLabel")
        self.input_type_room = QComboBox()
        self.input_type_room.addItems(
            ["Phòng trọ", "Chung cư mini", "Nhà nguyên căn", "Chung cư", "Nhà mặt phố", "Khác"])
        style_input(self.input_type_room)

        status_label = QLabel("Trạng thái:")
        status_label.setObjectName("keyLabel")
        self.input_status_room = QComboBox()
        self.input_status_room.addItems(["Trống", "Đã thuê", "Đang sửa chữa", "Đặt cọc"])
        style_input(self.input_status_room)

        # Thêm vào layout
        basic_info_layout.addWidget(room_name_label, 0, 0)
        basic_info_layout.addWidget(self.input_name_room, 0, 1)
        basic_info_layout.addWidget(type_label, 0, 2)
        basic_info_layout.addWidget(self.input_type_room, 0, 3)

        basic_info_layout.addWidget(people_label, 1, 0)
        basic_info_layout.addWidget(self.input_number_people_room, 1, 1)
        basic_info_layout.addWidget(status_label, 1, 2)
        basic_info_layout.addWidget(self.input_status_room, 1, 3)

        basic_info_layout.addWidget(address_label, 2, 0)
        self.input_address_room.setMinimumWidth(300)
        basic_info_layout.addWidget(self.input_address_room, 2, 1, 1, 3)

        scroll_layout.addWidget(basic_info_box)

        # THÔNG TIN GIÁ PHÒNG VÀ DIỆN TÍCH
        price_info_box = QGroupBox("Thông tin giá và diện tích")
        price_info_box.setProperty("theme", "blue")
        price_info_layout = QGridLayout(price_info_box)

        area_label = QLabel("Diện tích: *")
        area_label.setObjectName("keyLabel")
        self.input_area, area_container = create_input_with_unit("m²", "Nhập diện tích", decimal_validator)

        price_room_label = QLabel("Giá thuê: *")
        price_room_label.setObjectName("keyLabel")
        self.input_price_room, price_room_container = create_input_with_unit("VNĐ/tháng", "Nhập giá thuê",
                                                                             number_validator)

        price_electric_label = QLabel("Giá điện:")
        price_electric_label.setObjectName("keyLabel")
        self.input_price_electric, price_electric_container = create_input_with_unit("VNĐ/kWh", "Nhập giá điện",
                                                                                     number_validator)

        price_water_label = QLabel("Giá nước:")
        price_water_label.setObjectName("keyLabel")
        self.input_price_water, price_water_container = create_input_with_unit("VNĐ/m³", "Nhập giá nước",
                                                                               number_validator)

        # Thêm vào layout
        price_info_layout.addWidget(area_label, 0, 0)
        price_info_layout.addWidget(area_container, 0, 1)
        price_info_layout.addWidget(price_room_label, 0, 2)
        price_info_layout.addWidget(price_room_container, 0, 3)

        price_info_layout.addWidget(price_electric_label, 1, 0)
        price_info_layout.addWidget(price_electric_container, 1, 1)
        price_info_layout.addWidget(price_water_label, 1, 2)
        price_info_layout.addWidget(price_water_container, 1, 3)

        scroll_layout.addWidget(price_info_box)

        # CHỈ SỐ ĐỒNG HỒ
        meter_info_box = QGroupBox("Chỉ số đồng hồ ban đầu")
        meter_info_box.setProperty("theme", "blue")
        meter_info_layout = QGridLayout(meter_info_box)

        number_electric_label = QLabel("Số điện ban đầu:")
        number_electric_label.setObjectName("keyLabel")
        self.input_number_electric, number_electric_container = create_input_with_unit("kWh",
                                                                                       "Nhập chỉ số đồng hồ điện",
                                                                                       number_validator)

        number_water_label = QLabel("Số nước ban đầu:")
        number_water_label.setObjectName("keyLabel")
        self.input_number_water, number_water_container = create_input_with_unit("m³", "Nhập chỉ số đồng hồ nước",
                                                                                 number_validator)

        # Thêm vào layout
        meter_info_layout.addWidget(number_electric_label, 0, 0)
        meter_info_layout.addWidget(number_electric_container, 0, 1)
        meter_info_layout.addWidget(number_water_label, 0, 2)
        meter_info_layout.addWidget(number_water_container, 0, 3)

        scroll_layout.addWidget(meter_info_box)

        # THÔNG TIN TIỆN ÍCH
        amenities_box = QGroupBox("Tiện ích phòng")
        amenities_box.setProperty("theme", "blue")
        amenities_layout = QGridLayout(amenities_box)

        self.cb_wifi = QCheckBox("Wifi miễn phí")
        self.cb_parking = QCheckBox("Chỗ để xe")
        self.cb_aircon = QCheckBox("Máy lạnh/Điều hòa")
        self.cb_fridge = QCheckBox("Tủ lạnh")

        self.cb_wm = QCheckBox("Máy giặt")
        self.cb_security = QCheckBox("Bảo vệ 24/7")
        self.cb_tv = QCheckBox("TV")
        self.cb_kitchen = QCheckBox("Bếp")
        # ---
        self.cb_floor = QCheckBox("Tầng lầu")
        self.cb_hasLoft = QCheckBox("Gác lửng")
        self.cb_bathroom = QCheckBox("Phòng tắm")
        self.cb_balcony = QCheckBox("Ban công")

        self.cb_funiture = QCheckBox("Nội thất cơ bản")
        self.cb_pet = QCheckBox("Thú cưng")

        # Thêm vào layout
        amenities_layout.addWidget(self.cb_wifi, 0, 0)
        amenities_layout.addWidget(self.cb_parking, 0, 1)
        amenities_layout.addWidget(self.cb_aircon, 0, 2)
        amenities_layout.addWidget(self.cb_fridge, 0, 3)

        amenities_layout.addWidget(self.cb_wm, 1, 0)
        amenities_layout.addWidget(self.cb_security, 1, 1)
        amenities_layout.addWidget(self.cb_tv, 1, 2)
        amenities_layout.addWidget(self.cb_kitchen, 1, 3)

        amenities_layout.addWidget(self.cb_floor, 2, 0)
        amenities_layout.addWidget(self.cb_hasLoft, 2, 1)
        amenities_layout.addWidget(self.cb_bathroom, 2, 2)
        amenities_layout.addWidget(self.cb_balcony, 2, 3)

        amenities_layout.addWidget(self.cb_funiture, 3, 0)


        scroll_layout.addWidget(amenities_box)

        # THÔNG TIN KHÁC
        other_info_box = QGroupBox("Thông tin bổ sung")
        other_info_box.setProperty("theme", "blue")
        other_info_layout = QVBoxLayout(other_info_box)

        other_label = QLabel("Mô tả thêm:")
        other_label.setObjectName("keyLabel")
        self.input_infor_more = QLineEdit()
        self.input_infor_more.setPlaceholderText("Nhập các thông tin bổ sung khác về phòng")
        self.input_infor_more.setMinimumHeight(60)

        other_info_layout.addWidget(other_label)
        other_info_layout.addWidget(self.input_infor_more)

        scroll_layout.addWidget(other_info_box)

        # BUTTON ACTIONS
        button_layout = QHBoxLayout()

        self.btn_clear = QPushButton("Xóa dữ liệu")
        self.btn_clear.setObjectName("CancelBtn")
        self.btn_clear.setFixedWidth(150)
        self.btn_clear.setFixedHeight(40)
        self.btn_clear.clicked.connect(self.clear_form)

        self.btn_create = QPushButton("Tạo phòng")
        self.btn_create.setFixedWidth(150)
        self.btn_create.setFixedHeight(40)
        self.btn_create.clicked.connect(self.handle_create_room)

        button_layout.addWidget(self.btn_clear)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.btn_create)

        scroll_layout.addLayout(button_layout)
        scroll_layout.addStretch()

        # Thêm separator trước khu vực button để chia tách nội dung
        separator = QFrame()
        separator.setObjectName("separator")
        separator.setFrameShape(QFrame.HLine)
        scroll_layout.addWidget(separator)

        # Thiết lập cuộn
        scroll_area.setWidget(scroll_content)

        # Thêm nội dung vào main
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

    def clear_form(self):
        # Xóa tất cả dữ liệu trong form
        self.input_name_room.clear()
        self.input_number_people_room.clear()
        self.input_address_room.clear()
        self.input_type_room.setCurrentIndex(0)
        self.input_status_room.setCurrentIndex(0)
        self.input_infor_more.clear()
        self.input_area.clear()
        self.input_price_room.clear()
        self.input_price_electric.clear()
        self.input_price_water.clear()
        self.input_number_electric.clear()
        self.input_number_water.clear()

        # Xóa checkboxes
        self.cb_wifi.setChecked(False)
        self.cb_parking.setChecked(False)
        self.cb_aircon.setChecked(False)
        self.cb_fridge.setChecked(False)
        self.cb_wm.setChecked(False)
        self.cb_security.setChecked(False)
        self.cb_tv.setChecked(False)
        self.cb_kitchen.setChecked(False)

    def validate_form(self):
        # Kiểm tra các trường bắt buộc
        required_fields = [
            (self.input_name_room, "Tên phòng"),
            (self.input_number_people_room, "Số người tối đa"),
            (self.input_address_room, "Địa chỉ"),
            (self.input_area, "Diện tích"),
            (self.input_price_room, "Giá thuê")
        ]

        for field, name in required_fields:
            if not field.text().strip():
                QMessageBox.warning(self, "Thiếu thông tin", f"Vui lòng nhập {name}.")
                field.setFocus()
                return False

        # Kiểm tra định dạng số
        number_fields = [
            (self.input_number_people_room, "Số người tối đa"),
            (self.input_area, "Diện tích"),
            (self.input_price_room, "Giá thuê")
        ]

        for field, name in number_fields:
            try:
                if field.text().strip():
                    float(field.text().strip())
            except ValueError:
                QMessageBox.warning(self, "Định dạng không hợp lệ",
                                    f"{name} phải là số.")
                field.setFocus()
                return False

        return True

    def collect_amenities(self):
        amenities = []
        if self.cb_wifi.isChecked():
            amenities.append("Wifi miễn phí")
        if self.cb_parking.isChecked():
            amenities.append("Chỗ để xe")
        if self.cb_aircon.isChecked():
            amenities.append("Máy lạnh/Điều hòa")
        if self.cb_fridge.isChecked():
            amenities.append("Tủ lạnh")
        if self.cb_wm.isChecked():
            amenities.append("Máy giặt")
        if self.cb_security.isChecked():
            amenities.append("Bảo vệ 24/7")
        if self.cb_tv.isChecked():
            amenities.append("TV")
        if self.cb_kitchen.isChecked():
            amenities.append("Bếp")

        return ", ".join(amenities)

    def handle_create_room(self):
        if not self.validate_form():
            return

        # Thu thập thông tin tiện ích
        amenities = self.collect_amenities()

        # Kết hợp thông tin bổ sung với tiện ích
        other_info = self.input_infor_more.text().strip()
        if amenities and other_info:
            combined_info = f"Tiện ích: {amenities}. {other_info}"
        elif amenities:
            combined_info = f"Tiện ích: {amenities}"
        else:
            combined_info = other_info

        create_data = RoomService.collect_data_create_room(
            id_landlord=self.id_landlord,
            room_name=self.input_name_room.text().strip(),
            number_people=self.input_number_people_room.text().strip(),
            address=self.input_address_room.text().strip(),
            type_room=self.input_type_room.currentText(),
            status=self.input_status_room.currentText(),
            other_infor=combined_info,
            area=self.input_area.text().strip(),
            price_rent=self.input_price_room.text().strip(),
            electric_price=self.input_price_electric.text().strip() or "0",
            water_price=self.input_price_water.text().strip() or "0",
            num_electric=self.input_number_electric.text().strip() or "0",
            num_water=self.input_number_water.text().strip() or "0",
        )

        print("[DEBUG] Dữ liệu tạo phòng:", create_data)

        # Xác nhận tạo phòng
        confirm_box = QMessageBox()
        confirm_box.setIcon(QMessageBox.Question)
        confirm_box.setWindowTitle("Xác nhận tạo phòng")
        confirm_box.setText(f"Bạn có chắc chắn muốn tạo phòng {self.input_name_room.text()} không?")
        confirm_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_box.setDefaultButton(QMessageBox.No)

        if confirm_box.exec_() == QMessageBox.Yes:
            result = RoomMenuController.go_to_handel_data_for_create_room(self.id_landlord, create_data)

            if result:  # Giả sử hàm trả về True nếu thành công
                QMessageBox.information(
                    self,
                    "Tạo phòng thành công",
                    "Phòng trọ đã được thêm vào hệ thống thành công!",
                    QMessageBox.StandardButton.Ok
                )
                self.clear_form()
            else:
                QMessageBox.critical(
                    self,
                    "Lỗi",
                    "Có lỗi xảy ra khi tạo phòng. Vui lòng thử lại sau!",
                    QMessageBox.StandardButton.Ok
                )

'''
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
        content_layout.addSpacing(10)

        # Thêm tiêu đề

        desc = QLabel("** Vui lòng điền đầy đủ thông tin để thêm phòng mới vào hệ thống.")
        #desc.setStyleSheet("color: #666; font-size: 13px;")
        desc.setAlignment(Qt.AlignLeft)
        desc_1 = QLabel("** Nhập đầy đủ thông tin và đảm bảo các thông tin được nhập là chính xác")
        desc_1.setAlignment(Qt.AlignLeft)

        content_layout.addWidget(desc)
        content_layout.addWidget(desc_1)
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
        form_row.addSpacing(10)
        form_row.addLayout(form_right)
        content_layout.addLayout(form_row)

        # BUTTON TẠO PHÒNG
        btn_create = QPushButton("Tạo phòng")
        btn_create.setFixedWidth(180)



        btn_create.clicked.connect(self.handle_create_room)
        content_layout.addSpacing(10)
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
'''