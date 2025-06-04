from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit

from QLNHATRO.RentalManagementApplication.frontend.Component.DateTableUI import DateTableUI
from QLNHATRO.RentalManagementApplication.frontend.Component.GenderComboUI import GenderComboUI
from QLNHATRO.RentalManagementApplication.frontend.Component.InputFieldUI import FormSection, InputFieldUI
from QLNHATRO.RentalManagementApplication.frontend.Component.MaritalComboUI import MaritalComboUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class BaseUpdateFormView(QWidget):
    def __init__(self, role, user_id=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.role = role
        self.user_id = user_id
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(20)

        # Sections
        self.personal_section = FormSection("📋 Thông tin cá nhân")
        self.contact_section = FormSection("📱 Thông tin liên hệ")
        self.role_section = FormSection(f"🏠 Thông tin {self.role}")

        # Personal fields
        self.input_name = self.create_input_field("👤", "Họ và Tên:")
        self.input_birthdate = self.create_date_field("📅", "Ngày Sinh:")
        self.input_id_card = self.create_input_field("🆔", "CCCD:")
        self.input_gender = self.create_gender_field("⚧", "Giới tính:")
        self.input_job = self.create_input_field("💼", "Nghề nghiệp:")
        self.input_marital = self.create_marital_field("💍", "Tình trạng hôn nhân:")

        # Contact fields
        self.input_phone = self.create_input_field("📞", "Số điện thoại:")
        self.input_email = self.create_input_field("📧", "Email:")
        self.input_address = self.create_input_field("🏡", "Địa chỉ thường trú:")

        # Add to sections
        for field in [self.input_name, self.input_birthdate, self.input_id_card,
                      self.input_gender, self.input_job, self.input_marital]:
            self.personal_section.add_field(field)

        for field in [self.input_phone, self.input_email, self.input_address]:
            self.contact_section.add_field(field)

        # Add to main layout
        self.main_layout.addWidget(self.personal_section)
        self.main_layout.addWidget(self.contact_section)

    def create_input_field(self, icon, label):
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
        return {
            "name": self.input_name.input_widget.text(),
            "birthdate": self.input_birthdate.input_widget.date().toString("dd/MM/yyyy"),
            "id_card": self.input_id_card.input_widget.text(),
            "gender": self.input_gender.input_widget.currentText(),
            "job": self.input_job.input_widget.text(),
            "marital_status": self.input_marital.input_widget.currentText(),
            "phone": self.input_phone.input_widget.text(),
            "email": self.input_email.input_widget.text(),
            "address": self.input_address.input_widget.text()
        }

    def set_form_data(self, data):
        self.input_name.input_widget.setText(data.get("name", ""))
        self.input_id_card.input_widget.setText(data.get("id_card", ""))
        self.input_job.input_widget.setText(data.get("job", ""))
        self.input_phone.input_widget.setText(data.get("phone", ""))
        self.input_email.input_widget.setText(data.get("email", ""))
        self.input_address.input_widget.setText(data.get("address", ""))

    def validate(self):
        return all([
            self.input_name.input_widget.text().strip(),
            self.input_id_card.input_widget.text().strip(),
            self.input_phone.input_widget.text().strip(),
            self.input_email.input_widget.text().strip()
        ])
