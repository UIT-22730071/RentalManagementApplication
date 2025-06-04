from QLNHATRO.RentalManagementApplication.frontend.views.Form.BaseUpdateFormView import BaseUpdateFormView

class TenantUpdateFormView(BaseUpdateFormView):
    def __init__(self, user_id=None):
        super().__init__("Người thuê trọ", user_id)
        self.add_tenant_specific_fields()

    def add_tenant_specific_fields(self):
        self.input_income = self.create_input_field("💰", "Thu nhập hàng tháng:")
        self.role_section.add_field(self.input_income)
        self.main_layout.addWidget(self.role_section)

    def get_form_data(self):
        data = super().get_form_data()
        data["income"] = self.input_income.input_widget.text()
        return data

    def set_form_data(self, data):
        super().set_form_data(data)
        self.input_income.input_widget.setText(data.get("income", ""))