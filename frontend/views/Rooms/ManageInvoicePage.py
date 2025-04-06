from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QMessageBox, QGridLayout, QGroupBox, QDialog, QScrollArea, QFrame, QComboBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class InvoiceInputPage(QWidget):
    def __init__(self, main_window, room_data_list, tenant_finder_callback, go_to_preview_callback):
        super().__init__()
        self.main_window = main_window
        self.room_data_list = room_data_list  # List of all rooms
        self.tenant_finder_callback = tenant_finder_callback
        self.go_to_preview_callback = go_to_preview_callback
        self.selected_room = None
        self.selected_tenant = None
        self.labels = {}

        # Consistent gradient background from previous files
        self.setStyleSheet(
            "QWidget { background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E8E8E8, stop:1 #f2f9fb); }")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Create scroll area for better handling of content
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        scroll_content = QWidget()
        layout = QVBoxLayout(scroll_content)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(20)

        # ======= TITLE =======
        title = QLabel("📝 TẠO HÓA ĐƠN PHÒNG TRỌ")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setStyleSheet("color: white; background-color: #2C3E50; border-radius: 10px; padding: 10px;")
        title.setAlignment(Qt.AlignCenter)
        title.setFixedHeight(50)
        layout.addWidget(title)

        # ======= ROOM SELECTION SECTION =======
        room_selection_group = QGroupBox("🏠 Chọn phòng")
        room_selection_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold; 
                border: 1px solid #3498db;
                border-radius: 10px; 
                margin-top: 15px; 
                padding-top: 15px;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin; 
                left: 10px;
                padding: 0 10px; 
                font-size: 20px;
                background-color: #f2f9fb; 
                border-radius: 5px; 
                color: #2c3e50;
            }
        """)

        room_selection_layout = QVBoxLayout(room_selection_group)

        # Room selection combo box
        room_combo_layout = QHBoxLayout()
        room_label = QLabel("Chọn phòng:")
        room_label.setStyleSheet("font-weight: bold; color: #2c3e50; font-size: 14px;")

        self.room_combo = QComboBox()
        self.room_combo.setStyleSheet("""
            QComboBox {
                padding: 8px;
                border-radius: 5px;
                background-color: #f2f9fb;
                border: 1px solid #3498db;
                font-size: 14px;
                min-width: 250px;
            }
            QComboBox:hover {
                border-color: #2980b9;
                border: 1px solid #2980b9;
                background-color: #e8f4f8;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;
                border-left: 1px solid #3498db;
                background-color: #ffffff;
                image: none; 
            }
            QComboBox::drop-down:hover {
                background-color: #d6ecfa;
                image: "🔽"; 
            }
                """)

        # Populate room combo box
        for room in self.room_data_list:
            self.room_combo.addItem(f"{room['ten_phong']} - ID: {room['id']}", userData=room)

        self.room_combo.currentIndexChanged.connect(self.on_room_selected)

        room_combo_layout.addWidget(room_label)
        room_combo_layout.addWidget(self.room_combo)
        room_combo_layout.addStretch()
        room_selection_layout.addLayout(room_combo_layout)
        layout.addWidget(room_selection_group)

        # ======= PHẦN 1: THÔNG TIN PHÒNG =======
        self.group_info = QGroupBox("📋 Thông tin phòng và người thuê")
        self.group_info.setStyleSheet("""
            QGroupBox {
                font-weight: bold; 
                border: 1px solid #3498db;
                border-radius: 10px; 
                margin-top: 15px; 
                padding-top: 15px;
                background-color: #f2f9fb;
            }
            QGroupBox::title {
                subcontrol-origin: margin; 
                left: 10px;
                padding: 0 10px; 
                font-size: 20px;
                background-color: white; 
                border-radius: 5px; 
                color: #2c3e50;
            }
        """)

        info_grid = QGridLayout(self.group_info)
        info_grid.setVerticalSpacing(8)

        # Display placeholders initially
        static_fields = [
            ("Tên phòng", "Chưa chọn phòng"),
            ("Mã phòng", "---"),
            ("Người thuê", "---"),
            ("CCCD", "---"),
            ("Địa chỉ", "---"),
            ("Giá phòng", "---"),
            ("Giá điện", "---"),
            ("Giá nước", "---"),
            ("Internet", "---"),
            ("Phí khác", "---"),
            ("Số điện cũ", "---"),
            ("Số nước cũ", "---"),
        ]

        for i, (label, value) in enumerate(static_fields):
            key_lbl = QLabel(f"{label}:")
            key_lbl.setStyleSheet("font-weight: bold;")

            val_lbl = QLabel(str(value))
            val_lbl.setWordWrap(True)
            val_lbl.setStyleSheet("padding-left: 5px;")

            self.labels[label] = val_lbl
            info_grid.addWidget(key_lbl, i, 0)
            info_grid.addWidget(val_lbl, i, 1)

        layout.addWidget(self.group_info)

        # Initially hide the room info section until a room is selected
        self.group_info.setVisible(False)

        # ======= PHẦN 2: NHẬP THÔNG TIN HÓA ĐƠN =======
        self.update_group = QGroupBox("🧾 Cập nhật thông tin hóa đơn")
        self.update_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold; 
                border: 1px solid #3498db;
                border-radius: 10px; 
                margin-top: 15px; 
                padding-top: 15px;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin; 
                left: 10px;
                padding: 0 10px; 
                font-size: 18px;
                background-color: #f2f9fb; 
                border-radius: 5px; 
                color: #2c3e50;
            }
        """)

        update_layout = QGridLayout(self.update_group)
        update_layout.setVerticalSpacing(15)
        update_layout.setHorizontalSpacing(10)

        # Field styles
        field_style = """
            QLineEdit {
                padding: 8px;
                border-radius: 8px;
                background-color: #f2f9fb;
                border: 1px solid #3498db;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #2980b9;
                background-color: #e8f4f8;
            }
        """

        label_style = """
            font-weight: bold;
            color: #2c3e50;
            font-size: 14px;
        """

        # Create input fields with new styling
        self.dien_input = QLineEdit()
        self.dien_input.setPlaceholderText("Nhập chỉ số điện mới")
        self.dien_input.setStyleSheet(field_style)
        dien_label = QLabel("🔌 Số điện mới:")
        dien_label.setStyleSheet(label_style)
        update_layout.addWidget(dien_label, 0, 0)
        update_layout.addWidget(self.dien_input, 0, 1)

        self.nuoc_input = QLineEdit()
        self.nuoc_input.setPlaceholderText("Nhập chỉ số nước mới")
        self.nuoc_input.setStyleSheet(field_style)
        nuoc_label = QLabel("🚿 Số nước mới:")
        nuoc_label.setStyleSheet(label_style)
        update_layout.addWidget(nuoc_label, 1, 0)
        update_layout.addWidget(self.nuoc_input, 1, 1)

        self.phi_khac_input = QLineEdit()
        self.phi_khac_input.setPlaceholderText("Chi phí khác (nếu có)")
        self.phi_khac_input.setStyleSheet(field_style)
        phi_khac_label = QLabel("🧾 Phí khác (VNĐ):")
        phi_khac_label.setStyleSheet(label_style)
        update_layout.addWidget(phi_khac_label, 2, 0)
        update_layout.addWidget(self.phi_khac_input, 2, 1)


        layout.addWidget(self.update_group)

        # Initially hide the form until a room is selected
        self.update_group.setVisible(False)

        # ======= BUTTONS =======
        button_layout = QHBoxLayout()

        # Reset button
        self.reset_btn = QPushButton("Đặt lại")
        self.reset_btn.setStyleSheet("""
            QPushButton {
                background-color: #4FBEEE;
                color: white;
                font-weight: bold;
                font-size: 16px;
                padding: 10px 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #3ba8d8;
            }
            QPushButton:pressed {
                background-color: #2b93c3;
            }
        """)
        self.reset_btn.setFixedWidth(150)
        self.reset_btn.clicked.connect(self.reset_form)

        # Confirm button
        self.confirm_btn = QPushButton("Cập nhật hóa đơn")
        self.confirm_btn.setStyleSheet("""
            QPushButton {
                background-color: #1812DC;
                color: white;
                font-weight: bold;
                font-size: 16px;
                padding: 10px 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #e74c3c;
            }
            QPushButton:pressed {
                background-color: #c0392b;
            }
        """)
        self.confirm_btn.setFixedWidth(250)
        self.confirm_btn.clicked.connect(self.on_export_clicked)

        button_layout.addWidget(self.reset_btn)
        button_layout.addWidget(self.confirm_btn)
        button_layout.setAlignment(Qt.AlignCenter)
        layout.addLayout(button_layout)

        # Initially disable the buttons until a room is selected
        self.reset_btn.setEnabled(False)
        self.confirm_btn.setEnabled(False)

        # Setup scroll area
        scroll.setWidget(scroll_content)
        main_layout.addWidget(scroll)

    def on_room_selected(self):
        """Handle room selection from the combo box"""
        room = self.room_combo.currentData()

        if not room:
            self.group_info.setVisible(False)
            self.update_group.setVisible(False)
            self.reset_btn.setEnabled(False)
            self.confirm_btn.setEnabled(False)
            return

        self.selected_room = room

        # Find tenant information for this room
        tenant = self.tenant_finder_callback(room['id'])
        if tenant:
            self.selected_tenant = tenant

            # Update room and tenant info display
            self.update_room_tenant_info(room, tenant)

            # Enable form sections
            self.group_info.setVisible(True)
            self.update_group.setVisible(True)
            self.reset_btn.setEnabled(True)
            self.confirm_btn.setEnabled(True)

            # Pre-fill the form if previous values exist
            if 'phi_khac' in room:
                self.phi_khac_input.setText(str(room['phi_khac']))


        else:
            QMessageBox.warning(self, "Lỗi",
                                f"Phòng {room['ten_phong']} chưa có người thuê. Vui lòng cập nhật người thuê trước.")
            # Reset combo box selection
            self.room_combo.setCurrentIndex(0)

    def update_room_tenant_info(self, room, tenant):
        """Update the UI with room and tenant info"""
        info_mapping = {
            "Tên phòng": room['ten_phong'],
            "Mã phòng": room['id'],
            "Người thuê": tenant['ho_ten'],
            "CCCD": tenant['cccd'],
            "Địa chỉ": room.get('dia_chi', '---'),
            "Giá phòng": f"{room['gia_phong']} VNĐ",
            "Giá điện": f"{room['gia_dien']} VNĐ/kWh",
            "Giá nước": f"{room['gia_nuoc']} VNĐ/người",
            "Internet": f"{room.get('internet', '100000')} VNĐ",
            "Phí khác": f"{room.get('phi_khac', '20000')} VNĐ",
            "Số điện cũ": room.get('chi_so_dien', '---'),
            "Số nước cũ": room.get('chi_so_nuoc', '---'),
        }

        # Update all labels with the new information
        for key, value in info_mapping.items():
            if key in self.labels:
                self.labels[key].setText(str(value))

    def reset_form(self):
        """Reset all input fields"""
        self.dien_input.clear()
        self.nuoc_input.clear()
        self.phi_khac_input.clear()

        # Reset to default values if available
        if self.selected_room:
            if 'phi_khac' in self.selected_room:
                self.phi_khac_input.setText(str(self.selected_room['phi_khac']))

    def on_export_clicked(self):
        """Validate inputs and proceed to invoice preview"""
        # Validate inputs
        try:
            # Check if fields are not empty
            if not self.dien_input.text() or not self.nuoc_input.text() or not self.songuoi_input.text():
                QMessageBox.warning(self, "Thiếu thông tin",
                                    "Vui lòng nhập đầy đủ thông tin chỉ số điện, nước và số người ở.")
                return

            chi_so_dien = float(self.dien_input.text())
            chi_so_nuoc = float(self.nuoc_input.text())
            phi_khac = float(self.phi_khac_input.text() or self.selected_room.get('phi_khac', 20000))

            # Additional validation
            old_dien = float(self.selected_room.get('chi_so_dien', 0))
            old_nuoc = float(self.selected_room.get('chi_so_nuoc', 0))

            if chi_so_dien < old_dien:
                raise ValueError("Chỉ số điện mới không thể nhỏ hơn chỉ số cũ")

            if chi_so_nuoc < old_nuoc:
                raise ValueError("Chỉ số nước mới không thể nhỏ hơn chỉ số cũ")

        except ValueError as e:
            error_msg = str(e) if str(e) else "Vui lòng nhập đúng định dạng cho các trường số."
            QMessageBox.warning(self, "Lỗi nhập liệu", error_msg)
            return

        invoice_data = {
            'room': self.selected_room,
            'tenant': self.selected_tenant,
            'chi_so_dien': chi_so_dien,
            'chi_so_nuoc': chi_so_nuoc,

            'phi_khac': phi_khac
        }

        self.go_to_preview_callback(invoice_data)