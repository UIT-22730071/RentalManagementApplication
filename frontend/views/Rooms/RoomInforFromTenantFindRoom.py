from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QScrollArea, QFrame, QGroupBox, QGridLayout, QDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class RoomsInforViewFromTenant(QDialog):
    def __init__(self, room_id, data_room_infor):
        super().__init__()

        self.room_id = room_id
        self.room_data = data_room_infor

        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.setWindowTitle("Chi tiết phòng")
        self.setMinimumWidth(700)
        self.setMinimumHeight(800)
        self.setModal(True)  # Để chặn thao tác với cửa sổ chính


        main_layout = QVBoxLayout(self)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        #scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        scroll_content = QFrame()
        scroll_layout = QVBoxLayout(scroll_content)

        # Card
        card = QFrame()
        #card.setStyleSheet("QFrame { background: white; border-radius: 12px; }")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("📌 THÔNG TIN CHI TIẾT PHÒNG")
        title.setFixedHeight(60)
        #title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setObjectName("Title")  # ✅ dùng style từ GlobalStyle
        #title.setStyleSheet("color: white; background-color: #2C3E50; border-radius: 10px; padding: 10px;")
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)

        # Section: Group thông tin
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

        for key, value in self.room_data.items():
            key_lbl = QLabel(f"{key}:")
            #key_lbl.setStyleSheet("font-weight: bold; color: #2c3e50;")
            val_lbl = QLabel(str(value))
            val_lbl.setWordWrap(True)
            grid.addWidget(key_lbl, row, 0)
            grid.addWidget(val_lbl, row, 1)
            row += 1

        card_layout.addWidget(group)

        # ===== Buttons =====
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(20)
        btn_layout.addStretch()

        # Button Liên hệ
        contact_btn = QPushButton("📞 Liên hệ")
        '''
        contact_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                padding: 8px 20px;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        '''
        contact_btn.clicked.connect(self.contact_owner)
        btn_layout.addWidget(contact_btn)

        # Button Thoát
        exit_btn = QPushButton("❌ Thoát")
        '''
        exit_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                padding: 8px 20px;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        '''
        exit_btn.setObjectName('CancelBtn')
        exit_btn.clicked.connect(self.close)
        btn_layout.addWidget(exit_btn)

        card_layout.addLayout(btn_layout)
        scroll_layout.addWidget(card)
        scroll.setWidget(scroll_content)
        main_layout.addWidget(scroll)

    def contact_owner(self):
        phone = self.room_data.get("SĐT", "Không có số điện thoại")
        from QLNHATRO.RentalManagementApplication.frontend.views.Form.ContactDialog import ContactDialog
        dialog = ContactDialog(phone)
        dialog.exec_()

    def close_view(self):
        self.setParent(None)
        self.deleteLater()
