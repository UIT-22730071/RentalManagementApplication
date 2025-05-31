from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton,
    QScrollArea, QTextEdit, QGridLayout, QGroupBox, QMessageBox,
    QComboBox, QDateEdit, QLineEdit
)
from PyQt5.QtCore import Qt, QDate, pyqtSignal
from PyQt5.QtGui import QPixmap, QFont
import os
from datetime import datetime

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.Component.ConfirmDialog import ConfirmDialog
from QLNHATRO.RentalManagementApplication.frontend.Component.SuccessDialog import SuccessDialog


class MaintenanceRequestDetail(QWidget):
    """
    Widget hiển thị chi tiết yêu cầu bảo trì với giao diện đẹp và đầy đủ tính năng
    """
    # Signal để thông báo khi có thay đổi trạng thái
    status_updated = pyqtSignal(int, str)  # request_id, new_status

    def __init__(self, request_data, parent=None):
        super().__init__(parent)
        self.request_data = request_data
        self.setWindowTitle(f"Chi tiết yêu cầu bảo trì - {request_data.get('room_name', 'N/A')}")
        self.resize(GlobalStyle.WINDOW_WIDTH - 300, GlobalStyle.WINDOW_HEIGHT - 100)
        self.setMinimumSize(800, 600)
        self.setStyleSheet(GlobalStyle.global_stylesheet())

        self.setup_ui()
        self.populate_data()

    def setup_ui(self):
        """Thiết lập giao diện"""
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        # Tiêu đề
        self.create_header(main_layout)

        # Scroll area cho nội dung chính
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Widget chứa nội dung
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(15)

        # Các section thông tin
        self.create_basic_info_section(content_layout)
        self.create_issue_details_section(content_layout)
        self.create_contact_info_section(content_layout)
        self.create_image_section(content_layout)
        self.create_status_management_section(content_layout)
        self.create_notes_section(content_layout)

        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

        # Nút điều khiển
        self.create_action_buttons(main_layout)

        self.setLayout(main_layout)

    def create_header(self, layout):
        """Tạo header với thông tin tổng quan"""
        header_frame = QFrame()
        header_frame.setObjectName("tableCard")
        header_layout = QVBoxLayout(header_frame)
        header_layout.setContentsMargins(20, 15, 20, 15)

        # Tiêu đề chính
        title = QLabel("🔧 CHI TIẾT YÊU CẦU BẢO TRÌ")
        title.setObjectName("Title")
        title.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title)

        # Thông tin cơ bản
        info_layout = QHBoxLayout()

        # Thông tin phòng
        room_info = QLabel(f"📍 Phòng: {self.request_data.get('room_name', 'N/A')}")
        room_info.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: 600;
                color: #2c3e50;
                padding: 8px 12px;
                background-color: #ecf0f1;
                border-radius: 8px;
            }
        """)
        info_layout.addWidget(room_info)

        # Trạng thái hiện tại
        status = self.request_data.get('status', 'N/A')
        status_color = self.get_status_color(status)
        status_label = QLabel(f"📊 Trạng thái: {status}")
        status_label.setStyleSheet(f"""
            QLabel {{
                font-size: 16px;
                font-weight: 600;
                color: white;
                padding: 8px 12px;
                background-color: {status_color};
                border-radius: 8px;
            }}
        """)
        info_layout.addWidget(status_label)

        # Mức độ khẩn cấp
        urgency = self.request_data.get('urgency_level', 'N/A')
        urgency_color = "#e74c3c" if urgency == "Khẩn cấp" else "#f39c12"
        urgency_label = QLabel(f"🚨 Mức độ: {urgency}")
        urgency_label.setStyleSheet(f"""
            QLabel {{
                font-size: 16px;
                font-weight: 600;
                color: white;
                padding: 8px 12px;
                background-color: {urgency_color};
                border-radius: 8px;
            }}
        """)
        info_layout.addWidget(urgency_label)

        header_layout.addLayout(info_layout)
        layout.addWidget(header_frame)

    def create_basic_info_section(self, layout):
        """Tạo section thông tin cơ bản"""
        group_box = QGroupBox("📋 Thông tin cơ bản")
        group_box.setProperty("theme", "blue")
        group_layout = QGridLayout(group_box)
        group_layout.setSpacing(10)

        # Các thông tin cơ bản
        basic_info = [
            ("Mã yêu cầu:", self.request_data.get('request_id', 'N/A')),
            ("Người thuê:", self.request_data.get('tenant_name', 'N/A')),
            ("Ngày tạo:", self.request_data.get('created_at', 'N/A')),
            ("Loại sự cố:", self.request_data.get('issue_type', 'N/A'))
        ]

        for i, (label_text, value) in enumerate(basic_info):
            row = i // 2
            col = (i % 2) * 2

            label = QLabel(label_text)
            label.setObjectName("keyLabel")
            group_layout.addWidget(label, row, col)

            value_label = QLabel(str(value))
            value_label.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    color: #2c3e50;
                    padding: 6px 8px;
                    background-color: #f8f9fa;
                    border-radius: 4px;
                    border: 1px solid #dee2e6;
                }
            """)
            group_layout.addWidget(value_label, row, col + 1)

        layout.addWidget(group_box)

    def create_issue_details_section(self, layout):
        """Tạo section chi tiết sự cố"""
        group_box = QGroupBox("📝 Chi tiết sự cố")
        group_box.setProperty("theme", "blue")
        group_box.setFixedHeight(150)
        group_layout = QVBoxLayout(group_box)

        # Mô tả chi tiết
        self.description_display = QTextEdit()
        self.description_display.setReadOnly(True)
        self.description_display.setMinimumHeight(120)
        '''
        self.description_display.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
                line-height: 1.5;
            }
        """)
        '''
        group_layout.addWidget(self.description_display)

        layout.addWidget(group_box)

    def create_contact_info_section(self, layout):
        """Tạo section thông tin liên hệ"""
        group_box = QGroupBox("📞 Thông tin liên hệ")
        group_box.setProperty("theme", "blue")
        group_layout = QGridLayout(group_box)

        # Số điện thoại
        phone_label = QLabel("Số điện thoại:")
        phone_label.setObjectName("keyLabel")
        group_layout.addWidget(phone_label, 0, 0)

        phone_value = QLabel(self.request_data.get('contact_phone', 'Chưa cập nhật'))
        phone_value.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #2c3e50;
                padding: 6px 8px;
                background-color: #f8f9fa;
                border-radius: 4px;
                border: 1px solid #dee2e6;
            }
        """)
        group_layout.addWidget(phone_value, 0, 1)

        # Thời gian thuận tiện liên hệ (nếu có)
        if 'available_time' in self.request_data:
            time_label = QLabel("Thời gian thuận tiện:")
            time_label.setObjectName("keyLabel")
            group_layout.addWidget(time_label, 1, 0)

            time_value = QLabel(self.request_data.get('available_time', 'Không xác định'))
            time_value.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    color: #2c3e50;
                    padding: 6px 8px;
                    background-color: #f8f9fa;
                    border-radius: 4px;
                    border: 1px solid #dee2e6;
                }
            """)
            group_layout.addWidget(time_value, 1, 1)

        layout.addWidget(group_box)

    def create_image_section(self, layout):
        """Tạo section hiển thị hình ảnh"""
        group_box = QGroupBox("📷 Hình ảnh minh họa")
        group_box.setProperty("theme", "blue")
        group_layout = QVBoxLayout(group_box)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumHeight(200)
        self.image_label.setStyleSheet("""
            QLabel {
                border: 2px dashed #bdc3c7;
                border-radius: 8px;
                background-color: #f8f9fa;
                color: #7f8c8d;
                font-size: 14px;
            }
        """)

        # Kiểm tra và hiển thị hình ảnh
        image_path = self.request_data.get('image_path', '')
        if image_path and os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                # Scale ảnh để vừa với label
                scaled_pixmap = pixmap.scaled(
                    400, 200,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                self.image_label.setPixmap(scaled_pixmap)
            else:
                self.image_label.setText("⚠️ Không thể tải hình ảnh")
        else:
            self.image_label.setText("📷 Không có hình ảnh minh họa")

        group_layout.addWidget(self.image_label)
        layout.addWidget(group_box)

    def create_status_management_section(self, layout):
        """Tạo section quản lý trạng thái"""
        group_box = QGroupBox("⚙️ Quản lý trạng thái")
        group_box.setProperty("theme", "blue")
        group_layout = QVBoxLayout(group_box)

        # Combo box chọn trạng thái mới
        status_layout = QHBoxLayout()

        status_label = QLabel("Cập nhật trạng thái:")
        status_label.setObjectName("keyLabel")
        status_layout.addWidget(status_label)

        self.status_combo = QComboBox()
        self.status_combo.addItems([
            "Pending",
            "Đang xử lý",
            "Chờ phụ tùng",
            "Hoàn thành",
            "Hủy bỏ"
        ])

        # Set trạng thái hiện tại
        current_status = self.request_data.get('status', 'Pending')
        if current_status in [self.status_combo.itemText(i) for i in range(self.status_combo.count())]:
            self.status_combo.setCurrentText(current_status)

        status_layout.addWidget(self.status_combo)

        # Nút cập nhật trạng thái
        self.update_status_btn = QPushButton("🔄 Cập nhật trạng thái")
        self.update_status_btn.clicked.connect(self.update_status)
        status_layout.addWidget(self.update_status_btn)

        status_layout.addStretch()
        group_layout.addLayout(status_layout)

        layout.addWidget(group_box)

    def create_notes_section(self, layout):
        """Tạo section ghi chú của quản lý"""
        group_box = QGroupBox("📋 Ghi chú quản lý")
        group_box.setProperty("theme", "blue")
        group_box.setFixedHeight(220)
        group_layout = QVBoxLayout(group_box)

        self.notes_edit = QTextEdit()
        self.notes_edit.setPlaceholderText(
            "Ghi chú của quản lý về quá trình xử lý yêu cầu...\n"
            "- Nguyên nhân sự cố\n"
            "- Cách khắc phục\n"
            "- Chi phí ước tính\n"
            "- Thời gian hoàn thành dự kiến"
        )
        self.notes_edit.setMinimumHeight(100)
        self.notes_edit.setText(self.request_data.get('admin_notes', ''))

        group_layout.addWidget(self.notes_edit)

        # Nút lưu ghi chú
        save_notes_btn = QPushButton("💾 Lưu ghi chú")
        save_notes_btn.clicked.connect(self.save_notes)
        group_layout.addWidget(save_notes_btn)

        layout.addWidget(group_box)

    def create_action_buttons(self, layout):
        """Tạo các nút hành động"""
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        # Nút in báo cáo
        print_btn = QPushButton("🖨️ In báo cáo")
        print_btn.clicked.connect(self.print_report)
        btn_layout.addWidget(print_btn)

        # Nút đóng
        close_btn = QPushButton("❌ Đóng")
        close_btn.setObjectName("CancelBtn")
        close_btn.clicked.connect(self.close)
        btn_layout.addWidget(close_btn)

        layout.addLayout(btn_layout)

    def populate_data(self):
        """Điền dữ liệu vào các widget"""
        # Điền mô tả chi tiết
        description = self.request_data.get('description', 'Không có mô tả chi tiết')
        self.description_display.setText(description)

    def get_status_color(self, status):
        """Lấy màu tương ứng với trạng thái"""
        status_colors = {
            'Pending': '#e74c3c',
            'Đang xử lý': '#f39c12',
            'Chờ phụ tùng': '#9b59b6',
            'Hoàn thành': '#27ae60',
            'Hủy bỏ': '#95a5a6'
        }
        return status_colors.get(status, '#34495e')

    def update_status(self):
        """Cập nhật trạng thái yêu cầu"""
        new_status = self.status_combo.currentText()
        current_status = self.request_data.get('status', '')

        if new_status == current_status:
            QMessageBox.information(self, "Thông báo", "Trạng thái không thay đổi!")
            return

        # Xác nhận thay đổi
        confirmed = ConfirmDialog.ask(
            self,
            f"Bạn có chắc chắn muốn thay đổi trạng thái từ '{current_status}' thành '{new_status}'?"
        )

        if confirmed == QMessageBox.Yes:
            try:
                # Cập nhật trạng thái trong data
                self.request_data['status'] = new_status

                # Emit signal để thông báo cho parent widget
                self.status_updated.emit(
                    self.request_data.get('request_id', 0),
                    new_status
                )

                # Hiển thị thông báo thành công
                SuccessDialog.show(
                    self,
                    f"Đã cập nhật trạng thái thành '{new_status}' thành công!"
                )

                # Cập nhật lại header để reflect trạng thái mới
                self.refresh_header()

                # TODO: Gọi service để cập nhật database
                # MaintenanceService.update_status(request_id, new_status)

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Lỗi",
                    f"Không thể cập nhật trạng thái: {str(e)}"
                )

    def save_notes(self):
        """Lưu ghi chú quản lý"""
        notes = self.notes_edit.toPlainText().strip()

        try:
            # Cập nhật ghi chú trong data
            self.request_data['admin_notes'] = notes

            QMessageBox.information(self, "Thành công", "Đã lưu ghi chú thành công!")

            # TODO: Gọi service để lưu ghi chú vào database
            # MaintenanceService.update_notes(request_id, notes)

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể lưu ghi chú: {str(e)}")

    def print_report(self):
        """In báo cáo chi tiết yêu cầu bảo trì"""
        try:
            # Tạo nội dung báo cáo
            report_content = self.generate_report_content()

            # TODO: Implement chức năng in thực tế
            QMessageBox.information(
                self,
                "In báo cáo",
                "Chức năng in báo cáo sẽ được triển khai trong phiên bản tiếp theo."
            )

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể in báo cáo: {str(e)}")

    def generate_report_content(self):
        """Tạo nội dung báo cáo"""
        report = f"""
        BÁO CÁO CHI TIẾT YÊU CẦU BẢO TRÌ
        =====================================

        Mã yêu cầu: {self.request_data.get('request_id', 'N/A')}
        Phòng: {self.request_data.get('room_name', 'N/A')}
        Người thuê: {self.request_data.get('tenant_name', 'N/A')}
        Ngày tạo: {self.request_data.get('created_at', 'N/A')}

        THÔNG TIN SỰ CỐ
        ---------------
        Loại sự cố: {self.request_data.get('issue_type', 'N/A')}
        Mức độ: {self.request_data.get('urgency_level', 'N/A')}
        Trạng thái: {self.request_data.get('status', 'N/A')}

        MÔ TẢ CHI TIẾT
        --------------
        {self.request_data.get('description', 'Không có mô tả')}

        THÔNG TIN LIÊN HỆ
        ------------------
        SĐT: {self.request_data.get('contact_phone', 'N/A')}

        GHI CHÚ QUẢN LÝ
        ----------------
        {self.request_data.get('admin_notes', 'Chưa có ghi chú')}

        Ngày in: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        """
        return report

    def refresh_header(self):
        """Refresh lại header sau khi cập nhật trạng thái"""
        # TODO: Implement logic refresh header nếu cần
        pass

    def closeEvent(self, event):
        """Xử lý khi đóng cửa sổ"""
        event.accept()