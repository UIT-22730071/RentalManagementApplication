from PyQt5.QtWidgets import QComboBox
from QLNHATRO.RentalManagementApplication.frontend.Component.InputFieldUI import InputFieldUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class MaritalComboUI(InputFieldUI):
    def __init__(self, icon="💍", label="Tình trạng hôn nhân:"):
        marital_combo = QComboBox()
        marital_combo.addItems(["Độc thân", "Đã kết hôn", "Ly hôn", "Khác"])

        marital_combo.setStyleSheet(GlobalStyle.global_stylesheet() + """
            QComboBox {
                background-color: white;
                padding: 6px 12px;
            }
            QComboBox QAbstractItemView {
                selection-background-color: #FF6B6B;
                selection-color: white;
            }
        """)

        super().__init__(icon, label, marital_combo)

    def get_value(self):
        return self.input_widget.currentText()
