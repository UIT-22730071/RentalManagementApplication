from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox, QTextEdit,
    QPushButton, QFileDialog, QHBoxLayout, QCheckBox, QMessageBox,
    QScrollArea
)
from PyQt5.QtCore import Qt

class FindNewTenant(QWidget):
    def __init__(self, main_window, ds_phong=None):
        super().__init__()
        self.main_window = main_window
        self.setStyleSheet("background-color: #d4a9a9; padding: 20px;")

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        layout_main = QVBoxLayout(self)
        layout_main.addWidget(scroll)

        container = QWidget()
        container.setStyleSheet("background-color: white; border-radius: 16px; padding: 32px;")
        scroll.setWidget(container)

        layout = QVBoxLayout(container)
        layout.setSpacing(16)

        title = QLabel("📣 Đăng quảng cáo tìm người thuê mới")
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #2c3e50;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Chọn phòng
        layout_chonphong = QVBoxLayout()
        label_phong = QLabel("📄 Chọn phòng:")
        label_phong.setStyleSheet("font-weight: bold; color: #333; font-size: 16px;")
        self.combo_phong = QComboBox()
        self.combo_phong.addItems(ds_phong or ["Phòng A1", "Phòng B2"])
        self.combo_phong.setFixedHeight(34)
        self.combo_phong.setStyleSheet("""
            QComboBox {
                background-color: white;
                color: black;
                font-size: 16px;
                border: 1.5px solid #ccc;
                border-radius: 8px;
                padding: 4px 8px;
            }
        """)
        layout_chonphong.addWidget(label_phong)
        layout_chonphong.addWidget(self.combo_phong)
        layout.addLayout(layout_chonphong)

        # Mô tả
        layout_mota = QVBoxLayout()
        label_mota = QLabel("📝 Mô tả phòng:")
        label_mota.setStyleSheet("font-weight: bold; color: #333; font-size: 16px;")
        self.txt_mota = QTextEdit()
        self.txt_mota.setPlaceholderText("Mô tả ngắn gọn, hấp dẫn để thu hút người thuê...")
        self.txt_mota.setFixedHeight(100)
        self.txt_mota.setStyleSheet("""
            QTextEdit {
                font-size: 16px;
                border: 1.5px solid #ccc;
                border-radius: 10px;
                padding: 6px;
            }
        """)
        layout_mota.addWidget(label_mota)
        layout_mota.addWidget(self.txt_mota)
        layout.addLayout(layout_mota)

        # Tải ảnh
        image_box = QVBoxLayout()
        image_box.setSpacing(8)

        # Label ảnh
        label_anh = QLabel("🖼️ Hình ảnh:")
        label_anh.setStyleSheet("font-weight: bold; color: #333; font-size: 16px;")
        image_box.addWidget(label_anh, alignment=Qt.AlignLeft)

        # Nút tải ảnh
        self.btn_upload = QPushButton("📷 Tải ảnh lên")
        self.btn_upload.setStyleSheet("""
            padding: 6px 12px;
            font-size: 16px;
            background-color: #6c63ff;
            color: white;
            border-radius: 8px;
        """)
        self.btn_upload.setFixedWidth(150)
        self.btn_upload.clicked.connect(self.upload_image)
        image_box.addWidget(self.btn_upload, alignment=Qt.AlignHCenter)

        # Khu vực hiển thị ảnh
        self.preview_image = QLabel()
        self.preview_image.setFixedSize(240, 180)
        self.preview_image.setStyleSheet("border: 1px solid #ccc; border-radius: 12px;")
        self.preview_image.setAlignment(Qt.AlignCenter)
        image_box.addWidget(self.preview_image, alignment=Qt.AlignHCenter)

        # Đường dẫn
        self.label_anh_path = QLabel("Chưa chọn hình ảnh")
        self.label_anh_path.setStyleSheet("font-size: 14px; color: #555;")
        image_box.addWidget(self.label_anh_path, alignment=Qt.AlignHCenter)

        layout.addLayout(image_box)

        # Ưu tiên
        label_uu_tien = QLabel("💡 Ưu tiên:")
        label_uu_tien.setStyleSheet("font-weight: bold; color: #333; font-size: 20px;")
        self.check_sv = QCheckBox("🎓 Sinh viên")
        self.check_sv.setFixedWidth(250)
        self.check_nu = QCheckBox("😊 Nữ")
        self.check_nu.setFixedWidth(250)
        self.check_o_ghep = QCheckBox("👥 Ở ghép")
        self.check_o_ghep.setFixedWidth(250)

        for chk in (self.check_sv, self.check_nu, self.check_o_ghep):
            chk.setStyleSheet("""
                QCheckBox {
                    font-size: 20px;
                    padding: 6px 12px;
                    border-radius: 10px;
                    background-color: #f5f5f5;
                }
                QCheckBox:hover {
                    background-color: #e0e7ff;
                }
                QCheckBox::indicator {
                    width: 20px;
                    height: 20px;
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

        layout.addSpacing(10)
        layout.addWidget(label_uu_tien)
        layout.addLayout(uu_tien_layout)

        self.btn_submit = QPushButton("Đăng quảng cáo")
        self.btn_submit.setFixedWidth(200)
        self.btn_submit.setStyleSheet("""
            background-color: #6c63ff;
            color: white;
            font-size: 18px;
            padding: 8px;
            border-radius: 10px;
        """)
        self.btn_submit.clicked.connect(self.submit_quangcao)
        layout.addSpacing(10)
        layout.addWidget(self.btn_submit, alignment=Qt.AlignCenter)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh phòng", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.file_image_path = file_path
            self.label_anh_path.setText(f"📁 {file_path}")

            pixmap = QPixmap(file_path)
            if pixmap.isNull():
                self.preview_image.clear()
                QMessageBox.critical(self, "Lỗi", "❌ Không thể đọc ảnh này.")
                return

            scaled = pixmap.scaled(
                self.preview_image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.preview_image.setPixmap(scaled)

    def submit_quangcao(self):
        phong = self.combo_phong.currentText()
        mota = self.txt_mota.toPlainText()
        uu_tien = []
        if self.check_sv.isChecked(): uu_tien.append("Sinh viên")
        if self.check_nu.isChecked(): uu_tien.append("Nữ")
        if self.check_o_ghep.isChecked(): uu_tien.append("Ở ghép")
        image = getattr(self, "file_image_path", None)

        print("==> Đăng quảng cáo:")
        print("Phòng:", phong)
        print("Mô tả:", mota)
        print("Ưu tiên:", uu_tien)
        print("Hình ảnh:", image)

        QMessageBox.information(self, "Thành công", "🎉 Quảng cáo phòng trọ đã được đăng!")
