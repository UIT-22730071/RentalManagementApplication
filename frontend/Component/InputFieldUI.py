
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QFrame, QVBoxLayout

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


# Custom input field component
class InputFieldUI(QWidget):
    def __init__(self, icon, label, input_widget):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 5, 10, 5)

        # Icon label
        self.icon_label = QLabel(icon)
        self.icon_label.setFont(QFont("Arial", 14))
        self.icon_label.setFixedWidth(30)
        self.layout.addWidget(self.icon_label)

        # Label
        self.label = QLabel(label)
        self.label.setFont(QFont("Arial", 10))
        self.label.setFixedWidth(150)
        self.layout.addWidget(self.label)

        # Input widget
        self.input_widget = input_widget
        self.layout.addWidget(self.input_widget, 1)

        self.setStyleSheet(GlobalStyle.global_stylesheet() + """
            QLabel {
                font-size: 14px;
            }
            QLineEdit, QDateEdit, QComboBox {
                min-height: 24px;
            }
        """)

        # Add a shadow effect
        self.setGraphicsEffect(None)  # Clear any previous effect

        # Add container frame
        self.frame = QFrame()
        self.frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.7);
                border-radius: 8px;
                margin: 2px;
            }
        """)


# Form section component
class FormSection(QWidget):
    def __init__(self, title):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Section title
        self.title_label = QLabel(title)
        self.title_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: #333; margin-bottom: 10px; padding: 5px 10px;")

        # Section content
        self.content = QVBoxLayout()
        self.content.setSpacing(10)

        # Add to layout
        self.layout.addWidget(self.title_label)
        self.layout.addLayout(self.content)

    def add_field(self, field):
        self.content.addWidget(field)