from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QMessageBox, QPushButton, QTableWidgetItem

from QLNHATRO.RentalManagementApplication.frontend.Component.tableUI import TableUI


class AdminUserManagement(QWidget):
    def __init__(self, main_window, user_list=None):
        super().__init__()
        self.main_window = main_window
        self.user_list = user_list or [
            {"stt": 1, "username": "admin", "role": "admin", "status": "Active"},
            {"stt": 2, "username": "landlord01", "role": "chutro", "status": "Active"},
            {"stt": 3, "username": "tenant01", "role": "nguoithue", "status": "Inactive"}
        ]

        self.setStyleSheet("background-color: #ecf0f1;")
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
        user = self.user_list[row]
        QMessageBox.information(
            self,
            "Chi tiết người dùng",
            f"👤 Username: {user['username']}\n🔐 Vai trò: {user['role']}\n📌 Trạng thái: {user['status']}"
        )

    def toggle_status(self, row):
        user = self.user_list[row]
        user["status"] = "Inactive" if user["status"] == "Active" else "Active"
        self.populate_table()
        from QLNHATRO.RentalManagementApplication.frontend.Component.SuccessDialog import SuccessDialog

        SuccessDialog.show_success(f"✅ Đã chuyển '{user['username']}' thành '{user['status']}'", self)

