import datetime
from datetime import datetime
now = datetime.now()
import os
import shutil

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox, QTextEdit,
    QPushButton, QFileDialog, QHBoxLayout, QCheckBox, QMessageBox,
    QScrollArea, QLineEdit, QGridLayout, QFormLayout
)
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class FindNewTenant(QWidget):
    def __init__(self, main_window, ds_phong=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        layout_main = QVBoxLayout(self)
        layout_main.addWidget(scroll)

        container = QWidget()
        #container.setStyleSheet("background-color: white; border-radius: 20px; padding: 32px;")
        scroll.setWidget(container)

        layout = QVBoxLayout(container)
        layout.setSpacing(16)

        title = QLabel("📣 Đăng quảng cáo tìm người thuê mới")
        #title.setStyleSheet("font-size: 22px; font-weight: bold;")
        title.setObjectName("Title")  # ✅ sẽ dùng style của QLabel#Title

        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Chọn phòng
        layout_chonphong = QVBoxLayout()
        label_phong = QLabel("📄 Chọn phòng:")
        #label_phong.setStyleSheet("font-weight: bold; color: #333; font-size: 16px;")

        self.room_id_map = {phong["RoomName"]: phong["RoomID"] for phong in ds_phong}

        self.combo_phong = QComboBox()
        #self.combo_phong.addItems(ds_phong or ["Phòng A1", "Phòng B2"])
        self.combo_phong.setFixedHeight(34)
        self.combo_phong.setFixedWidth(250)
        self.combo_phong.setStyleSheet("""
            QComboBox {
                background-color: #DBF7F1;
                color: black;
                font-size: 16px;
                border: 1.5px solid #ccc;
                border-radius: 8px;
                padding: 4px 8px;
            }

            QComboBox QAbstractItemView {
                background-color: #DBF7F1;
                selection-background-color: #FFA07A;  /* khi chọn */
                selection-color: black;
                font-size: 15px;
            }

            QComboBox::item:hover {
                background-color: #f0f0f0;  /* khi hover */
                color: black;

            }
        """)

        # Sau khi khởi tạo xong thì mới addItems
        self.combo_phong.addItems([phong["RoomName"] for phong in ds_phong])

        layout_chonphong.addWidget(label_phong)
        layout_chonphong.addWidget(self.combo_phong)
        layout.addLayout(layout_chonphong)



        # Thông tin phòng: Giá phòng, Giá điện, Giá nước, Địa chỉ
        layout.addSpacing(10)
        info_title = QLabel("💰 Thông tin giá và địa chỉ:")
        info_title.setStyleSheet("font-weight: bold; color: #333; font-size: 16px;")
        layout.addWidget(info_title)

        # Tạo form layout cho các thông tin
        form_layout = QFormLayout()
        form_layout.setVerticalSpacing(12)
        form_layout.setHorizontalSpacing(15)

        # Style chung cho các input
        input_style = """
            QLineEdit {
                font-size: 16px;
                border: 1.5px solid #ccc;
                border-radius: 8px;
                padding: 6px;
                background-color: #DBF7F1;
            }
        """

        # Giá phòng
        self.txt_gia_phong = QLineEdit()
        self.txt_gia_phong.setPlaceholderText("VD: 3,000,000 VNĐ/tháng")
        self.txt_gia_phong.setFixedHeight(34)
        self.txt_gia_phong.setFixedWidth(250)
        #self.txt_gia_phong.setStyleSheet(input_style)
        form_layout.addRow(QLabel("💵 Giá phòng:"), self.txt_gia_phong)

        # Giá điện
        self.txt_gia_dien = QLineEdit()
        self.txt_gia_dien.setPlaceholderText("VD: 3,500 VNĐ/kWh")
        self.txt_gia_dien.setFixedHeight(34)
        self.txt_gia_dien.setFixedWidth(250)
        #self.txt_gia_dien.setStyleSheet(input_style)
        form_layout.addRow(QLabel("⚡ Giá điện:"), self.txt_gia_dien)

        # Giá nước
        self.txt_gia_nuoc = QLineEdit()
        self.txt_gia_nuoc.setPlaceholderText("VD: 15,000 VNĐ/khối")
        self.txt_gia_nuoc.setFixedHeight(34)
        self.txt_gia_nuoc.setFixedWidth(250)
        #self.txt_gia_nuoc.setStyleSheet(input_style)
        form_layout.addRow(QLabel("💧 Giá nước:"), self.txt_gia_nuoc)

        # Địa chỉ
        self.txt_dia_chi = QTextEdit()
        self.txt_dia_chi.setPlaceholderText("Địa chỉ chi tiết (số nhà, đường, phường, quận, thành phố)")
        self.txt_dia_chi.setFixedHeight(60)
        #self.txt_dia_chi.setStyleSheet("""
           # QTextEdit {
               # font-size: 16px;
               # border: 1.5px solid #ccc;
               # border-radius: 8px;
               # padding: 6px;
               # background-color: #DBF7F1;
          #  }
       # """)
        form_layout.addRow(QLabel("📍 Địa chỉ:"), self.txt_dia_chi)

        # Thiết lập style cho labels
        for i in range(form_layout.rowCount()):
            label_item = form_layout.itemAt(i, QFormLayout.LabelRole)
            if label_item:
                label = label_item.widget()
                if label:
                    label.setStyleSheet("font-size: 16px; color: #333;")

        layout.addLayout(form_layout)

        # Mô tả
        layout_mota = QVBoxLayout()
        label_mota = QLabel("📝 Mô tả phòng:")
        #label_mota.setStyleSheet("font-weight: bold; color: #333; font-size: 16px;")
        self.txt_mota = QTextEdit()
        self.txt_mota.setPlaceholderText("Mô tả ngắn gọn, hấp dẫn để thu hút người thuê...")
        self.txt_mota.setFixedHeight(100)
        #self.txt_mota.setStyleSheet("""
           # QTextEdit {
                #font-size: 16px;
                #border: 1.5px solid #ccc;
                #border-radius: 10px;
                #padding: 6px;
           # }
        #""")
        layout_mota.addWidget(label_mota)
        layout_mota.addWidget(self.txt_mota)
        layout.addLayout(layout_mota)

        # Tiện ích
        layout.addSpacing(10)
        tienich_title = QLabel("🛠️ Tiện ích có sẵn:")
        #tienich_title.setStyleSheet("font-weight: bold; color: #333; font-size: 16px;")
        layout.addWidget(tienich_title)

        # Tạo grid layout cho các tiện ích
        tienich_grid = QGridLayout()
        tienich_grid.setHorizontalSpacing(10)
        tienich_grid.setVerticalSpacing(10)

        # Danh sách các tiện ích phổ biến
        tienich_items = [
            "Wifi miễn phí", "Chỗ để xe", "Máy lạnh/Điều hòa", "Tủ lạnh",
            "Máy giặt", "Bảo vệ 24/7", "TV", "Bếp",
            "Tầng lầu", "Gác lửng", "Phòng tắm", "Ban công",
            "Nội thất cơ bản", "Thú cưng"
        ]

        # Tạo các checkbox tiện ích
        self.tienich_checks = {}
        row, col = 0, 0
        for item in tienich_items:
            checkbox = QCheckBox(item)
            self.tienich_checks[item] = checkbox
            tienich_grid.addWidget(checkbox, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        layout.addLayout(tienich_grid)

        # Tải ảnh
        layout.addSpacing(10)
        image_box = QVBoxLayout()
        image_box.setSpacing(8)


        #TODO: cho phép up nhiều ảnh và ảnh lên sẽ đặt kế bên đối xứng

        # Label ảnh
        label_anh = QLabel("🖼️ Hình ảnh:")
        label_anh.setStyleSheet("font-weight: bold; color: #333; font-size: 16px;")
        image_box.addWidget(label_anh, alignment=Qt.AlignLeft)

        # Nút tải ảnh
        self.btn_upload = QPushButton("📷 Tải ảnh lên")
        '''
        self.btn_upload.setStyleSheet("""
            padding: 6px 12px;
            font-size: 16px;
            background-color: #6c63ff;
            color: white;
            border-radius: 8px;
        """)
        '''
        self.btn_upload.setFixedWidth(150)
        self.btn_upload.clicked.connect(self.upload_image)
        image_box.addWidget(self.btn_upload, alignment=Qt.AlignHCenter)

        # Khu vực hiển thị ảnh
        self.preview_image = QLabel()
        self.preview_image.setFixedSize(240, 180)
        #self.preview_image.setStyleSheet("border: 1px solid #ccc; border-radius: 12px;")
        self.preview_image.setAlignment(Qt.AlignCenter)
        image_box.addWidget(self.preview_image, alignment=Qt.AlignHCenter)

        # Đường dẫn
        self.label_anh_path = QLabel("Chưa chọn hình ảnh")
        #self.label_anh_path.setStyleSheet("font-size: 14px; color: #555;")
        image_box.addWidget(self.label_anh_path, alignment=Qt.AlignHCenter)

        layout.addLayout(image_box)

        # Ưu tiên
        layout.addSpacing(10)
        label_uu_tien = QLabel("💡 Ưu tiên đối tượng thuê:")
        #label_uu_tien.setStyleSheet("font-weight: bold; color: #333; font-size: 16px;")
        self.check_sv = QCheckBox("🎓 Sinh viên")
        self.check_sv.setFixedWidth(250)
        self.check_nu = QCheckBox("😊 Nữ")
        self.check_nu.setFixedWidth(250)
        self.check_o_ghep = QCheckBox("👥 Ở ghép")
        self.check_o_ghep.setFixedWidth(250)

        for chk in (self.check_sv, self.check_nu, self.check_o_ghep):
            chk.setStyleSheet("""
                QCheckBox {
                    font-size: 16px;
                    padding: 6px 12px;
                    border-radius: 10px;
                    background-color: #f5f5f5;
                }
                QCheckBox:hover {
                    background-color: #e0e7ff;
                }
                QCheckBox::indicator {
                    width: 18px;
                    height: 18px;
                    border-radius: 5px;
                    background-color: white;
                    border: 2px solid #6c63ff;
                }
                QCheckBox::indicator:checked {
                    background-color: #6c63ff;
                }
                QCheckBox::indicator:unchecked {
                    background-color: white;
                }
            """)

        uu_tien_layout = QHBoxLayout()
        uu_tien_layout.addWidget(self.check_sv)
        uu_tien_layout.addWidget(self.check_nu)
        uu_tien_layout.addWidget(self.check_o_ghep)

        layout.addWidget(label_uu_tien)
        layout.addLayout(uu_tien_layout)

        # Thông tin liên hệ
        layout.addSpacing(10)
        contact_title = QLabel("📞 Thông tin liên hệ:")
        #contact_title.setStyleSheet("font-weight: bold; color: #333; font-size: 16px;")
        layout.addWidget(contact_title)


        contact_form = QFormLayout()
        contact_form.setVerticalSpacing(12)

        # Gán style cố định cho label để thẳng hàng
        label_style = "min-width: 140px; font-weight: bold;"

        # Tên liên hệ
        self.txt_contact_name = QLineEdit()
        self.txt_contact_name.setPlaceholderText("Họ và tên người liên hệ")
        self.txt_contact_name.setFixedHeight(34)
        #self.txt_contact_name.setStyleSheet(input_style)
        label_contact_name = QLabel("👤 Tên liên hệ:")
        label_contact_name.setStyleSheet(label_style)
        contact_form.addRow(label_contact_name, self.txt_contact_name)

        # Số điện thoại
        self.txt_contact_phone = QLineEdit()
        self.txt_contact_phone.setPlaceholderText("Số điện thoại liên hệ")
        self.txt_contact_phone.setFixedHeight(34)
        #self.txt_contact_phone.setStyleSheet(input_style)
        label_contact_phone = QLabel("📱 Điện thoại:")
        label_contact_phone.setStyleSheet(label_style)
        contact_form.addRow(label_contact_phone, self.txt_contact_phone)

        # Email
        self.txt_contact_email = QLineEdit()
        self.txt_contact_email.setPlaceholderText("Email liên hệ (không bắt buộc)")
        self.txt_contact_email.setFixedHeight(34)
        #self.txt_contact_email.setStyleSheet(input_style)
        label_contact_email = QLabel("✉️ Email:")
        label_contact_email.setStyleSheet(label_style)
        contact_form.addRow(label_contact_email, self.txt_contact_email)


        # Thiết lập style cho labels
        for i in range(contact_form.rowCount()):
            label_item = contact_form.itemAt(i, QFormLayout.LabelRole)
            if label_item:
                label = label_item.widget()
                if label:
                    label.setStyleSheet("font-size: 16px; color: #333;")

        layout.addLayout(contact_form)

        # Nút đăng quảng cáo
        layout.addSpacing(20)
        self.btn_submit = QPushButton("📢 Đăng quảng cáo")
        self.btn_submit.setFixedWidth(200)
        '''
        self.btn_submit.setStyleSheet("""
            background-color: #6c63ff;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
        """)
        '''
        self.btn_submit.clicked.connect(self.submit_quangcao)
        layout.addWidget(self.btn_submit, alignment=Qt.AlignCenter)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh phòng", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            # Tạo thư mục lưu nếu chưa có
            project_root = os.path.dirname(os.path.abspath(__file__))
            upload_dir = os.path.join(project_root, "../../../../../uploads/RoomAdvertisement")
            os.makedirs(upload_dir, exist_ok=True)

            # Đặt tên ảnh mới không trùng lặp theo timestamp
            extension = os.path.splitext(file_path)[1]
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            new_filename = f"room_{timestamp}{extension}"
            new_file_path = os.path.join(upload_dir, new_filename)

            # Sao chép ảnh vào thư mục dự án
            shutil.copy(file_path, new_file_path)

            # Lưu lại path mới (để lưu vào database)
            self.file_image_path = os.path.abspath(new_file_path)
            self.label_anh_path.setText(f"📁 {new_filename}")

            # Hiển thị preview ảnh
            pixmap = QPixmap(new_file_path)
            if pixmap.isNull():
                self.preview_image.clear()
                QMessageBox.critical(self, "Lỗi", "❌ Không thể đọc ảnh này.")
                return

            scaled = pixmap.scaled(
                self.preview_image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.preview_image.setPixmap(scaled)

    def get_selected_tienich(self):
        selected = []
        for name, checkbox in self.tienich_checks.items():
            if checkbox.isChecked():
                selected.append(name)
        return selected

    def submit_quangcao(self):
        # Thu thập dữ liệu cần thiết theo yêu cầu của controller
        phong = self.combo_phong.currentText()
        room_name = self.combo_phong.currentText()
        room_id = self.room_id_map.get(room_name)
        mota = self.txt_mota.toPlainText()

        # Thu thập các trường thông tin bổ sung để thêm vào mô tả
        gia_phong = self.txt_gia_phong.text()
        gia_dien = self.txt_gia_dien.text()
        gia_nuoc = self.txt_gia_nuoc.text()
        dia_chi = self.txt_dia_chi.toPlainText()
        tien_ich = self.get_selected_tienich()

        # Thu thập thông tin liên hệ
        ten_lienhe = self.txt_contact_name.text() if hasattr(self, 'txt_contact_name') else ""
        dienthoai = self.txt_contact_phone.text() if hasattr(self, 'txt_contact_phone') else ""
        email = self.txt_contact_email.text() if hasattr(self, 'txt_contact_email') else ""

        # Tạo mô tả đầy đủ kết hợp tất cả thông tin
        full_description = mota

        # Thêm thông tin giá và địa chỉ vào mô tả
        if gia_phong:
            full_description += f"\n\n💰 Giá phòng: {gia_phong}"
        if gia_dien:
            full_description += f"\n⚡ Giá điện: {gia_dien}"
        if gia_nuoc:
            full_description += f"\n💧 Giá nước: {gia_nuoc}"
        if dia_chi:
            full_description += f"\n\n📍 Địa chỉ: {dia_chi}"

        # Thêm tiện ích vào mô tả nếu có
        if tien_ich:
            full_description += "\n\n🛠️ Tiện ích: " + ", ".join(tien_ich)

        # Thêm thông tin liên hệ vào mô tả
        contact_info = []
        if ten_lienhe:
            contact_info.append(f"👤 {ten_lienhe}")
        if dienthoai:
            contact_info.append(f"📱 {dienthoai}")
        if email:
            contact_info.append(f"✉️ {email}")

        if contact_info:
            full_description += "\n\n📞 Liên hệ: " + " | ".join(contact_info)

        # Thu thập ưu tiên
        uu_tien = []
        if self.check_sv.isChecked(): uu_tien.append("Sinh viên")
        if self.check_nu.isChecked(): uu_tien.append("Nữ")
        if self.check_o_ghep.isChecked(): uu_tien.append("Ở ghép")

        # Thu thập đường dẫn ảnh
        image = getattr(self, "file_image_path", None)

        # Kiểm tra thông tin bắt buộc
        if not phong or not full_description:
            self.show_error("Phòng và mô tả không được để trống!")
            return

        # Gọi controller xử lý với các tham số phù hợp với định nghĩa hiện tại
        from QLNHATRO.RentalManagementApplication.controller.AdvertisementController.AdvertisementController import \
            AdvertisementController
        AdvertisementController.handle_submit_ad(
            room_name=phong,
            description=full_description,
            image_path=image,
            preferences=uu_tien,
            view=self, # truyền view để gọi show_error/show_success
            RoomID = room_id,
        )

    def show_error(self, message):
        QMessageBox.critical(self, "Lỗi", message)

    def show_success(self, message):
        QMessageBox.information(self, "Thành công", message)