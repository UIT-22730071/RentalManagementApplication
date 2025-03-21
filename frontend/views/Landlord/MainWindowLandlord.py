import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QStackedWidget
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordMenu import LandlordMenu


# TODO: MainwindowLandlord được chuyển từ controller qua khi điều kiện checkuser thỏa mản
#TODO:  __int__(self,User_landlord, landlord_infor)


# MainWindowLandlord
class MainWindowLandlord(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dashboard Chủ trọ")
        self.setGeometry(300, 100, 1000, 600)

        self.setStyleSheet("background-color: #CAA4A4; border-radius: 15px;")

        self.setCentralWidget(LandlordMenu(self))  # Nếu LandlordMenu cần MainWindowLandlord

        #self.setCentralWidget()                    # Khung làm việc bên phải


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowLandlord()
    window.show()
    sys.exit(app.exec_())