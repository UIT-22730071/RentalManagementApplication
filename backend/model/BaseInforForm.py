class BaseFormModel:
    def __init__(self):
        self.user_id = ""
        self.name = ""
        self.birthdate = ""
        self.id_card = ""
        self.gender = ""
        self.job = ""
        self.phone = ""
        self.marital_status = ""
        self.email = ""
        self.address = ""

    def validate(self):
        """Validate basic form data"""
        return bool(self.name and self.phone and self.id_card)

    def to_dict(self):
        """Convert model to dictionary"""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "birthdate": self.birthdate,
            "id_card": self.id_card,
            "gender": self.gender,
            "job": self.job,
            "phone": self.phone,
            "marital_status": self.marital_status,
            "email": self.email,
            "address": self.address
        }

''' user_id sẽ được tạo sau khi username được tạo'''
class TenantFormModel(BaseFormModel):
    def __init__(self):
        super().__init__()
        self.income = ""

    def validate(self):
        """Validate tenant form data"""
        return super().validate()

    def to_dict(self):
        data = super().to_dict()
        data["income"] = self.income
        return data


class LandlordFormModel(BaseFormModel):
    def __init__(self):
        super().__init__()
        self.property_count = ""
        self.rental_price = ""

    def validate(self):
        """Validate landlord form data"""
        return super().validate()

    def to_dict(self):
        data = super().to_dict()
        data["property_count"] = self.property_count
        data["rental_price"] = self.rental_price
        return data