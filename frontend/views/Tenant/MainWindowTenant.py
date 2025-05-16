import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Tenant.TenantMenu import TenantMenu


class MainWindowTenant(QMainWindow):
    def __init__(self, id_tenant):
        super().__init__()
        self.setWindowTitle("Dashboard Người thuê")
        self.setGeometry(300, 100, GlobalStyle.WINDOW_WIDTH, GlobalStyle.WINDOW_HEIGHT)
        self.setStyleSheet(GlobalStyle.global_stylesheet())

        self.id_tenant = id_tenant

        # Widget trung tâm
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        main_layout = QVBoxLayout(central_widget)

        # Giao diện chính của người thuê
        self.tenant_menu = TenantMenu(self, self.id_tenant)
        main_layout.addWidget(self.tenant_menu)

    def close_window_menu(self):
        self.main_window.close()

'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowTenant(id_tenant=1)  # test demo
    window.show()
    sys.exit(app.exec_())
'''