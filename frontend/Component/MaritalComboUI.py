from PyQt5.QtWidgets import QComboBox

from QLNHATRO.RentalManagementApplication.frontend.Component.InputFieldUI import InputFieldUI

class MaritalComboUI(InputFieldUI):
    def __init__(self, icon="💍", label="Tình trạng hôn nhân:"):
        marital_combo = QComboBox()
        marital_combo.addItems(["Độc thân", "Đã kết hôn", "Ly hôn", "Khác"])

        marital_combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 6px 12px;
                background-color: white;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                selection-background-color: #FF6B6B;
                selection-color: white;
                border: 1px solid #ccc;
            }
            QComboBox QAbstractItemView::item {
                padding: 6px;
                margin: 2px;
                background-color: transparent;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #1812DC;
            }
        """)

        super().__init__(icon, label, marital_combo)

    def get_value(self):
        return self.input_widget.currentText()
