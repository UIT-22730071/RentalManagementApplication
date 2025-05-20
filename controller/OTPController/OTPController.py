# QLNHATRO/controller/LoginRegister/OTPController.py
from PyQt5.QtWidgets import QMessageBox

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


    @staticmethod
    def request_initial_otp(username: str, email: str):
        """
        Yêu cầu backend gửi mã OTP ban đầu.
        Trả về (bool: success, str: message)
        """
        print(f"OTPController: Yêu cầu gửi OTP ban đầu cho username '{username}', email '{email}'.")
        # --- LOGIC GỌI BACKEND/SERVICE ĐỂ GỬI OTP BAN ĐẦU ---
        # Ví dụ:
        # from your_project.services import AuthService
        # success, message = AuthService.request_otp_for_password_reset(username, email)
        # Giả lập kết quả:
        if username and email:
            print(f"OTPController: Giả lập gửi OTP thành công đến {email}.")
            return True, f"Mã OTP đã được gửi đến {email}."
        else:
            return False, "Thiếu thông tin username hoặc email."
        # --- KẾT THÚC LOGIC GỌI BACKEND/SERVICE ---
'''
    @staticmethod
    def verify_otp(otp_code: str, username: str, view_instance: 'OTPVerificationView'):
        """
        Xác minh mã OTP.
        view_instance là instance của OTPVerificationView.
        """
        print(f"OTPController: Xác minh OTP '{otp_code}' cho username '{username}'.")
        # --- LOGIC GỌI BACKEND/SERVICE ĐỂ XÁC MINH OTP ---
        # Ví dụ:
        # from your_project.services import AuthService
        # success, message = AuthService.verify_otp_for_password_reset(username, otp_code)

        # Giả lập kết quả từ backend:
        # Để test, OTP đúng là "1234"
        if username and otp_code == "1234":
            success = True
            message = "Xác minh OTP thành công!"
        elif not username:
            success = False
            message = "Lỗi: Không có thông tin người dùng."
        else:
            success = False
            message = "Mã OTP không chính xác hoặc đã hết hạn."
        # --- KẾT THÚC LOGIC GỌI BACKEND/SERVICE ---

        if success:
            if hasattr(view_instance, 'on_otp_verification_success'):
                view_instance.on_otp_verification_success()
        else:
            if hasattr(view_instance, 'on_otp_verification_failure'):
                view_instance.on_otp_verification_failure(message)

    @staticmethod
    def resend_otp(username: str, email: str, view_instance: 'OTPVerificationView'):
        """
        Yêu cầu gửi lại mã OTP.
        """
        print(f"OTPController: Yêu cầu gửi lại OTP cho username '{username}', email '{email}'.")
        # --- LOGIC GỌI BACKEND/SERVICE ĐỂ GỬI LẠI OTP ---
        # Ví dụ:
        # success_resend, message_resend = AuthService.resend_otp_for_password_reset(username, email)

        # Giả lập kết quả:
        success_resend = True
        message_resend = f"Mã OTP mới đã được gửi đến {email}."
        # --- KẾT THÚC LOGIC GỌI BACKEND/SERVICE ---

        if success_resend:
            QMessageBox.information(view_instance, "Đã gửi lại OTP", message_resend)
            # view_instance đã tự xử lý việc reset timer và fields
        else:
            QMessageBox.warning(view_instance, "Lỗi gửi lại OTP", message_resend)
'''