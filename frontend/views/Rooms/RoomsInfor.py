# RoomInfor.py
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QScrollArea, QFrame, QGroupBox, QGridLayout, QDialog, QLineEdit)
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.Component.InforUpdater import InfoUpdater


class RoomsInfor(QWidget):
    def __init__(self, main_window, room_id,data_room_infor):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window
        self.room_id = room_id
        self.room_data = data_room_infor
        self.label_fields = []  #  để lưu thứ tự key tương ứng cho từng dòng

        #self.setStyleSheet("QWidget { background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFDEE9, stop:1 #B5FFFC); }")

        main_layout = QVBoxLayout(self)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        #scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # Card
        card = QFrame()
        #card.setStyleSheet("QFrame { background: white; border-radius: 12px; }")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("📌 THÔNG TIN CHI TIẾT PHÒNG")
        #title.setFont(QFont("Arial", 20, QFont.Bold))
        #title.setStyleSheet("color: white; background-color: #2C3E50; border-radius: 10px; padding: 10px;")
        title.setObjectName("Title")
        title.setFixedHeight(60)
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)

        # Section
        group = QGroupBox("📋 Thông tin phòng")
        '''
        group.setStyleSheet("""
            QGroupBox {
                font-weight: bold; border: 1px solid #3498db;
                border-radius: 10px; margin-top: 15px; padding-top: 15px;
                background-color: #f2f9fb;
            }
            QGroupBox::title {
                subcontrol-origin: margin; left: 10px;
                padding: 0 10px; font-size: 20px;
                background-color: white; border-radius: 5px; color: #2c3e50;
            }
        """)
        '''
        grid = QGridLayout(group)
        row = 0

        # Lưu label để cập nhật
        self.value_labels = {}

        for key, value in self.room_data.items():
            i = row  # row cũng là thứ tự index
            self.label_fields.append(key)  # lưu key tương ứng cho mỗi dòng
            key_lbl = QLabel(key + ":")
            key_lbl.setFixedWidth(300)
            #key_lbl.setStyleSheet("font-weight: bold;")
            val_lbl = QLabel(value)
            val_lbl.setWordWrap(True)
            self.value_labels[key] = val_lbl

            edit_btn = QPushButton("Thay đổi")
            edit_btn.setFixedWidth(180)
            edit_btn.setFixedHeight(40)

            #edit_btn.clicked.connect(lambda _, k=key: self.open_edit_dialog(k))

            edit_btn.clicked.connect(lambda _, index=i: self.update_field(index))


            grid.addWidget(key_lbl, row, 0)
            grid.addWidget(val_lbl, row, 1)
            grid.addWidget(edit_btn, row, 2)
            row += 1

        card_layout.addWidget(group)
        scroll_layout.addWidget(card)
        scroll.setWidget(scroll_content)
        main_layout.addWidget(scroll)

    def update_field(self, index):
        key = self.label_fields[index]
        label = self.value_labels[key]

        dialog = InfoUpdater(
            title=key,
            current_value=label.text(),
            on_update_callback=lambda new_val: self.apply_update(index, new_val)
        )
        dialog.exec_()

    def open_edit_dialog(self, key):
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Cập nhật {key}")
        dialog.setModal(True)
        dialog.setMinimumWidth(600)
        dialog.setMinimumHeight(350)
        '''
        dialog.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
                border-radius: 10px;
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #2C3E50;
                padding: 5px 0;
            }
            QLineEdit {
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #bdc3c7;
                background-color: white;
                font-size: 14px;
                margin: 5px 0;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
        """)
        '''
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Title label
        title_label = QLabel(f"Cập nhật thông tin: {key}")
        title_label.setObjectName("Title")
        #title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #2C3E50; padding: 5px 0;")
        title_label.setFixedHeight(50)
        layout.addWidget(title_label)

        # Input field
        input_field = QLineEdit()
        input_field.setText(self.value_labels[key].text())
        input_field.setFixedHeight(60)
        layout.addWidget(input_field)

        # Button layout for alignment
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        # Cancel button
        cancel_btn = QPushButton("Hủy")
        cancel_btn.setFixedSize(100, 40)
        cancel_btn.setObjectName("CancelBtn")
        cancel_btn.clicked.connect(dialog.reject)
        button_layout.addWidget(cancel_btn)

        # Save button
        save_btn = QPushButton("Lưu")
        save_btn.setFixedSize(100, 40)
        '''
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1e6091;
            }
        """)
        '''
        save_btn.clicked.connect(lambda: self.save_change(dialog, key, input_field.text()))
        button_layout.addWidget(save_btn)

        layout.addLayout(button_layout)

        # Set focus on input field
        input_field.setFocus()

        dialog.exec()

    def save_change(self, dialog, key, text):
        self.value_labels[key].setText(text)
        dialog.accept()
