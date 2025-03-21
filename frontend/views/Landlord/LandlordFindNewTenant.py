from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class FindNewTenant(QWidget):
    def __init__(self, main_window):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel(" 🔍 Tìm người thuê trọ mới")
        label.setStyleSheet("font-size: 20px; color: white;")
        layout.addWidget(label)
        self.setLayout(layout)