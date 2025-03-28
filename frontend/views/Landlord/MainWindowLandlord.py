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

        self.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF6B6B, stop:1 #FFA07A);"
                           " border-radius: 15px;")

        self.setCentralWidget(LandlordMenu(self))  # Nếu LandlordMenu cần MainWindowLandlord

        #self.setCentralWidget()                    # Khung làm việc bên phải
        def go_to_exs(self, main_window):
            """
            Method to handle exit functionality (placeholder)
            In a real application, this might close the application or return to login screen
            """
            print("Exiting application")
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowLandlord()
    window.show()
    sys.exit(app.exec_())