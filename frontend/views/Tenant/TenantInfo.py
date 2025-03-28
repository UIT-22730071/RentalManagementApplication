from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from QLNHATRO.RentalManagementApplication.frontend.Component.FormInforUI import FormInforUI

class TenantInfo(QWidget):
    tenant_info_updated = pyqtSignal(dict)

    def __init__(self, main_window, initial_data=None):
        super().__init__()

        # Field configurations
        field_configs = [
            {"name": "Ho_ten", "key": "full_name", "icon": "👤"},
            {"name": "Ngày Sinh", "key": "birth_date", "icon": "📅"},
            {"name": "CCCD", "key": "citizen_id", "icon": "🆔"},
            {"name": "Giới tính", "key": "gender", "icon": "⚧"},
            {"name": "Nghề nghiệp", "key": "occupation", "icon": "💼"},
            {"name": "Số điện thoại", "key": "phone_number", "icon": "📞"},
            {"name": "Tình trạng hôn nhân", "key": "marital_status", "icon": "💍"},
            {"name": "Ngày Đăng Ký", "key": "registration_date", "icon": "📝"}
        ]

        # Default initial data
        default_data = {
            'full_name': '',
            'birth_date': '',
            'citizen_id': '',
            'gender': '',
            'occupation': '',
            'phone_number': '',
            'marital_status': '',
            'registration_date': ''
        }

        # Merge provided initial data with default
        if initial_data:
            default_data.update(initial_data)

        # Create form UI
        self.form_ui = FormInforUI(
            title="👥 THÔNG TIN KHÁCH THUÊ",
            initial_data=default_data,
            field_configs=field_configs
        )

        # Connect signals
        self.form_ui.info_updated.connect(self.on_tenant_info_updated)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.form_ui)
        self.setLayout(layout)

    def on_tenant_info_updated(self, updated_data):
        # Emit signal to parent/main window
        self.tenant_info_updated.emit(updated_data)

    def load_tenant_data(self, data=None):
        # Delegate to form UI's load method
        self.form_ui.load_data(data)