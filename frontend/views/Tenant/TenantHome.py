from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class TenantHome(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # Thêm giao diện chính ở đây
        # Ví dụ:
        layout = QVBoxLayout(self)
        label = QLabel("Chào mừng đến trang chính người thuê trọ!")
        layout.addWidget(label)
