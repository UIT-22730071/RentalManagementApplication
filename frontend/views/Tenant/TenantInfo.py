from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout,
    QPushButton, QGroupBox
)

from QLNHATRO.RentalManagementApplication.frontend.Component.LabelUI import LabelUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.Component.InforUpdater import InfoUpdater


class TenantInfo(QWidget):
    tenant_info_updated = pyqtSignal(dict)

    def __init__(self, main_window, initial_data=None, tenant_id=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window
        self.tenant_id = tenant_id

        # Default initial data
        if initial_data is None:
            self.information = {
                'full_name': 'None',
                'birth_date': 'None',
                'citizen_id': 'None',
                'gender': 'None',
                'occupation': 'None',
                'email':'None',
                'phone_number': 'None',
                'marital_status': 'None'
            }
        else:
            self.information = initial_data

        main_layout = QVBoxLayout()

        title = QLabel("👥 THÔNG TIN NGƯỜI THUÊ")
        title.setObjectName("Title")  # ✅ sẽ dùng style của QLabel#Title
        title.setFixedHeight(60)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout()

        field_names = [
            "Họ và Tên", "Ngày Sinh", "CCCD", "Giới tính",
            "Nghề nghiệp", "Email" ,"Số điện thoại", "Tình trạng hôn nhân"
        ]
        field_keys = ['full_name', 'birth_date', 'citizen_id', 'gender', 'occupation', 'email' ,'phone_number', 'marital_status']

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
        field_keys = ['full_name', 'birth_date', 'citizen_id', 'gender', 'occupation', 'phone_number', 'marital_status']
        key = field_keys[index]

        self.label_fields[index].setText(new_value)
        self.information[key] = new_value
        print(f"✅ Đã cập nhật {key}: {new_value}")

        # Cập nhật tenant data thông qua service
        from QLNHATRO.RentalManagementApplication.services.TenantService import TenantService
        if self.tenant_id:
            success = TenantService.update_tenant_info(self.tenant_id, self.information)
            if success:
                print("✅ Dữ liệu người thuê đã được cập nhật thành công!")
            else:
                print("❌ Cập nhật thất bại.")
        else:
            print("⚠ Không có tenant_id để cập nhật!")

        # Emit signal để báo dữ liệu đã được cập nhật
        self.tenant_info_updated.emit(self.information)

    def load_tenant_data(self, data=None):
        if data:
            self.information = data
            field_keys = ['full_name', 'birth_date', 'citizen_id', 'gender', 'occupation', 'phone_number',
                          'marital_status']

            for i, key in enumerate(field_keys):
                if i < len(self.label_fields):
                    value = self.information.get(key, "Chưa có dữ liệu")
                    self.label_fields[i].setText(str(value))