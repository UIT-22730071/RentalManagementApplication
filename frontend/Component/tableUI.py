# TableUI.py - Component QTableWidget tổng quát có style đáng áp dụng chung

from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem, QPushButton
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class TableUI(QTableWidget):
    def __init__(self, column_labels: list[str], row_count=10, parent=None):
        super().__init__(parent)

        self.setColumnCount(len(column_labels))
        self.setHorizontalHeaderLabels(column_labels)
        self.setRowCount(row_count)

        # Cài đặt header và các thuộc tính chung
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setShowGrid(True)

        self.verticalHeader().setDefaultSectionSize(40)

        # Style mới từ GlobalStyle
        self.setStyleSheet(f"""
            QTableWidget {{
                background-color: {GlobalStyle.MAIN_BG};
                color: {GlobalStyle.TEXT_COLOR};
                font-size: 14px;
                font-family: 'Inter', sans-serif;
                border: 1px solid #EBEBF0;
                border-radius: 8px;
                gridline-color: #EBEBF0;
            }}

            QHeaderView::section {{
                background-color: {GlobalStyle.TABLE_HEADER_BG};
                color: {GlobalStyle.TABLE_TEXT_COLOR};
                font-size: 14px;
                font-weight: 400;
                font-family: 'Inter', sans-serif;
                padding: 8px;
                border: none;
            }}

            QTableWidget::item {{
                padding: 5px;
            }}

            QTableWidget::item:selected {{
                background-color: #DDEEFF;
                color: #202E66;
            }}

            QPushButton {{
                background-color: {GlobalStyle.PRIMARY_COLOR};
                color: white;
                padding: 6px 12px;
                border-radius: 8px;
                font-size: 14px;
                font-family: 'Be Vietnam', sans-serif;
            }}

            QPushButton:hover {{
                background-color: #1D4DA5;
            }}
        """)

    def populate(
            self,
            data: list[dict],
            has_button=False,
            button_column_name="Chi tiết",
            button_callback=None,
            header_to_key: dict = None
    ):
        self.setRowCount(max(len(data), 10))
        headers = [self.horizontalHeaderItem(i).text() for i in range(self.columnCount())]

        for row, row_data in enumerate(data):
            for col, header in enumerate(headers):
                # Nếu có ánh xạ key → dùng, không thì lấy header làm key
                key = header_to_key.get(header, header) if header_to_key else header
                value = row_data.get(key, "")
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.setItem(row, col, item)

            if has_button:
                btn = QPushButton(f"🔍 {button_column_name}")
                if button_callback:
                    btn.clicked.connect(lambda _, r=row: button_callback(r))
                self.setCellWidget(row, self.columnCount() - 1, btn)
