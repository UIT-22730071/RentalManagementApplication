# QLNHATRO/services/OTPService.py

class OTPService:
    @staticmethod
    def verify_otp(username, otp):
        # Check from DB hoặc OTP lưu tạm thời
        return otp == "1234"  # Demo
