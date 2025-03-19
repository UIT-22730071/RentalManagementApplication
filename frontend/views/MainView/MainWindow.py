import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import os
from PyQt5.QtCore import pyqtSignal

class SubWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWin


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Quản lý nhà trọ")
        self.setGeometry(100, 100, 400, 300)
        self.show()

        self.button = QPushButton('Nhấn vào đây', self)


        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_click(self):
        print("Bạn đã nhấn nút!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())