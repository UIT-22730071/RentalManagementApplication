import sys
import os

from QLNHATRO.RentalManagementApplication.frontend.Component.ConfirmDialog import ConfirmDialog
from QLNHATRO.RentalManagementApplication.frontend.Component.ErrorDialog import ErrorDialog

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout,
                             QFrame, QWidget, QScrollArea, QLabel, QApplication)


from QLNHATRO.RentalManagementApplication.Repository.LandlordRepository import LanlordRepository
from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Form.LandlordUpdateFormView import LandlordUpdateFormView
from QLNHATRO.RentalManagementApplication.frontend.views.Form.TenantUpdateFormView import TenantUpdateFormView


class OptimizedUpdateInfoView(QWidget):
    def __init__(self, role, username, user_id, save_callback=None, cancel_callback=None):
        super().__init__()
        self.role = role
        self.user_id = user_id
        self.username = username
        self.save_callback = save_callback or self.default_save_callback
        self.cancel_callback = cancel_callback or self.default_cancel_callback

        # Set up window properties for standalone display
        self.setWindowTitle("Hoàn thiện thông tin đăng ký")
        self.setFixedSize(GlobalStyle.WINDOW_WIDTH, GlobalStyle.WINDOW_HEIGHT)

        # Apply global stylesheet as base
        self.setStyleSheet(GlobalStyle.global_stylesheet())

        # Center the window on screen
        self.center_on_screen()

        self.initUI()

    def center_on_screen(self):
        """Center the window on the screen"""
        screen = QApplication.desktop().screenGeometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) // 2,
            (screen.height() - size.height()) // 2
        )

    def initUI(self):
        # Main container with gradient background using GlobalStyle colors
        main_container = QFrame(self)
        main_container.setGeometry(0, 0, GlobalStyle.WINDOW_WIDTH, GlobalStyle.WINDOW_HEIGHT)
        main_container.setStyleSheet(f"""
            QFrame {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {GlobalStyle.PRIMARY_COLOR}, 
                    stop:1 {GlobalStyle.BUTTON_SPECIAL_COLOR});
                border: none;
            }}
        """)

        # Content layout with proper margins
        main_layout = QVBoxLayout(main_container)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        # Create main content card using GlobalStyle
        content_card = QFrame()
        content_card.setObjectName("InfoCard")  # Use GlobalStyle's InfoCard
        content_card.setStyleSheet(f"""
            QFrame#InfoCard {{
                background-color: {GlobalStyle.MAIN_BG};
                border-radius: 15px;
                border: none;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            }}
        """)

        card_layout = QVBoxLayout(content_card)
        card_layout.setContentsMargins(0, 0, 0, 0)
        card_layout.setSpacing(0)

        # Header section
        header_section = self.create_header_section()
        card_layout.addWidget(header_section)

        # Separator using GlobalStyle
        separator = QFrame()
        separator.setObjectName("separator")
        separator.setFrameShape(QFrame.HLine)
        card_layout.addWidget(separator)

        # Form section with scroll
        form_section = self.create_form_section()
        card_layout.addWidget(form_section, 1)

        # Button section
        button_section = self.create_button_section()
        card_layout.addWidget(button_section)

        # Add content card to main layout
        main_layout.addWidget(content_card)

    def create_header_section(self):
        """Create header section using GlobalStyle"""
        header_frame = QFrame()
        header_frame.setStyleSheet(f"""
            QFrame {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {GlobalStyle.PRIMARY_COLOR}, 
                    stop:1 {GlobalStyle.BUTTON_SPECIAL_COLOR});
                border-top-left-radius: 15px;
                border-top-right-radius: 15px;
                border: none;
            }}
        """)
        header_frame.setFixedHeight(120)

        header_layout = QVBoxLayout(header_frame)
        header_layout.setContentsMargins(30, 20, 30, 20)
        header_layout.setSpacing(8)

        # Main title using GlobalStyle font
        title_label = QLabel("🏠 Hoàn thiện thông tin đăng ký")
        title_label.setStyleSheet(f"""
            QLabel {{
                color: {GlobalStyle.LABEL_TEXT_COLOR};
                font-size: {GlobalStyle.TITLE_FONT_SIZE};
                font-family: {GlobalStyle.FONT_FAMILY};
                font-weight: 700;
                border: none;
                background: transparent;
            }}
        """)
        #title_label.setFixedHeight(120)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Subtitle with role info
        role_display = "Người thuê trọ" if self.role == "tenant" else "Chủ trọ"
        subtitle_label = QLabel(f"✨ Vai trò: {role_display}")
        subtitle_label.setStyleSheet(f"""
            QLabel {{
                color: rgba(255, 255, 255, 0.9);
                font-size: {GlobalStyle.LABEL_FONT_SIZE};
                font-family: {GlobalStyle.FONT_FAMILY};
                font-weight: 400;
                border: none;
                background: transparent;
            }}
        """)
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # User info
        user_info = QLabel(f"👤 Tài khoản: {self.username}")
        user_info.setStyleSheet(f"""
            QLabel {{
                color: rgba(255, 255, 255, 0.8);
                font-size: 14px;
                font-family: {GlobalStyle.FONT_FAMILY};
                font-weight: 400;
                border: none;
                background: transparent;
            }}
        """)
        user_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        header_layout.addWidget(title_label)
        header_layout.addWidget(subtitle_label)
        header_layout.addWidget(user_info)

        return header_frame

    def create_form_section(self):
        """Create scrollable form section with GlobalStyle"""
        # Scroll area using GlobalStyle
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet(f"""
            QScrollArea {{
                border: none;
                background-color: transparent;
            }}
            QScrollBar:vertical {{
                background-color: {GlobalStyle.TABLE_HEADER_BG};
                width: 12px;
                border-radius: 6px;
            }}
            QScrollBar::handle:vertical {{
                background-color: {GlobalStyle.PRIMARY_COLOR};
                border-radius: 6px;
                min-height: 20px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: #1D4DA5;
            }}
        """)

        # Form container
        form_container = QWidget()
        form_container.setStyleSheet("background-color: transparent;")

        form_layout = QVBoxLayout(form_container)
        form_layout.setContentsMargins(30, 25, 30, 25)
        form_layout.setSpacing(0)

        # Create form based on role
        if self.role == "tenant":
            self.form = TenantUpdateFormView(self.user_id)
        else:
            self.form = LandlordUpdateFormView(self.user_id)

        # Apply GlobalStyle to form
        self.form.setStyleSheet(GlobalStyle.global_stylesheet())

        # Additional styling for form sections
        self.style_form_sections()

        form_layout.addWidget(self.form)
        scroll.setWidget(form_container)

        return scroll

    def style_form_sections(self):
        """Apply GlobalStyle-based styling to form sections"""
        # Use GlobalStyle colors for form sections
        section_style = f"""
            FormSection {{
                background-color: {GlobalStyle.TABLE_HEADER_BG};
                border: 1px solid #E9ECEF;
                border-radius: 10px;
                margin-bottom: 15px;
                padding: 15px;
            }}
            QLabel {{
                color: {GlobalStyle.TEXT_COLOR};
                font-family: {GlobalStyle.FONT_FAMILY};
                font-weight: 600;
            }}
        """

        # Apply to different sections if they exist
        if hasattr(self.form, 'personal_section'):
            self.form.personal_section.setStyleSheet(section_style)

        if hasattr(self.form, 'contact_section'):
            self.form.contact_section.setStyleSheet(section_style)

        if hasattr(self.form, 'role_section'):
            special_section_style = f"""
                FormSection {{
                    background-color: #FFF3E0;
                    border: 1px solid {GlobalStyle.PRIMARY_COLOR};
                    border-radius: 10px;
                    margin-bottom: 15px;
                    padding: 15px;
                }}
                QLabel {{
                    color: {GlobalStyle.TEXT_COLOR};
                    font-family: {GlobalStyle.FONT_FAMILY};
                }}
            """
            self.form.role_section.setStyleSheet(special_section_style)

    def create_button_section(self):
        """Create button section using GlobalStyle"""
        button_frame = QFrame()
        button_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {GlobalStyle.TABLE_HEADER_BG};
                border-bottom-left-radius: 15px;
                border-bottom-right-radius: 15px;
                border: none;
            }}
        """)
        button_frame.setFixedHeight(80)

        button_layout = QHBoxLayout(button_frame)
        button_layout.setContentsMargins(40, 20, 40, 20)
        button_layout.setSpacing(20)

        # Cancel button using GlobalStyle CancelBtn
        self.btn_cancel = QPushButton("❌ Hủy đăng ký")
        self.btn_cancel.setObjectName("CancelBtn")
        self.btn_cancel.setFixedHeight(40)
        self.btn_cancel.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_cancel.clicked.connect(self.handle_cancel_clicked)

        # Save button using GlobalStyle primary button
        self.btn_save = QPushButton("✅ Hoàn tất đăng ký")
        self.btn_save.setFixedHeight(40)
        # Add some custom styling to make it more prominent
        self.btn_save.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {GlobalStyle.PRIMARY_COLOR}, 
                    stop:1 {GlobalStyle.BUTTON_SPECIAL_COLOR});
                color: {GlobalStyle.LABEL_TEXT_COLOR};
                border: none;
                border-radius: 9px;
                font-size: 14px;
                font-weight: 600;
                font-family: {GlobalStyle.FONT_FAMILY};
                padding: 12px 38px;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1D4DA5, stop:1 #1E40AF);
                transform: translateY(-1px);
            }}
            QPushButton:pressed {{
                background-color: #1D4DA5;
            }}
        """)
        self.btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_save.clicked.connect(self.handle_save_clicked)

        button_layout.addWidget(self.btn_cancel)
        button_layout.addStretch()
        button_layout.addWidget(self.btn_save)

        return button_frame

    def handle_save_clicked(self):
        """Handle save button click with validation"""
        if not self.form.validate():
            # Create styled message box
            msg = QMessageBox(self)
            msg.setWindowTitle("Thông tin chưa đầy đủ")
            msg.setText("Vui lòng điền đầy đủ các thông tin bắt buộc:")
            msg.setDetailedText("• Họ và tên\n• CCCD\n• Số điện thoại\n• Email")
            msg.setIcon(QMessageBox.Warning)
            msg.setStyleSheet(GlobalStyle.global_stylesheet())
            msg.exec_()
            return

        # Show success message
        msg = QMessageBox(self)
        msg.setWindowTitle("Đăng ký thành công")
        msg.setText("Thông tin đã được cập nhật thành công!\nBạn có thể bắt đầu sử dụng ứng dụng.")
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet(GlobalStyle.global_stylesheet())

        reply = msg.exec_()
        if reply == QMessageBox.Ok:
            self.save_callback()

    def handle_cancel_clicked(self):
        """Xử lý khi bấm nút Hủy với xác nhận"""
        if ConfirmDialog.ask(self, "⚠️ Bạn có chắc chắn muốn hủy đăng ký?\nTất cả thông tin đã nhập sẽ bị mất và bạn sẽ cần đăng ký lại."):
            self.cancel_callback()

    def save_to_repository(self, user_id):
        """Save form data to repository"""
        try:
            data = self.form.get_form_data()
            if self.role == "tenant":
                TenantRepository.update_user_info(user_id, data)
            else:
                LanlordRepository.update_user_info(user_id, data)
            return True
        except Exception as e:
            ErrorDialog.show_error(f"Không thể lưu thông tin:\n{str(e)}", self)
            return False

    def get_form_data(self):
        """Get form data"""
        return self.form.get_form_data()

    def set_form_data(self, data):
        """Set form data"""
        self.form.set_form_data(data)

    def default_save_callback(self):
        """Default save callback"""
        print("Form saved successfully!")
        self.close()

    def default_cancel_callback(self):
        """Default cancel callback"""
        print("Registration cancelled!")
        self.close()

    def closeEvent(self, event):
        """Xác nhận khi đóng cửa sổ nếu có dữ liệu chưa lưu"""
        if hasattr(self, 'form'):
            data = self.form.get_form_data()
            has_data = any(str(value).strip() for value in data.values() if value)
            if has_data:
                confirm = ConfirmDialog.ask(self, "Bạn có chắc chắn muốn đóng? Dữ liệu chưa lưu sẽ bị mất.")
                if not confirm:
                    event.ignore()
                    return
        event.accept()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Set application-wide font from GlobalStyle
    from PyQt5.QtGui import QFont

    font = QFont()
    font.setFamily("Be Vietnam Pro")
    app.setFont(font)

    # Create test window
    window = OptimizedUpdateInfoView(
        role="landlord",  # Fixed typo: "lanlord" -> "landlord"
        username="hoangphuc1235",
        user_id=1
    )

    window.show()
    window.activateWindow()

    sys.exit(app.exec_())