from PyQt5.QtWidgets import QWidget


class FindNewRoom(QWidget):
    def __int__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # Thêm giao diện chính ở đây