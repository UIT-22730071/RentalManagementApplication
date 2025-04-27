from PyQt5.QtWidgets import QMessageBox
from QLNHATRO.RentalManagementApplication.backend.model.BaseInforForm import TenantFormModel, LandlordFormModel
from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.UpdateInfoView import UpdateInfoView


class UpdateInfoController:
    def __init__(self, main_window, role, username, password,user_id):
        self.main_window = main_window
        self.role = role
        self.username = username
        self.password = password
        self.user_id = user_id

        # Create view

        self.view = UpdateInfoView(
            role=self.role,
            username=self.username,
            save_callback=self.save_info,
            cancel_callback=self.cancel
        )

        # Create model based on role
        if role == "Người thuê trọ":
            self.model = TenantFormModel()
        else:
            self.model = LandlordFormModel()

        #TODO: Lỗi ở đây
        # Connect signals
        #self.view.save_clicked.connect(self.save_info)
        #self.view.cancel_clicked.connect(self.cancel)

        # Set gradient background for main window
        self.main_window.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #FFDEE9, stop:1 #B5FFFC);
            }
        """)

    def show(self):
        """Set the view as central widget of main window"""
        self.main_window.setCentralWidget(self.view)

    def save_info(self):
        """Handle save button click"""
        # Get form data from view
        form_data = self.view.get_form_data()
        print("[DEBUG] form_data:", form_data)

        if not form_data:
            print("[ERROR] Không lấy được form_data")
            return

        # Update model with form data
        for key, value in form_data.items():
            if hasattr(self.model, key):
                setattr(self.model, key, value)

        # Validate model
        if not self.model.validate():
            print("[ERROR] Model validate failed")
            QMessageBox.warning(self.view, "Lỗi", "Vui lòng điền đầy đủ thông tin bắt buộc!")
            return
        print("[DEBUG] Model validate passed")  # Thêm dòng này
        # Save data to database
        # TODO: Add database save code here
        if self.role == "Người thuê trọ":
            from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository
            TenantRepository.update_user_info(self.user_id, self.model.to_dict())
        else:
            from QLNHATRO.RentalManagementApplication.Repository.LandlordRepository import LanlordRepository
            LanlordRepository.update_user_info(self.user_id, self.model.to_dict())
        print("[DEBUG] Đã lưu vào database thành công")  # Thêm dòng này
        # Show success message
        msg = QMessageBox(self.view)
        msg.setWindowTitle("Thành công")
        msg.setText("Thông tin đã được cập nhật thành công!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #f8f9fa;
            }
            QLabel {
                color: #333;
                font-size: 14px;
            }
            QPushButton {
                background-color: #4FBEEE;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: bold;
            }
        """)
        msg.exec()

        # TODO: Switch to main workspace screen
        # self.main_window.switch_to_workspace()

    def cancel(self):
        """Handle cancel button click"""
        msg = QMessageBox(self.view)
        msg.setWindowTitle("Xác nhận")
        msg.setText("Bạn có chắc muốn hủy cập nhật thông tin?")
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #f8f9fa;
            }
            QLabel {
                color: #333;
                font-size: 14px;
            }
            QPushButton {
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton[text="&Yes"] {
                background-color: #FF6B6B;
                color: white;
            }
            QPushButton[text="&No"] {
                background-color: #4FBEEE;
                color: white;
            }
        """)
        reply = msg.exec()

        if reply == QMessageBox.StandardButton.Yes:
            # Go back to login screen
            from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.HomeLogin import LoginWindow
            self.main_window.setCentralWidget(LoginWindow(self.main_window))