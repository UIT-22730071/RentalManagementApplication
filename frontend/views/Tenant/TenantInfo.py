from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from QLNHATRO.RentalManagementApplication.frontend.Component.FormInforUI import FormInforUI



class TenantInfo(QWidget):
    tenant_info_updated = pyqtSignal(dict)

    def __init__(self, main_window, initial_data=None, tenant_id=None):
        super().__init__()
        self.main_window = main_window
        self.tenant_id = tenant_id
        # Field configurations
        field_configs = [
            {"name": "Ho_ten", "key": "full_name", "icon": "👤"},
            {"name": "Ngày Sinh", "key": "birth_date", "icon": "📅"},
            {"name": "CCCD", "key": "citizen_id", "icon": "🆔"},
            {"name": "Giới tính", "key": "gender", "icon": "⚧"},
            {"name": "Nghề nghiệp", "key": "occupation", "icon": "💼"},
            {"name": "Số điện thoại", "key": "phone_number", "icon": "📞"},
            {"name": "Tình trạng hôn nhân", "key": "marital_status", "icon": "💍"},
        ]

        # Default initial data
        default_data = {
            'full_name': '',
            'birth_date': '',
            'citizen_id': '',
            'gender': '',
            'occupation': '',
            'phone_number': '',
            'marital_status': ''
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

    def on_tenant_info_updated(self, update_payload):
        # Gửi về controller hoặc gọi service để cập nhật DB
        updated_key = update_payload["updated_key"]
        new_value = update_payload["new_value"]
        full_data = update_payload["full_data"]
        from QLNHATRO.RentalManagementApplication.services.TenantService import TenantService
        if self.tenant_id:
            success = TenantService.update_tenant_info(self.tenant_id, full_data)
            if success:
                print("✅ Dữ liệu người thuê đã được cập nhật thành công!")
            else:
                print("❌ Cập nhật thất bại.")
        else:
            print("⚠ Không có tenant_id để cập nhật!")

        self.tenant_info_updated.emit(full_data)

    def load_tenant_data(self, data=None):
        # Delegate to form UI's load method
        self.form_ui.load_data(data)