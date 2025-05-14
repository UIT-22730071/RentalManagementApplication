from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Form.BaseUpdateFormView import BaseUpdateFormView


class LandlordUpdateFormView(BaseUpdateFormView):
    def __init__(self):
        super().__init__("Chủ trọ")
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.add_landlord_specific_fields()

    def add_landlord_specific_fields(self):
        # Create landlord-specific fields
        self.input_property_count = self.create_input_field("🏘️", "SL phòng quản lý:")
        self.input_rental_price = self.create_input_field("💵", "Giá cho thuê TB:")

        # Add to role section
        self.role_section.add_field(self.input_property_count)
        self.role_section.add_field(self.input_rental_price)

        # Add role section to main layout
        self.main_layout.addWidget(self.role_section)

    def get_form_data(self):
        # Get base data
        data = super().get_form_data()

        # Add landlord-specific data
        data["property_count"] = self.input_property_count.input_widget.text()
        data["rental_price"] = self.input_rental_price.input_widget.text()
        return data

    def set_form_data(self, data):
        super().set_form_data(data)
        if "property_count" in data:
            self.input_property_count.input_widget.setText(data["property_count"])
        if "rental_price" in data:
            self.input_rental_price.input_widget.setText(data["rental_price"])