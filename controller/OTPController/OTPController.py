# QLNHATRO/controller/LoginRegister/OTPController.py

from QLNHATRO.RentalManagementApplication.frontend.Component.ErrorDialog import ErrorDialog


class OTPController:
    @staticmethod
    def verify_otp(otp_text, username, view):
        if len(otp_text) != 4:
            ErrorDialog.show_error("⚠️ Vui lòng nhập đủ 4 chữ số của mã OTP.", view)
            return

        # TODO: Nếu có xác thực thực tế => gọi OTPService.verify_otp()
        print(f"✅ OTP xác nhận: {otp_text}")
        view.timer.stop()
        from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.ResetPasswordView import \
            ResetPasswordView
        view.reset_password_view = ResetPasswordView(username=username)
        view.hide()
        view.reset_password_view.show()

    @staticmethod
    def resend_otp(username, email, view):
        print(f"🔄 Gửi lại OTP cho {email}")
        view.reset_otp_fields()

    def go_to_reset_password(self):
        from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.ResetPasswordView import \
            ResetPasswordView
