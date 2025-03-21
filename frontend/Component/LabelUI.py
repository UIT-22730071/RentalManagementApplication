# Lưu trữ các thiết kế UI Label
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

class LabelUI(QWidget):
    def __init__(self, label_text="", font_size=14, color="white"):
        super().__init__()

        self.label = QLabel(label_text)
        self.label.setStyleSheet(f"""
            font-size: {font_size}px;
            color: {color};
            padding: 6px;
        """)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def setText(self, text):
        self.label.setText(text)

    def text(self):
        return self.label.text()
