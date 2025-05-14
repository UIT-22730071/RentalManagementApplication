from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDateEdit

from QLNHATRO.RentalManagementApplication.frontend.Component.InputFieldUI import InputFieldUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class DateTableUI(InputFieldUI):
    def __init__(self, icon: str, label: str):
        # Tạo QDateEdit với cấu hình sẵn
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        date_edit.setDate(QDate.currentDate())
        date_edit.setDisplayFormat("dd/MM/yyyy")

        date_edit.setStyleSheet(GlobalStyle.global_stylesheet() + """
            QDateEdit {
                background-color: white;
                padding: 6px 12px;
            }
            QCalendarWidget QToolButton {
                color: black;
                font-weight: bold;
                icon-size: 24px;
            }
            QCalendarWidget QWidget {
                alternate-background-color: #f6f6f6;
                background-color: white;
                color: black;
            }
            QCalendarWidget QAbstractItemView:enabled {
                background-color: white;
                selection-background-color: #FF6B6B;
                selection-color: white;
            }
            QCalendarWidget QHeaderView::section {
                background-color: #FF6B6B;
                color: white;
                padding: 4px;
                border: none;
            }
        """)

        # Gọi constructor cha
        super().__init__(icon, label, date_edit)

    def get_value(self):
        return self.input_widget.date().toString("dd/MM/yyyy")

    def set_date(self, qdate: QDate):
        self.input_widget.setDate(qdate)
