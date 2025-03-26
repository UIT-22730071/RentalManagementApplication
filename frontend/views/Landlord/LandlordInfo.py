from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout,
    QPushButton, QGroupBox
)

from QLNHATRO.RentalManagementApplication.frontend.Component.LabelUI import LabelUI
from QLNHATRO.RentalManagementApplication.frontend.views.UpdateUI.InforUpdater import InfoUpdater


# Nhớ đảm bảo file LabelUI.py tồn tại

class LandlordInfo(QWidget):
    def __init__(self, main_window):
        super().__init__()

        #self.main_window = main_window
        self.Landlord = ['0','1','2','3','4','5','6','7','*']
        # self.Landlord = Landlord
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                color: white;
                font-family: Arial;
            }
            QPushButton {
                background-color: #203BEC;
                color: white;
                padding: 6px 12px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #d35400;
            }
        """)

        main_layout = QVBoxLayout()

        # Tiêu đề
        title = QLabel("👤 THÔNG TIN CHỦ TRỌ")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        content_widget = QWidget()
        content_layout = QVBoxLayout()

        # Danh sách các trường
        field_names = [
            "Họ và Tên", "Ngày Sinh", "CCCD", "Giới tính",
            "Nghề nghiệp", "Số điện thoại", "Tình trạng hôn nhân","Mật khẩu"
        ]

        self.label_fields = []

        for i, field in enumerate(field_names):
            group = QGroupBox()
            hbox = QHBoxLayout()

            label = QLabel(f"{field}:")
            label.setStyleSheet("font-size: 16px; min-width: 140px;")

            try:
                label_ui = LabelUI(str(self.Landlord[i]))
            except Exception as e:
                print(f"Lỗi khi tạo LabelUI ở chỉ mục {i}: {e}")
                continue  # Bỏ qua nếu lỗi
            else:
                self.label_fields.append(label_ui)

                update_btn = QPushButton("Cập nhật")
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
            "Nghề nghiệp", "Số điện thoại", "Tình trạng hôn nhân","Mật khẩu"
        ][index]
        print(label)

        # Mở dialog cập nhật
        dialog = InfoUpdater(
            title=field_name,
            current_value=label.text(),
            on_update_callback=lambda new_val: self.apply_update(index, new_val)

        )

        dialog.exec_()

    def apply_update(self, index, new_value):
        self.label_fields[index].setText(new_value)
        self.Landlord[index] = new_value
        print(f"✅ Đã cập nhật: {new_value}")
        # TODO: Gửi về database tại đây nếu cần