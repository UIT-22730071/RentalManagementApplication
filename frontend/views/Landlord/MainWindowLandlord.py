from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


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

        # Create and set central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Set up layout
        main_layout = QVBoxLayout(central_widget)

        # Add the landlord menu
        #self.landlord_menu = LandlordMenu(self, self.id_landlord)
        #main_layout.addWidget(self.landlord_menu)
