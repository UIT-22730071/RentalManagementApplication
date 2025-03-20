import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.HomeLogin import LoginWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ứng dụng Quản lý")
        self.setGeometry(200, 100, 800, 500)

        # Đặt giao diện đăng nhập làm trang chính
        self.setCentralWidget(LoginWindow(self))

    def switch_to_workspace(self):
        """Chuyển sang giao diện Workspace sau khi đăng nhập"""
        #from WorkspacePage import WorkspacePage  # Import tại đây để tránh circular import
        #self.setCentralWidget(WorkspacePage(self))
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
