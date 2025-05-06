from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QFileDialog,
    QHBoxLayout, QMessageBox, QGroupBox, QComboBox, QDateEdit, QLineEdit,
    QFormLayout, QSplitter, QFrame, QGridLayout, QScrollArea
)
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QDate
import os


class TenantMaintenanceRequest(QWidget):
    def __init__(self, main_window, tenant_id):
        super().__init__()
        self.main_window = main_window
        self.tenant_id = tenant_id
        self.room_id = self.get_room_id_for_tenant(tenant_id)
        self.image_path = None

        # Thiết lập cửa sổ
        self.setWindowTitle("Yêu Cầu Sửa Chữa")
        self.setMinimumSize(800, 600)
        self.setStyleSheet("""
            QWidget { 
                background-color: #FF7F7F; 
                font-family: 'Segoe UI', Arial; 
            }
            QGroupBox {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                margin-top: 1ex;
                font-weight: bold;
                background-color: #f0f0f0;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton#resetBtn {
                background-color: #e74c3c;
            }
            QPushButton#resetBtn:hover {
                background-color: #c0392b;
            }
            QTextEdit, QComboBox, QLineEdit, QDateEdit {
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                padding: 8px;
                background-color: white;
            }
            QLabel#titleLabel {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                padding: 10px;
                background-color: #f0f0f0;
                border-radius: 5px;
            }
            QLabel#infoLabel {
                color: #7f8c8d;
                font-style: italic;
            }
            QLabel#sectionLabel {
                font-weight: bold;
                color: #2c3e50;
            }
            QLabel#imagePreview {
                border: 1px dashed #bdc3c7;
                border-radius: 4px;
                background-color: white;
                min-height: 120px;
                min-width: 120px;
            }
            QFrame#headerFrame {
                background-color: white;
                border-radius: 10px;
                margin: 5px;
            }
            QFrame#contentFrame {
                background-color: white;
                border-radius: 10px;
                margin: 5px;
            }
        """)

        self.init_ui()

    def init_ui(self):
        # Layout chính
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # --- Tiêu đề ---
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        header_layout = QVBoxLayout(header_frame)

        title = QLabel("🔧 GỬI YÊU CẦU SỬA CHỮA")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title)

        # --- Thông tin phòng ---
        room_info = QLabel(f"Phòng: #{self.room_id} | Mã người thuê: {self.tenant_id}")
        room_info.setObjectName("infoLabel")
        room_info.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(room_info)

        main_layout.addWidget(header_frame)

        # --- Nội dung chính ---
        content_frame = QFrame()
        content_frame.setObjectName("contentFrame")
        content_layout = QGridLayout(content_frame)

        # --- Cột trái - Mô tả chi tiết sự cố ---
        left_col = 0

        # Label mô tả
        desc_label = QLabel("📝 Mô tả chi tiết sự cố")
        desc_label.setObjectName("sectionLabel")
        content_layout.addWidget(desc_label, 0, left_col)

        # Loại sự cố
        issue_type_label = QLabel("Loại sự cố:")
        content_layout.addWidget(issue_type_label, 1, left_col)

        self.issue_type_combo = QComboBox()
        self.issue_type_combo.addItems([
            "--- Chọn loại sự cố ---",
            "Điện - Đèn, ổ cắm, thiết bị điện",
            "Nước - Ống nước, vòi, bồn cầu",
            "Cấu trúc - Tường, trần, sàn, cửa",
            "Đồ nội thất - Giường, tủ, bàn ghế",
            "Thiết bị - Máy lạnh, quạt, tủ lạnh",
            "Côn trùng - Muỗi, kiến, gián",
            "An ninh - Khóa, cửa, camera",
            "Khác"
        ])
        content_layout.addWidget(self.issue_type_combo, 2, left_col)

        # Mức độ khẩn cấp
        urgency_label = QLabel("Mức độ khẩn cấp:")
        content_layout.addWidget(urgency_label, 3, left_col)

        self.urgency_combo = QComboBox()
        self.urgency_combo.addItems([
            "Bình thường - Có thể chờ đợi",
            "Khẩn cấp - Cần sửa trong 24h",
            "Rất khẩn cấp - Cần sửa ngay lập tức"
        ])
        content_layout.addWidget(self.urgency_combo, 4, left_col)

        # Chi tiết sự cố
        detail_label = QLabel("Chi tiết sự cố:")
        content_layout.addWidget(detail_label, 5, left_col)

        self.description_edit = QTextEdit()
        self.description_edit.setPlaceholderText(
            "Mô tả chi tiết về sự cố trong phòng...\nVị trí chính xác, thời điểm phát hiện, ảnh hưởng đến sinh hoạt...")
        self.description_edit.setMinimumHeight(200)
        content_layout.addWidget(self.description_edit, 6, left_col)

        # --- Cột phải - Thông tin bổ sung ---
        right_col = 1

        # Thời gian phát hiện
        time_label = QLabel("⏰ Thời gian phát hiện")
        time_label.setObjectName("sectionLabel")
        content_layout.addWidget(time_label, 0, right_col)

        self.date_edit = QDateEdit(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setMaximumDate(QDate.currentDate())
        self.date_edit.setDisplayFormat("dd/MM/yyyy")
        content_layout.addWidget(self.date_edit, 1, right_col)

        # Hình ảnh minh họa
        img_label = QLabel("📷 Hình ảnh minh họa")
        img_label.setObjectName("sectionLabel")
        content_layout.addWidget(img_label, 2, right_col)

        self.image_label = QLabel("Chưa có ảnh được chọn")
        self.image_label.setObjectName("imagePreview")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumHeight(120)
        content_layout.addWidget(self.image_label, 3, right_col)

        self.upload_btn = QPushButton("🖼️ Chọn ảnh")
        self.upload_btn.clicked.connect(self.upload_image)
        content_layout.addWidget(self.upload_btn, 4, right_col)

        # Thông tin liên hệ
        contact_label = QLabel("📞 Thông tin liên hệ")
        contact_label.setObjectName("sectionLabel")
        content_layout.addWidget(contact_label, 5, right_col)

        contact_form = QFormLayout()

        self.contact_phone = QLineEdit()
        self.contact_phone.setPlaceholderText("Số điện thoại liên hệ")
        contact_form.addRow("Điện thoại:", self.contact_phone)

        self.available_time = QLineEdit()
        self.available_time.setPlaceholderText("VD: Sau 18h hàng ngày")
        contact_form.addRow("Thời gian thuận tiện:", self.available_time)

        contact_widget = QWidget()
        contact_widget.setLayout(contact_form)
        content_layout.addWidget(contact_widget, 6, right_col)

        # Thiết lập kích thước cột
        content_layout.setColumnStretch(left_col, 2)
        content_layout.setColumnStretch(right_col, 1)

        main_layout.addWidget(content_frame)

        # --- Nút bấm ---
        btn_layout = QHBoxLayout()

        # Thêm khoảng trống đẩy các nút sang phải
        btn_layout.addStretch()

        self.reset_btn = QPushButton("ĐẶT LẠI")
        self.reset_btn.setObjectName("resetBtn")
        self.reset_btn.clicked.connect(self.reset_form)
        btn_layout.addWidget(self.reset_btn)

        self.submit_btn = QPushButton("GỬI YÊU CẦU")
        self.submit_btn.clicked.connect(self.submit_request)
        btn_layout.addWidget(self.submit_btn)

        main_layout.addLayout(btn_layout)

        # Hiển thị lịch sử sửa chữa gần đây
        self.add_maintenance_history()
        main_layout.addWidget(self.create_maintenance_history())

        self.setLayout(main_layout)

    def add_maintenance_history(self):
        # Hàm này sẽ tải lịch sử yêu cầu sửa chữa của phòng hiện tại
        # Tạm thời sử dụng dữ liệu giả
        self.maintenance_history = [
            {
                "id": 1,
                "description": "Vòi nước bị rỉ",
                "status": "Đã hoàn thành",
                "date": "01/04/2025"
            },
            {
                "id": 2,
                "description": "Đèn phòng tắm không sáng",
                "status": "Đang xử lý",
                "date": "20/04/2025"
            }
        ]

    def create_maintenance_history(self):
        # Tạo một frame chứa lịch sử
        history_container = QFrame()
        history_container.setStyleSheet("background-color: white; border-radius: 5px;")

        # Tạo layout cho frame
        history_layout = QVBoxLayout(history_container)
        history_layout.setContentsMargins(0, 0, 0, 0)

        if not hasattr(self, 'maintenance_history') or not self.maintenance_history:
            no_data = QLabel("Không có yêu cầu sửa chữa gần đây")
            no_data.setAlignment(Qt.AlignCenter)
            no_data.setStyleSheet("color: #7f8c8d; padding: 15px;")
            history_layout.addWidget(no_data)
        else:
            # Tạo table-like layout với header
            grid = QGridLayout()
            grid.setSpacing(10)

            # Header
            headers = ["#", "Mô tả sự cố", "Trạng thái", "Ngày"]
            for col, header in enumerate(headers):
                label = QLabel(header)
                label.setStyleSheet("font-weight: bold; padding: 5px; background-color: #f0f0f0;")
                grid.addWidget(label, 0, col)

            # Rows
            for row, item in enumerate(self.maintenance_history, 1):
                # ID
                id_label = QLabel(f"#{item['id']}")
                id_label.setAlignment(Qt.AlignCenter)
                grid.addWidget(id_label, row, 0)

                # Description
                desc_label = QLabel(item["description"])
                grid.addWidget(desc_label, row, 1)

                # Status
                status_label = QLabel(item["status"])
                if item["status"] == "Đã hoàn thành":
                    status_label.setStyleSheet("color: #27ae60; font-weight: bold;")
                else:
                    status_label.setStyleSheet("color: #f39c12; font-weight: bold;")
                grid.addWidget(status_label, row, 2)

                # Date
                date_label = QLabel(item["date"])
                date_label.setAlignment(Qt.AlignCenter)
                grid.addWidget(date_label, row, 3)

            # Set column stretch
            grid.setColumnStretch(0, 1)  # ID
            grid.setColumnStretch(1, 3)  # Description
            grid.setColumnStretch(2, 2)  # Status
            grid.setColumnStretch(3, 1)  # Date

            history_layout.addLayout(grid)

        return history_container

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Chọn ảnh minh họa",
            "",
            "Images (*.png *.xpm *.jpg *.jpeg)"
        )

        if file_path:
            self.image_path = file_path
            # Hiển thị ảnh thu nhỏ
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(300, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.image_label.setPixmap(pixmap)
                self.image_label.setToolTip(file_path)
            else:
                file_name = os.path.basename(file_path)
                self.image_label.setText(f"Đã chọn: {file_name}")

    def submit_request(self):
        # Lấy thông tin từ form
        issue_type = self.issue_type_combo.currentText()
        urgency = self.urgency_combo.currentText()
        description = self.description_edit.toPlainText().strip()

        # Kiểm tra điều kiện
        if issue_type == "--- Chọn loại sự cố ---":
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng chọn loại sự cố.")
            return

        if not description:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập mô tả chi tiết sự cố.")
            return

        # Tạo chuỗi mô tả đầy đủ
        full_description = f"[{issue_type}] [{urgency}]\n{description}"

        # Thêm thông tin liên hệ nếu có
        contact_info = []
        if self.contact_phone.text().strip():
            contact_info.append(f"SĐT: {self.contact_phone.text().strip()}")
        if self.available_time.text().strip():
            contact_info.append(f"Thời gian liên hệ: {self.available_time.text().strip()}")

        if contact_info:
            full_description += "\n\nThông tin liên hệ:\n" + "\n".join(contact_info)

        # Thêm thời gian phát hiện
        discovery_date = self.date_edit.date().toString("dd/MM/yyyy")
        full_description += f"\n\nThời gian phát hiện sự cố: {discovery_date}"

        # Đóng gói dữ liệu
        request_data = {
            "room_id": self.room_id,
            "tenant_id": self.tenant_id,
            "description": full_description,
            "image_path": self.image_path or ""
        }

        # Gửi dữ liệu cho controller/service
        try:
            from QLNHATRO.RentalManagementApplication.controller.TenantController.TenantController import \
                TenantController
            TenantController.submit_maintenance_request(request_data)

            QMessageBox.information(
                self,
                "Đã gửi",
                "Yêu cầu sửa chữa đã được gửi đến chủ trọ.\nBạn sẽ nhận được phản hồi trong thời gian sớm nhất."
            )

            # Cập nhật lịch sử yêu cầu sau khi gửi thành công
            self.add_maintenance_history()
            self.reset_form()
        except Exception as e:
            QMessageBox.critical(
                self,
                "Lỗi",
                f"Không thể gửi yêu cầu. Lỗi: {str(e)}"
            )

    def reset_form(self):
        self.description_edit.clear()
        self.image_label.setPixmap(QPixmap())  # Xóa hình ảnh
        self.image_label.setText("Chưa có ảnh được chọn")
        self.image_path = None
        self.issue_type_combo.setCurrentIndex(0)
        self.urgency_combo.setCurrentIndex(0)
        self.date_edit.setDate(QDate.currentDate())
        self.contact_phone.clear()
        self.available_time.clear()

    def get_room_id_for_tenant(self, tenant_id):
        # Trong thực tế, hàm này sẽ truy vấn cơ sở dữ liệu để lấy thông tin phòng
        try:
            from QLNHATRO.RentalManagementApplication.services.TenantService import TenantService
            return TenantService.get_room_id_by_tenant(tenant_id)
        except Exception:
            # Trường hợp không kết nối được, trả về giá trị mặc định
            return "N/A"