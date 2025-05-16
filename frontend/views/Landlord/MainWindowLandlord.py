from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordMenu import LandlordMenu


class MainWindowLandlord(QMainWindow):
    print("mở MainWindowLandLord")

    def __init__(self, id_lanlord):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.id_landlord = id_lanlord

        # Setup UI
        self.setWindowTitle("Dashboard Chủ trọ")
        self.setGeometry(300, 100, 1000, 600)
        #self.setStyleSheet("""
            #background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF6B6B, stop:1 #FFA07A);
            #border-radius: 15px;
        #""")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.landlord_menu = LandlordMenu(self, id_lanlord)
        layout.addWidget(self.landlord_menu)

    def close_window_menu(self):
        self.main_window.close()