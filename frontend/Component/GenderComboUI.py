from PyQt5.QtWidgets import QComboBox

from QLNHATRO.RentalManagementApplication.frontend.Component.InputFieldUI import InputFieldUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class GenderComboUI(InputFieldUI):
    def __init__(self, icon="⚧", label="Giới tính:"):
        gender_combo = QComboBox()
        gender_combo.addItems(["Nam", "Nữ", "Khác"])

        gender_combo.setStyleSheet(GlobalStyle.global_stylesheet() + """
            QComboBox {
                background-color: white;
                padding: 6px 12px;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                selection-background-color: #FF6B6B;
                selection-color: white;
            }
        """)

        super().__init__(icon, label, gender_combo)

    def get_value(self):
        return self.input_widget.currentText()
