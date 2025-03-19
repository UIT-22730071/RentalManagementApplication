import sys

from PyQt5.QtWidgets.QWidget import setWindowFlag
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QStackedWidget
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login & Sign Up")
        self.setGeometry(200, 100, 300, 450)  # 📌 Ban đầu chỉ hiển thị frame trái
        self.setStyleSheet("background-color: #202020; border-radius: 15px;")

        # main widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())