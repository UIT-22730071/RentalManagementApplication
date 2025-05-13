# file: UserInfoWindow.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class UserInfoWindow(QMainWindow):
    def __init__(self, content_widget: QWidget, title="Thông tin người dùng"):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(400, 200, 700, 800)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(content_widget)

        container.setLayout(layout)
        self.setCentralWidget(container)
