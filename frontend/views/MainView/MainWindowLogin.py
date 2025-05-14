import sys

from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Login_Register.HomeLogin import LoginWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.setWindowTitle("Ứng dụng Quản lý")
        self.setGeometry(200, 100, 300, 620)  # Ban đầu chỉ hiển thị khung trái
        #self.setGeometry(300, 100, 1000, 600)
        #self.setStyleSheet("background-color: #202020; border-radius: 15px;")

        # Đặt giao diện đăng nhập làm trang chính
        #self.setCentralWidget(LoginWindow(self))
        # Trang khởi đầu
        # Sửa lại dòng này:
        self.switch_to_page(LoginWindow)

    def switch_to_page(self, PageClass, *args):
        try:
            #print(f"[MainWindow] Đang tạo {PageClass.__name__} với args={args}")
            widget = PageClass(self, *args)
            #print(f"[MainWindow] Tạo {PageClass.__name__} thành công")
        except Exception as e:
            #print(f"[❌ MainWindow] Lỗi tạo {PageClass.__name__}: {e}")
            import traceback
            traceback.print_exc()
            widget = QLabel("⚠️ Không thể hiển thị trang")

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
