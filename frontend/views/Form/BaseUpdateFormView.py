from PyQt5.QtWidgets import QVBoxLayout, QWidget
from QLNHATRO.RentalManagementApplication.frontend.Component.DateTableUI import DateTableUI
from QLNHATRO.RentalManagementApplication.frontend.Component.GenderComboUI import GenderComboUI
from QLNHATRO.RentalManagementApplication.frontend.Component.InputFieldUI import FormSection, InputFieldUI
from QLNHATRO.RentalManagementApplication.frontend.Component.MaritalComboUI import MaritalComboUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class BaseUpdateFormView(QWidget):
    def __init__(self, role):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
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
        # Just collect the data from UI fields
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

    def set_form_data(self, data):
        """Set form data from model"""
        if "name" in data:
            self.input_name.input_widget.setText(data["name"])
        # Similarly set other fields