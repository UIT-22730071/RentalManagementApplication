from QLNHATRO.RentalManagementApplication.frontend.views.Form.BaseUpdateFormView import BaseUpdateFormView


class TenantUpdateFormView(BaseUpdateFormView):
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

        # Add tenant-specific data
        data["income"] = self.input_income.input_widget.text()
        return data

    def set_form_data(self, data):
        super().set_form_data(data)
        if "income" in data:
            self.input_income.input_widget.setText(data["income"])