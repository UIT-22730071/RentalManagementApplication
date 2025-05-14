from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout,
    QPushButton, QGroupBox, QMessageBox
)

from QLNHATRO.RentalManagementApplication.frontend.Component.LabelUI import LabelUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.UpdateUI.InforUpdater import InfoUpdater


class LandlordInfo(QWidget):
    def __init__(self, main_window, id_lanlord, information_data):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.id_lanlord = id_lanlord
        self.main_window = main_window

        if information_data is None:
            self.information = {
                'name': 'None ',
                'birth': 'None ',
                'cccd': ' None',
                'sex': ' None',
                'job': 'None ',
                'phone': ' None',
                'marriage': 'None',
                'password': '**********'}
        else:
            self.information = information_data

        main_layout = QVBoxLayout()

        title = QLabel("👤 THÔNG TIN CHỦ TRỌ")
        #title.setStyleSheet("font-size: 24px; font-weight: bold;")
        title.setObjectName("Title")  # ✅ sẽ dùng style của QLabel#Title
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout()

        field_names = [
            "Họ và Tên", "Ngày Sinh", "CCCD", "Giới tính",
            "Nghề nghiệp", "Số điện thoại", "Tình trạng hôn nhân"
        ]
        field_keys = ['name', 'birth', 'cccd', 'sex', 'job', 'phone', 'marriage']

        self.label_fields = []

        for i, field in enumerate(field_names):
            group = QGroupBox()
            hbox = QHBoxLayout()

            label = QLabel(f"{field}:")
            label.setStyleSheet("font-size: 16px; min-width: 140px;")

            try:
                value = self.information.get(field_keys[i], "Chưa có dữ liệu")
                label_ui = LabelUI(str(value))
            except Exception as e:
                print(f"Lỗi khi tạo LabelUI ở chỉ mục {i}: {e}")
                continue
            else:
                self.label_fields.append(label_ui)

                update_btn = QPushButton("Cập nhật")
                update_btn.setFixedHeight(40)
                update_btn.setFixedWidth(200)
                update_btn.clicked.connect(lambda _, index=i: self.update_field(index))

                hbox.addWidget(label)
                hbox.addWidget(label_ui, stretch=1)
                hbox.addWidget(update_btn)
                group.setLayout(hbox)
                content_layout.addWidget(group)

        # ➕ Thêm phần mật khẩu riêng
        #password_group = QGroupBox()
        #password_layout = QHBoxLayout()

        #password_label = QLabel("Mật khẩu:")
        #password_label.setStyleSheet("font-size: 16px; min-width: 140px;")
        #password_ui = LabelUI("**********")

        #change_pass_btn = QPushButton("Đổi mật khẩu")
        #change_pass_btn.clicked.connect(self.open_change_password_dialog)

        #password_layout.addWidget(password_label)
        #password_layout.addWidget(password_ui, stretch=1)
        #password_layout.addWidget(change_pass_btn)
        #password_group.setLayout(password_layout)

        #content_layout.addWidget(password_group)

        content_widget.setLayout(content_layout)
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

    def update_field(self, index):
        label = self.label_fields[index]
        field_name = [
            "Họ và Tên", "Ngày Sinh", "CCCD", "Giới tính",
            "Nghề nghiệp", "Số điện thoại", "Tình trạng hôn nhân"
        ][index]

        dialog = InfoUpdater(
            title=field_name,
            current_value=label.text(),
            on_update_callback=lambda new_val: self.apply_update(index, new_val)
        )
        dialog.exec_()

    def apply_update(self, index, new_value):
        field_keys = ['name', 'birth', 'cccd', 'sex', 'job', 'phone', 'marriage']
        key = field_keys[index]

        self.label_fields[index].setText(new_value)
        self.information[key] = new_value
        print(f"✅ Đã cập nhật {key}: {new_value}")

        from QLNHATRO.RentalManagementApplication.controller.LandlordController.LandlordController import LandlordController
        controller = LandlordController()
        controller.update_landlord_field(self.id_lanlord, key, new_value)

    def open_change_password_dialog(self):
        QMessageBox.information(self, "Đổi mật khẩu", "Mở cửa sổ đổi mật khẩu tại đây.")
        # TODO: sau này sẽ mở form nhập mật khẩu cũ + mới để xác nhận
