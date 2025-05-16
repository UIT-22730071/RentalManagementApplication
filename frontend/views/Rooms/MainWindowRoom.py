import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Rooms.RoomMenu import RoomMenu


class MainWindowRoom(QMainWindow):
    def __init__(self, room_id):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.setWindowTitle("Dashboard Chủ trọ")
        self.setGeometry(300, 100, 860, 600)

        '''
        self.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF6B6B, stop:1 #FFA07A);"
            "border-radius: 15px;"
        )
        '''
        # Giao diện chính được xử lý hoàn toàn bên trong RoomMenu
        self.setCentralWidget(RoomMenu(self, room_id))

    def close_window_menu(self):
        self.main_window.close()

'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowRoom(room_id="001")
    window.show()
    sys.exit(app.exec())
'''