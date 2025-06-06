import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Admin.AdminMenu import AdminMenu


class MainWindowAdmin(QMainWindow):
    def __init__(self, user_id):
        super().__init__()

        self.user_id = user_id
        self.setWindowTitle("Quản Lý Nhà Trọ - Admin Dashboard")
        self.setGeometry(300, 100, 1000, 600)

        self.setStyleSheet(GlobalStyle.global_stylesheet() + """
            QMainWindow {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #8E2DE2, stop:1 #4A00E0);
                border-radius: 15px;
            }
        """)

        # Set up the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Add AdminMenu
        self.admin_menu = AdminMenu(self, user_id)
        layout.addWidget(self.admin_menu)


    def close_window_menu(self):
        self.main_window.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowAdmin(user_id=1)  # Giả lập user_id
    window.show()
    sys.exit(app.exec_())
