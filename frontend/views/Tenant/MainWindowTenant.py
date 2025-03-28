import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantMenu import TenantMenu


class MainWindowTenant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản Lý Nhà Trọ - Tenant Dashboard")
        self.setGeometry(300, 100, 1000, 600)

        self.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF6B6B, stop:1 #FFA07A);"
                           " border-radius: 15px;")
        # Create a central widget to hold the tenant menu
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        main_layout = QVBoxLayout(central_widget)

        # Create TenantMenu instance
        self.tenant_menu = TenantMenu(self)
        main_layout.addWidget(self.tenant_menu)

    def go_to_exs(self, main_window):
        """
        Method to handle exit functionality (placeholder)
        In a real application, this might close the application or return to login screen
        """
        print("Exiting application")
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowTenant()
    window.show()
    sys.exit(app.exec_())