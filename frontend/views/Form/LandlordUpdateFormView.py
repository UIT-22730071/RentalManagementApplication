from QLNHATRO.RentalManagementApplication.frontend.views.Form.BaseUpdateFormView import BaseUpdateFormView

class LandlordUpdateFormView(BaseUpdateFormView):
    def __init__(self, user_id=None):
        super().__init__("Chủ trọ", user_id)
        self.add_landlord_specific_fields()

    def add_landlord_specific_fields(self):
        self.input_property_count = self.create_input_field("🏠", "SL phòng quản lý:")
        self.input_rental_price = self.create_input_field("💵", "Giá cho thuê TB:")
        self.role_section.add_field(self.input_property_count)
        self.role_section.add_field(self.input_rental_price)
        self.main_layout.addWidget(self.role_section)

    def get_form_data(self):
        data = super().get_form_data()
        data["property_count"] = self.input_property_count.input_widget.text()
        data["rental_price"] = self.input_rental_price.input_widget.text()
        return data

    def set_form_data(self, data):
        super().set_form_data(data)
        self.input_property_count.input_widget.setText(data.get("property_count", ""))
        self.input_rental_price.input_widget.setText(data.get("rental_price", ""))
