from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class ListInvoices(QWidget):
    def __init__(self, main_window):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("🧾 Danh sách hóa đơn")
        label.setStyleSheet("font-size: 20px; color: white;")
        layout.addWidget(label)
        self.setLayout(layout)