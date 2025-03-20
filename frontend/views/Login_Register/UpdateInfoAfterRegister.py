import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox, QLineEdit
)
from PyQt6.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Component.InputTextUI import InputTextUI


# ✅ Lớp Form cập nhật thông tin sau đăng ký
class UpdateInfoAfterRegister(QWidget):
    def __init__(self,main_window, role, username, password):
        super().__init__()
        self.main_window = main_window
        self.role = role
        self.username = username
        self.password = password
        self.setWindowTitle("Cập nhật thông tin")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #FDD7D2; border-radius: 15px;")
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout(self)
        label_update_info = QLabel(f"Cập nhật thông tin - {self.role}")
        label_update_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        form_layout = QVBoxLayout()

        # Hiển thị thông tin đăng ký
        self.label_username = QLabel(f"Tên tài khoản: {self.username}")
        self.label_password = QLabel("Mật khẩu: ********")

        form_layout.addWidget(label_update_info)
        form_layout.addWidget(self.label_username)
        form_layout.addWidget(self.label_password)

        if self.role == "Người thuê trọ":
            self.form = TenantUpdateForm()
        else:
            self.form = LandlordUpdateForm()

        form_layout.addWidget(self.form)

        self.btn_save = QPushButton("Lưu thông tin")
        self.btn_save.clicked.connect(self.save_info)

        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.btn_save)

    def save_info(self):
        QMessageBox.information(self, "Thông báo", "Thông tin đã được cập nhật thành công!")


# ✅ Lớp cập nhật thông tin cho Người thuê trọ
class TenantUpdateForm(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.input_name = InputTextUI("Họ và tên")
        self.input_phone = InputTextUI("Số điện thoại")
        self.input_email = InputTextUI("Email")
        self.input_address = InputTextUI("Địa chỉ thường trú")
        self.input_job = InputTextUI("Nghề nghiệp")
        self.input_income = InputTextUI("Thu nhập hàng tháng")
        self.input_budget = InputTextUI("Ngân sách")

        layout.addWidget(self.input_name)
        layout.addWidget(self.input_phone)
        layout.addWidget(self.input_email)
        layout.addWidget(self.input_address)
        layout.addWidget(self.input_job)
        layout.addWidget(self.input_income)
        layout.addWidget(self.input_budget)


# ✅ Lớp cập nhật thông tin cho Chủ trọ
class LandlordUpdateForm(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.input_name = InputTextUI("Họ và tên")
        self.input_phone = InputTextUI("Số điện thoại")
        self.input_email = InputTextUI("Email")
        self.input_address = InputTextUI("Địa chỉ thường trú")
        self.input_property_count = InputTextUI("Số lượng phòng trọ đang quản lý")
        self.input_rental_price = InputTextUI("Giá cho thuê trung bình")

        layout.addWidget(self.input_name)
        layout.addWidget(self.input_phone)
        layout.addWidget(self.input_email)
        layout.addWidget(self.input_address)
        layout.addWidget(self.input_property_count)
        layout.addWidget(self.input_rental_price)



