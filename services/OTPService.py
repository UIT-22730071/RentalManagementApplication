# QLNHATRO/services/OTPService.py

class OTPService:
    @staticmethod
    def verify_otp(username, otp):
        # Check from DB hoặc OTP lưu tạm thời
        return otp == "1234"  # Demo

    @staticmethod
    def check_change_password(username, current_password):
        #TODO: kiểm tra user name và passowrd người dùng nhập vào nếu đúng thì retuen True
        # nếu sai return false
        return True