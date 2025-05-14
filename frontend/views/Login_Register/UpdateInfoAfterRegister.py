from QLNHATRO.RentalManagementApplication.controller.UpdateInfor.UpdateInfoController import UpdateInfoController


class UpdateInfoAfterRegister:
    """Factory class that creates and returns the UpdateInfoController"""
    @staticmethod
    def create(main_window, role, username, password,user_id):
        controller = UpdateInfoController(main_window, role, username, password,user_id)
        controller.show()
        return controller


'''
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QMessageBox, QScrollArea, QFrame, QLabel, QHBoxLayout, QPushButton

# Thành:


from QLNHATRO.RentalManagementApplication.frontend.Component.DateTableUI import DateTableUI
from QLNHATRO.RentalManagementApplication.frontend.Component.GenderComboUI import GenderComboUI
from QLNHATRO.RentalManagementApplication.frontend.Component.InputFieldUI import FormSection, InputFieldUI
from QLNHATRO.RentalManagementApplication.frontend.Component.MaritalComboUI import MaritalComboUI


# Base form class
class BaseUpdateForm(QWidget):
    def __init__(self, role):
        super().__init__()
        self.role = role
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(20)

        # Create form sections
        self.personal_section = FormSection("📋 Thông tin cá nhân")
        self.contact_section = FormSection("📱 Thông tin liên hệ")
        self.role_section = FormSection(f"🏠 Thông tin {self.role}")

        # Add common fields
        self.input_name = self.create_input_field("👤", "Họ và Tên:")
        self.input_birthdate = self.create_date_field("📅", "Ngày Sinh:")
        self.input_id_card = self.create_input_field("🆔", "CCCD:")
        self.input_gender = self.create_gender_field("⚧", "Giới tính:")
        self.input_job = self.create_input_field("💼", "Nghề nghiệp:")
        self.input_marital = self.create_marital_field("💍", "Tình trạng hôn nhân:")

        # Add contact fields
        self.input_phone = self.create_input_field("📞", "Số điện thoại:")
        self.input_email = self.create_input_field("📧", "Email:")
        self.input_address = self.create_input_field("🏡", "Địa chỉ thường trú:")

        # Add fields to sections
        self.personal_section.add_field(self.input_name)
        self.personal_section.add_field(self.input_birthdate)
        self.personal_section.add_field(self.input_id_card)
        self.personal_section.add_field(self.input_gender)
        self.personal_section.add_field(self.input_job)
        self.personal_section.add_field(self.input_marital)

        self.contact_section.add_field(self.input_phone)
        self.contact_section.add_field(self.input_email)
        self.contact_section.add_field(self.input_address)

        # Add sections to main layout
        self.main_layout.addWidget(self.personal_section)
        self.main_layout.addWidget(self.contact_section)

        # Set style for the form
        self.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
        """)

    def create_input_field(self, icon, label):
        from PyQt5.QtWidgets import QLineEdit
        input_widget = QLineEdit()
        input_widget.setPlaceholderText(f"Nhập {label.replace(':', '')}")
        return InputFieldUI(icon, label, input_widget)


    def create_date_field(self, icon, label):
        return DateTableUI(icon, label)

    def create_gender_field(self, icon, label):
        return GenderComboUI(icon, label)

    def create_marital_field(self, icon, label):
        return MaritalComboUI(icon, label)

    def get_form_data(self):
        # Validate data - check input_name widget's input component
        if not self.input_name.input_widget.text() or not self.input_phone.input_widget.text() or not self.input_id_card.input_widget.text():
            QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ thông tin bắt buộc!")
            return None

        # Return base form data
        return {
            "name": self.input_name.input_widget.text(),
            "birthdate": self.input_birthdate.input_widget.date().toString("dd/MM/yyyy"),
            "id_card": self.input_id_card.input_widget.text(),
            "gender": self.input_gender.input_widget.currentText(),
            "job": self.input_job.input_widget.text(),
            "phone": self.input_phone.input_widget.text(),
            "marital_status": self.input_marital.input_widget.currentText(),
            "email": self.input_email.input_widget.text(),
            "address": self.input_address.input_widget.text()
        }


# Tenant update form
class TenantUpdateForm(BaseUpdateForm):
    def __init__(self):
        super().__init__("Người thuê trọ")
        self.add_tenant_specific_fields()

    def add_tenant_specific_fields(self):
        # Create tenant-specific fields
        self.input_income = self.create_input_field("💰", "Thu nhập hàng tháng:")

        # Add to role section
        self.role_section.add_field(self.input_income)

        # Add role section to main layout
        self.main_layout.addWidget(self.role_section)

    def get_form_data(self):
        # Get base data
        data = super().get_form_data()
        if not data:
            return None

        # Add tenant-specific data
        data["income"] = self.input_income.input_widget.text()

        return data


# Landlord update form
class LandlordUpdateForm(BaseUpdateForm):
    def __init__(self):
        super().__init__("Chủ trọ")
        self.add_landlord_specific_fields()

    def add_landlord_specific_fields(self):
        # Create landlord-specific fields
        self.input_property_count = self.create_input_field("🏘️", "Số lượng phòng quản lý:")
        self.input_rental_price = self.create_input_field("💵", "Giá cho thuê trung bình:")

        # Add to role section
        self.role_section.add_field(self.input_property_count)
        self.role_section.add_field(self.input_rental_price)

        # Add role section to main layout
        self.main_layout.addWidget(self.role_section)

    def get_form_data(self):
        # Get base data
        data = super().get_form_data()
        if not data:
            return None

        # Add landlord-specific data
        data["property_count"] = self.input_property_count.input_widget.text()
        data["rental_price"] = self.input_rental_price.input_widget.text()

        return data


# Main update info class
class UpdateInfoAfterRegister(QWidget):
    info_updated = pyqtSignal(dict)
    def __init__(self, main_window, role, username, password):
        super().__init__()
        self.main_window = main_window
        self.role = role
        self.username = username
        self.password = password
        self.setWindowTitle("Cập nhật thông tin")
        self.setGeometry(100, 100, 600, 700)
        self.initUI()
        print(f"[DEBUG] role={self.role}, username={self.username}, password={self.password}")
        # 🌈 Set nền gradient cho MainWindow từ bên trong form này
        self.main_window.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #FFDEE9, stop:1 #B5FFFC);
            }
        """)

    def initUI(self):
        # Create main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Thêm scroll
        scroll = QScrollArea()
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFDEE9, stop:1 #B5FFFC);
            }
        """)

        scroll.setWidgetResizable(True)

        # Create card container to hold card
        scroll_content = QWidget()
        scroll_content.setStyleSheet("""
            background-color: transparent;
        """)

        scroll.setWidget(scroll_content)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(0)

        # Create card
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #FFFFFF;
                border-radius: 12px;
            }
        """)
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(20, 20, 20, 20)
        card_layout.setSpacing(20)

        # Header
        header_layout = QVBoxLayout()

        # Main title
        title_label = QLabel("Cập nhật thông tin")
        title_label.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #FF6B6B;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Role
        role_label = QLabel(f"[{self.role}]")
        role_label.setFont(QFont("Arial", 14))
        role_label.setStyleSheet("color: #555;")
        role_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # User info
        user_info_frame = QFrame()
        user_info_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        user_info_layout = QHBoxLayout(user_info_frame)

        username_label = QLabel(f"👤 Tên đăng nhập: {self.username}")
        username_label.setFont(QFont("Arial", 10))
        username_label.setStyleSheet("color: #333;")

        password_label = QLabel("🔑 Mật khẩu: ********")
        password_label.setFont(QFont("Arial", 10))
        password_label.setStyleSheet("color: #333;")

        user_info_layout.addWidget(username_label)
        user_info_layout.addWidget(password_label)

        # Add to header layout
        header_layout.addWidget(title_label)
        header_layout.addWidget(role_label)
        header_layout.addWidget(user_info_frame)

        # Create form based on role
        if self.role == "Người thuê trọ":
            self.form = TenantUpdateForm()
        else:
            self.form = LandlordUpdateForm()

        # Create button layout
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(50, 0, 50, 0)

        # Save button
        self.btn_save = QPushButton("💾 Lưu thông tin")
        self.btn_save.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.btn_save.setStyleSheet("""
            QPushButton {
                background-color: #FF6B6B;
                color: white;
                border-radius: 20px;
                padding: 12px 20px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #ff5252;
            }
            QPushButton:pressed {
                background-color: #e04545;
            }
        """)
        self.btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_save.clicked.connect(self.save_info)

        # Cancel button
        self.btn_cancel = QPushButton("❌ Hủy")
        self.btn_cancel.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.btn_cancel.setStyleSheet("""
            QPushButton {
                background-color: #4FBEEE;
                color: white;
                border-radius: 20px;
                padding: 12px 20px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #3ba8d8;
            }
            QPushButton:pressed {
                background-color: #2b93c3;
            }
        """)
        self.btn_cancel.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_cancel.clicked.connect(self.cancel)

        # Add buttons to layout
        button_layout.addWidget(self.btn_save)
        button_layout.addWidget(self.btn_cancel)

        # Add everything to card layout
        card_layout.addLayout(header_layout)
        card_layout.addWidget(self.form)
        card_layout.addLayout(button_layout)

        # Add card to scroll layout
        scroll_layout.addWidget(card)

        # Add card to main layout
        main_layout.addWidget(scroll)

        # Set overall styling
        self.setStyleSheet("""
            QWidget {
                font-family: Arial, sans-serif;
            }
            QWidget#UpdateInfoAfterRegister {
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                                    stop:0 #FFDEE9, stop:1 #B5FFFC);}
        """)

        self.setObjectName("UpdateInfoAfterRegister")

    def save_info(self):
        # Get and validate form data
        form_data = self.form.get_form_data()
        if not form_data:
            return

        # Show success message with animation
        msg = QMessageBox(self)
        msg.setWindowTitle("Thành công")
        msg.setText("Thông tin đã được cập nhật thành công!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #f8f9fa;
            }
            QLabel {
                color: #333;
                font-size: 14px;
            }
            QPushButton {
                background-color: #4FBEEE;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: bold;
            }
        """)
        msg.exec()

        # TODO: Save data to database

        # Emit the signal with form data
        #self.info_updated.emit(form_data)

        # TODO: Switch to main workspace screen
        # self.main_window.switch_to_workspace()

    def cancel(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Xác nhận")
        msg.setText("Bạn có chắc muốn hủy cập nhật thông tin?")
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #f8f9fa;
            }
            QLabel {
                color: #333;
                font-size: 14px;
            }
            QPushButton {
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton[text="&Yes"] {
                background-color: #FF6B6B;
                color: white;
            }
            QPushButton[text="&No"] {
                background-color: #4FBEEE;
                color: white;
            }
        """)
        reply = msg.exec()

        if reply == QMessageBox.StandardButton.Yes:
            # Go back to login screen
            from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.HomeLogin import LoginWindow
            self.main_window.setCentralWidget(LoginWindow(self.main_window))


'''