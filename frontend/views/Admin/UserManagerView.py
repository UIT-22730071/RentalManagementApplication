from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QMessageBox, QPushButton, QTableWidgetItem



from QLNHATRO.RentalManagementApplication.frontend.Component.ErrorDialog import ErrorDialog
from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class AdminUserManagement(QWidget):
    def __init__(self, main_window, user_list=None):
        super().__init__()
        self.main_window = main_window
        self.user_list = user_list or [
            {"stt": 1, "username": "admin", "role": "admin", "status": "Active"},
            {"stt": 2, "username": "landlord01", "role": "Chủ trọ", "status": "Active"},
            {"stt": 3, "username": "tenant01", "role": "Người thuê trọ", "status": "Inactive"}
        ]

        self.setStyleSheet(GlobalStyle.global_stylesheet() + """
            QWidget {
                background-color: #F7F9FC;
            }
            QLabel {
                color: #202E66;
            }
        """)

        main_layout = QVBoxLayout()

        title = QLabel("👥 Danh sách tài khoản người dùng")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                border: 1px solid #dcdcdc;
                padding: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }
        """)

        headers = ["STT", "Username", "Vai trò", "Trạng thái", "Xem chi tiết", "Thay đổi trạng thái"]
        self.table = TableUI(headers)
        self.populate_table()

        main_layout.addWidget(self.table)
        main_layout.addWidget(frame)
        self.setLayout(main_layout)

    def populate_table(self):
        self.table.setRowCount(len(self.user_list))

        for row, user in enumerate(self.user_list):
            self.table.setItem(row, 0, QTableWidgetItem(str(user['stt'])))
            self.table.setItem(row, 1, QTableWidgetItem(user['username']))
            self.table.setItem(row, 2, QTableWidgetItem(user['role']))
            self.table.setItem(row, 3, QTableWidgetItem(user['status']))

            for col in range(4):
                self.table.item(row, col).setTextAlignment(Qt.AlignCenter)

            # Nút "Xem chi tiết"
            btn_detail = QPushButton("Chi tiết")
            btn_detail.clicked.connect(lambda _, r=row: self.view_detail(r))
            self.table.setCellWidget(row, 4, btn_detail)

            # Nút "Chuyển trạng thái"
            btn_toggle = QPushButton("Chuyển")
            btn_toggle.clicked.connect(lambda _, r=row: self.toggle_status(r))
            self.table.setCellWidget(row, 5, btn_toggle)


    def view_detail(self, row):
        try:
            user = self.user_list[row]
            role = user.get('role')
            username = user.get('username')
            print(f"🔍 Kiểm tra role: {role}, username: {username}")

            if not role or not username:
                ErrorDialog.show_error("Không tìm thấy thông tin người dùng hợp lệ.", self)
                return

            if role == 'Chủ trọ':
                from QLNHATRO.RentalManagementApplication.controller.AdminController.AdminController import \
                    AdminController
                AdminController.go_to_open_infor_lanlord(username)
            elif role == 'Người thuê trọ':
                from QLNHATRO.RentalManagementApplication.controller.AdminController.AdminController import \
                    AdminController
                AdminController.go_to_infor_tenant(username)
            elif role == 'admin':
                from QLNHATRO.RentalManagementApplication.controller.AdminController.AdminController import \
                    AdminController
                #AdminController.go_to_infor_admin(username)
                pass
            else:
                ErrorDialog.show_error(f"Không nhận diện được quyền truy cập: {role}", self)

        except IndexError:
            ErrorDialog.show_error("Vui lòng chọn một dòng hợp lệ.", self)
        except Exception as e:
            import traceback
            traceback.print_exc()
            ErrorDialog.show_error(f"Đã xảy ra lỗi: {str(e)}", self)

    def toggle_status(self, row):
        user = self.user_list[row]
        user["status"] = "Inactive" if user["status"] == "Active" else "Active"
        self.populate_table()
        from QLNHATRO.RentalManagementApplication.frontend.Component.SuccessDialog import SuccessDialog

        SuccessDialog.show_success(f"✅ Đã chuyển '{user['username']}' thành '{user['status']}'", self)

