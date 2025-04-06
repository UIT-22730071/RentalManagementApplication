from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from QLNHATRO.RentalManagementApplication.frontend.views.Landlord.LandlordMenu import LandlordMenu


class MainWindowLandlord(QMainWindow):
    print("mở MainWindowLandLord")
    def __init__(self, main_window, id_lanlord):
        super().__init__()
        print("[DEBUG] Bắt đầu tạo MainWindowLandlord 1 ")
        self.main_window = main_window
        self.id_landlord = id_lanlord

        print("[DEBUG] Bắt đầu tạo MainWindowLandlord 2")

        self.setWindowTitle("Dashboard Chủ trọ")
        self.setGeometry(300, 100, 1000, 600)
        self.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF6B6B, stop:1 #FFA07A);
            border-radius: 15px;
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        print("[DEBUG] Trước khi tạo LandlordHome")
        self.landlord_menu = LandlordMenu(self.main_window, self.id_landlord)
        main_layout.addWidget(self.landlord_menu)

        def go_to_exs(self, main_window):
            self.close()
