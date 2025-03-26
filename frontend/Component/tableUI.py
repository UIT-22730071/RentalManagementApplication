# TableUI.py - Component QTableWidget tổng quát có style đáng áp dụng chung

from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem, QPushButton
from PyQt5.QtCore import Qt

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

        # Style đồng bộ với RoomList
        self.setStyleSheet("""
            QTableWidget {
                background-color: #34495e;
                gridline-color: #ecf0f1;
                color: white;
                font-size: 14px;
                border: 2px solid #d35400;
                border-radius: 8px;
            }

            QHeaderView::section {
                background-color: #FFA07A;
                color: white;
                font-weight: bold;
                padding: 6px;
                min-height: 30px;
                border-radius: 2px;
                border: 1px solid #d35400;
            }

            QTableWidget::item {
                padding: 5px;
            }

            QTableWidget::item:selected {
                background-color: #4AA1C6;
                color: white;
            }

            QPushButton {
                background-color: #203BEC;
                color: white;
                padding: 5px 10px;
                border-radius: 8px;
            }

            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

    def populate(self, data: list[dict], has_button=False, button_column_name="Chi tiết", button_callback=None):
        self.setRowCount(max(len(data), 10))
        for row, row_data in enumerate(data):
            for col, (key, value) in enumerate(row_data.items()):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)  # ✅ Căn giữa nội dung
                self.setItem(row, col, item)

            if has_button:
                btn = QPushButton(f"🔍 {button_column_name}")
                if button_callback:
                    btn.clicked.connect(lambda _, r=row: button_callback(r))
                self.setCellWidget(row, self.columnCount() - 1, btn)