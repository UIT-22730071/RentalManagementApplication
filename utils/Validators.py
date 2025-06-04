import re

from sympy.printing.octave import print_octave_code


class Validators:
    """
    A utility class providing static methods for validating different types of input data.
    All methods return True if validation passes, False otherwise.
    """

    @staticmethod
    def is_valid_phone(phone):
        """
        Validates Vietnamese phone numbers in two formats:
        - Starting with '0' followed by 9 digits
        - Starting with '+84' followed by 9 digits

        Args:
            phone (str): Phone number to validate

        Returns:
            bool: True if valid, False otherwise
        """
        pattern = r"^(0\d{9}|(\+84)\d{9})$"
        return re.match(pattern, phone) is not None

    @staticmethod
    def is_valid_email(email):
        """
        Validates email format using a basic pattern

        Args:
            email (str): Email address to validate

        Returns:
            bool: True if valid, False otherwise
        """
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    @staticmethod
    def is_numeric_only(text):
        """
        Checks if the string contains only numeric characters

        Args:
            text (str): String to check

        Returns:
            bool: True if only numbers, False otherwise
        """
        return text.isdigit() if text else False

    @staticmethod
    def is_alpha_only(text):
        """
        Checks if the string contains only alphabetic characters and spaces

        Args:
            text (str): String to check

        Returns:
            bool: True if only alphabetic characters and spaces, False otherwise
        """
        return all(char.isalpha() or char.isspace() for char in text) if text else False

    @staticmethod
    def is_valid_name(name):
        """
        Validates person names (2-50 chars, letters, spaces and Vietnamese accents only)

        Args:
            name (str): Name to validate

        Returns:
            bool: True if valid, False otherwise
        """
        if not name or len(name) < 2 or len(name) > 50:
            return False
        return bool(re.match(r"^[A-Za-zÀ-ỹ\s]{2,50}$", name))

    @staticmethod
    def is_valid_id_card(id_card):
        """
        Validates Vietnamese ID cards (CCCD) - must be exactly 12 digits

        Args:
            id_card (str): ID card number to validate

        Returns:
            bool: True if valid, False otherwise
        """
        return id_card and id_card.isdigit() and len(id_card) == 12

    @staticmethod
    def is_valid_vn_phone(phone):
        """
        Validates Vietnamese phone numbers - must be exactly 10 digits and start with 0

        Args:
            phone (str): Phone number to validate

        Returns:
            bool: True if valid, False otherwise
        """
        return phone and phone.isdigit() and len(phone) == 10 and phone.startswith("0")

    @staticmethod
    def is_valid_password(password):
        """
        Validates password strength:
        - At least 8 characters
        - Contains uppercase letters
        - Contains lowercase letters
        - Contains digits
        - Contains special characters

        Args:
            password (str): Password to validate

        Returns:
            bool: True if strong password, False otherwise
        """
        if not password or len(password) < 8:
            return False

        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)

        return all([has_upper, has_lower, has_digit, has_special])

    @staticmethod
    def is_positive_number(value):
        """
        Checks if the value is a positive number

        Args:
            value (str or number): Value to check

        Returns:
            bool: True if positive number, False otherwise
        """
        try:
            return float(value) > 0
        except (ValueError, TypeError):
            return False

    @staticmethod
    def is_valid_date_format(date_str):
        """
        Validates date in format DD/MM/YYYY

        Args:
            date_str (str): Date string to validate

        Returns:
            bool: True if valid format, False otherwise
        """
        pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/\d{4}$"
        return bool(re.match(pattern, date_str)) if date_str else False

    @staticmethod
    def is_valid_room_area(value):
        """
        Validates room area (must be positive and less than 200 square meters)

        Args:
            value (str or number): Area value to validate

        Returns:
            bool: True if valid, False otherwise
        """
        try:
            area = float(value)
            return 0 < area < 200
        except (ValueError, TypeError):
            return False

    @staticmethod
    def has_no_whitespace(text):
        """
        Checks if text contains no whitespace characters

        Args:
            text (str): Text to check

        Returns:
            bool: True if no whitespace, False otherwise
        """
        return text and ' ' not in text

    @staticmethod
    def is_valid_username(username):
        """
        Validates username:
        - 4-20 characters
        - Can contain letters, numbers, underscore, dot
        - No spaces
        - Must start with a letter

        Args:
            username (str): Username to validate

        Returns:
            bool: True if valid, False otherwise
        """
        pattern = r"^[a-zA-Z][a-zA-Z0-9_.]{3,19}$"
        return bool(re.match(pattern, username)) if username else False

    @staticmethod
    def has_min_length(text, min_length):
        """
        Checks if text has minimum required length

        Args:
            text (str): Text to check
            min_length (int): Minimum required length

        Returns:
            bool: True if length is sufficient, False otherwise
        """
        return bool(text and len(text) >= min_length)

    @staticmethod
    def passwords_match(password1, password2):
        """
        Checks if two passwords match

        Args:
            password1 (str): First password
            password2 (str): Second password

        Returns:
            bool: True if matching, False otherwise
        """
        return password1 == password2 and password1 is not None

    @staticmethod
    def is_valid_input(text, allow_spaces=True, min_length=1, max_length=None):
        """
        General purpose input validation

        Args:
            text (str): Text to validate
            allow_spaces (bool): Whether spaces are allowed
            min_length (int): Minimum length required
            max_length (int): Maximum length allowed (None for no limit)

        Returns:
            bool: True if valid, False otherwise
        """
        if not text:
            return False

        if not allow_spaces and ' ' in text:
            return False

        if len(text) < min_length:
            return False

        if max_length and len(text) > max_length:
            return False

        return True

    @staticmethod
    def check_password_confirmpassword(password, confirm_password):
        """
        Checks if password and confirm password match

        Args:
            password (str): Password input
            confirm_password (str): Confirm password input

        Returns:
            bool: True if they match, False otherwise
        """
        print("password:", password)
        print("confirm_password:", confirm_password)
        return password == confirm_password if password and confirm_password else False