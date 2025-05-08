import re


class Validators:

    @staticmethod
    def is_valid_phone(phone):
        pattern = r"^(0\d{9}|(\+84)\d{9})$"
        return re.match(pattern, phone) is not None

    @staticmethod
    def is_valid_email(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    @staticmethod
    def is_numeric_only(text):
        """Kiểm tra xem chuỗi chỉ chứa số"""
        return text.isdigit()

    @staticmethod
    def is_alpha_only(text):
        """Kiểm tra chuỗi chỉ chứa chữ (kể cả Unicode và dấu cách)"""
        return all(char.isalpha() or char.isspace() for char in text)

    @staticmethod
    def is_valid_cccd(cccd):
        """CCCD phải đúng 12 chữ số"""
        return cccd.isdigit() and len(cccd) == 12

    @staticmethod
    def is_valid_vietnamese_phone(phone):
        """Số điện thoại Việt Nam đúng 10 chữ số và bắt đầu bằng 0"""
        return phone.isdigit() and len(phone) == 10 and phone.startswith("0")

    @staticmethod
    def is_valid_password(password):
        """
        Mật khẩu mạnh: ít nhất 8 ký tự, gồm chữ hoa, chữ thường, số và ký tự đặc biệt
        """
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
        return re.match(pattern, password) is not None

    @staticmethod
    def is_positive_number(value):
        """Kiểm tra số dương"""
        try:
            return float(value) > 0
        except ValueError:
            return False

    @staticmethod
    def is_valid_date_format(date_str):
        """Kiểm tra định dạng ngày dd/mm/yyyy"""
        pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/\d{4}$"
        return re.match(pattern, date_str) is not None

    @staticmethod
    def is_valid_room_area(value):
        """Diện tích phòng phải là số thực dương dưới 200m²"""
        try:
            area = float(value)
            return 0 < area < 200
        except ValueError:
            return False

    @staticmethod
    def is_valid_name(name):
        """Tên chỉ chứa chữ, không chứa số hoặc ký tự lạ"""
        return bool(re.match(r"^[A-Za-zÀ-ỹ\s]{2,50}$", name))
