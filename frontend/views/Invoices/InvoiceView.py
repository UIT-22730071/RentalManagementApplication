# InvoiceView.py
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QScrollArea, QFrame, QGridLayout, QGroupBox, QTableWidget,
                             QTableWidgetItem, QHeaderView)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont



class InvoiceView(QWidget):
    invoice_saved = pyqtSignal(int)  # Signal to emit when invoice is saved

    #TODO : có nhiều lỗi UI
    # giới hạn kích thươc view Chữ ký xác nhận và từng vị trí view bên trong
    # Bổ sung thêm các giá trị tiền thuê khác nếu có, chi phí internet,... bla bla
    # Thoong tin người mua bổ sung thêm sđt, bỏ phần hình thức thanh toán
    # Nếu ổn tạo phương thức thanh toán qua qét mã QR trong teanat thì quá Oke la rồi
    #
    def __init__(self, main_window=None, invoice_data=None, landlord_data=None, tenant_data=None, room_data=None):
        super().__init__()
        self.main_window = main_window

        # Set default data if not provided
        #invoice_code viết hàm tạo mã số ngẫu hiên cho phần ký hiệu hóa đơn (string)
        # số hóa đơn lấy id hóa đơn (int)
        # date - hiển thị ngày today()
        self.invoice_data = invoice_data or {
            'invoice_id': 123,
            'invoice_code': '1C21TAA',
            'date': datetime.now().strftime('%d/%m/%Y'),
            'prev_electric': 0,
            'curr_electric': 0,
            'prev_water': 0,
            'curr_water': 0,
            'room_price': 0,
            'electric_price': 0,
            'internet_fee':0,
            'water_price': 0,
            'garbage_fee': 0
        }

        self.landlord_data = landlord_data or {
            'name': 'Chưa có dữ liệu',
            'cccd': 'Đang cập nhật',
            'address': 'Khu Phố 6, Phường Linh Trung, Thành phố Thủ Đức, TP Hồ Chí Minh',
            'phone': 'Chưa có dữ liệu'
        }

        self.tenant_data = tenant_data or {
            'full_name': 'Chưa có dữ liệu',
            'citizen_id': 'Chưa có dữ liệu',
            'address': 'Khu Phố 6, Phường Linh Trung, Thành phố Thủ Đức, TP Hồ Chí Minh',
            'phone': 'Chưa có dữ liệu'
        }

        self.room_data = room_data or {
            'room_name': 'Chưa có dữ liệu'
        }

        self.initUI()
        self.calculateTotals()

    def initUI(self):
        self.setWindowTitle("HÓA ĐƠN GIÁ TRỊ GIA TĂNG")
        self.setMinimumSize(800, 900)

        # Gradient background like RoomsInfor class
        self.setStyleSheet(
            "QWidget { background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFDEE9, stop:1 #B5FFFC); }")

        main_layout = QVBoxLayout(self)

        # Create scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # Card container for invoice
        card = QFrame()
        card.setStyleSheet("QFrame { background: white; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(20, 20, 20, 20)

        # ===== HEADER SECTION =====
        self.createHeaderSection(card_layout)

        # ===== SELLER INFORMATION =====
        self.createSellerSection(card_layout)

        # ===== BUYER INFORMATION =====
        self.createBuyerSection(card_layout)

        # ===== INVOICE ITEMS TABLE =====
        self.createInvoiceTable(card_layout)

        # ===== TOTALS SECTION =====
        self.createTotalsSection(card_layout)

        # ===== SIGNATURE SECTION =====
        self.createSignatureSection(card_layout)

        # ===== FOOTER SECTION =====
        self.createFooterSection(card_layout)

        scroll_layout.addWidget(card)
        scroll.setWidget(scroll_content)
        main_layout.addWidget(scroll)

        # Bottom action buttons
        self.createActionButtons(main_layout)

    def createHeaderSection(self, parent_layout):
        # Title
        title = QLabel("📝 HÓA ĐƠN GIÁ TRỊ GIA TĂNG")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setStyleSheet("color: white; background-color: #2C3E50; border-radius: 10px; padding: 10px;")
        title.setAlignment(Qt.AlignCenter)
        parent_layout.addWidget(title)

        # Invoice code and number
        header_layout = QGridLayout()
        header_layout.addWidget(QLabel(""), 0, 0)

        invoice_code = QLabel(f"Ký hiệu: {self.invoice_data['invoice_code']}") # hiển thị ký hiệu
        invoice_code.setStyleSheet("font-weight: bold; font-size: 14px;")
        invoice_code.setAlignment(Qt.AlignRight)
        header_layout.addWidget(invoice_code, 0, 1)

        header_layout.addWidget(QLabel(""), 1, 0)

        invoice_number = QLabel(f"Số: {self.invoice_data['invoice_id']}")
        invoice_number.setStyleSheet("font-weight: bold; font-size: 14px;")
        invoice_number.setAlignment(Qt.AlignRight)
        header_layout.addWidget(invoice_number, 1, 1)

        parent_layout.addLayout(header_layout)

        # Date
        date_layout = QHBoxLayout()
        date_label = QLabel(f"Ngày: {self.invoice_data['date']}")
        date_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        date_label.setAlignment(Qt.AlignCenter)
        date_layout.addStretch()
        date_layout.addWidget(date_label)
        date_layout.addStretch()
        parent_layout.addLayout(date_layout)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("background-color: #3498db;")
        parent_layout.addWidget(separator)

    def createSellerSection(self, parent_layout):
        seller_group = QGroupBox("📋 Thông tin người bán")
        seller_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold; border: 1px solid #3498db;
                border-radius: 10px; margin-top: 15px; padding-top: 15px;
                background-color: #f2f9fb;
            }
            QGroupBox::title {
                subcontrol-origin: margin; left: 10px;
                padding: 0 10px; font-size: 16px;
                background-color: white; border-radius: 5px; color: #2c3e50;
            }
        """)

        seller_layout = QVBoxLayout(seller_group)

        # Seller name
        name_layout = QHBoxLayout()
        name_label = QLabel("Tên người bán:")
        name_label.setStyleSheet("font-weight: bold;")
        name_value = QLabel(self.landlord_data['name'])
        name_layout.addWidget(name_label)
        name_layout.addWidget(name_value)
        name_layout.addStretch()
        seller_layout.addLayout(name_layout)

        # Tax code
        tax_layout = QHBoxLayout()
        tax_label = QLabel("Mã số CCCD:")
        tax_label.setStyleSheet("font-weight: bold;")
        tax_value = QLabel(self.landlord_data['cccd'])
        tax_layout.addWidget(tax_label)
        tax_layout.addWidget(tax_value)
        tax_layout.addStretch()
        seller_layout.addLayout(tax_layout)

        # Address
        address_layout = QHBoxLayout()
        address_label = QLabel("Địa chỉ:")
        address_label.setStyleSheet("font-weight: bold;")
        address_value = QLabel(self.landlord_data['address'])
        address_value.setWordWrap(True)
        address_layout.addWidget(address_label)
        address_layout.addWidget(address_value, 1)
        seller_layout.addLayout(address_layout)

        # Phone & Bank account
        contact_layout = QHBoxLayout()
        phone_label = QLabel("Điện thoại:")
        phone_label.setStyleSheet("font-weight: bold;")
        phone_value = QLabel(self.landlord_data['phone'])
        contact_layout.addWidget(phone_label)
        contact_layout.addWidget(phone_value)
        contact_layout.addStretch()

        #bank_label = QLabel("Số tài khoản:")
        #bank_label.setStyleSheet("font-weight: bold;")
        #bank_value = QLabel(self.landlord_data['bank_account'])

        #contact_layout.addWidget(bank_label)
        #contact_layout.addWidget(bank_value)

        seller_layout.addLayout(contact_layout)
        parent_layout.addWidget(seller_group)

    def createBuyerSection(self, parent_layout):
        buyer_group = QGroupBox("👥 Thông tin người mua")
        buyer_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold; border: 1px solid #3498db;
                border-radius: 10px; margin-top: 15px; padding-top: 15px;
                background-color: #f2f9fb;
            }
            QGroupBox::title {
                subcontrol-origin: margin; left: 10px;
                padding: 0 10px; font-size: 16px;
                background-color: white; border-radius: 5px; color: #2c3e50;
            }
        """)

        buyer_layout = QVBoxLayout(buyer_group)

        # Buyer name
        name_layout = QHBoxLayout()
        name_label = QLabel("Họ tên người mua:")
        name_label.setStyleSheet("font-weight: bold;")
        name_value = QLabel(self.tenant_data['full_name'])
        name_layout.addWidget(name_label)
        name_layout.addWidget(name_value)
        name_layout.addStretch()
        buyer_layout.addLayout(name_layout)

        # ID
        id_layout = QHBoxLayout()
        id_label = QLabel("Mã số CCCD:")
        id_label.setStyleSheet("font-weight: bold;")
        id_value = QLabel(self.tenant_data['citizen_id'])
        id_layout.addWidget(id_label)
        id_layout.addWidget(id_value)
        id_layout.addStretch()
        buyer_layout.addLayout(id_layout)

        # Address
        address_layout = QHBoxLayout()
        address_label = QLabel("Địa chỉ:")
        address_label.setStyleSheet("font-weight: bold;")
        address_value = QLabel(self.tenant_data['address'])
        address_value.setWordWrap(True)
        address_layout.addWidget(address_label)
        address_layout.addWidget(address_value, 1)
        buyer_layout.addLayout(address_layout)

        # Payment info
        payment_layout = QHBoxLayout()
        payment_method_label = QLabel("Hình thức thanh toán:")
        payment_method_label.setStyleSheet("font-weight: bold;")
        payment_method_value = QLabel("Tiền mặt")
        payment_layout.addWidget(payment_method_label)
        payment_layout.addWidget(payment_method_value)
        payment_layout.addStretch()

        # Mở chức năng này khi thuực heinej được thanh toán online
        #bank_label = QLabel("Số tài khoản:")
        #bank_label.setStyleSheet("font-weight: bold;")
        #bank_value = QLabel(self.tenant_data['bank_account'])
        #payment_layout.addWidget(bank_label)
        #payment_layout.addWidget(bank_value)
        #payment_layout.addStretch()

        #currency_label = QLabel("Đồng tiền thanh toán:")
        #currency_label.setStyleSheet("font-weight: bold;")
        #currency_value = QLabel(self.tenant_data['currency'])
        #payment_layout.addWidget(currency_label)
        #payment_layout.addWidget(currency_value)

        buyer_layout.addLayout(payment_layout)
        parent_layout.addWidget(buyer_group)

    def createInvoiceTable(self, parent_layout):
        table_group = QGroupBox("🧾 Chi tiết hóa đơn")
        table_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold; border: 1px solid #3498db;
                border-radius: 10px; margin-top: 15px; padding-top: 15px;
                background-color: #f2f9fb;
            }
            QGroupBox::title {
                subcontrol-origin: margin; left: 10px;
                padding: 0 10px; font-size: 16px;
                background-color: white; border-radius: 5px; color: #2c3e50;
            }
            QTableWidget {
                background-color: white;
                gridline-color: #d0d0d0;
                border-radius: 5px;
            }
            QHeaderView::section {
                background-color: #3498db;
                color: white;
                padding: 6px;
                font-weight: bold;
                border: 1px solid #2980b9;
            }
        """)

        table_layout = QVBoxLayout(table_group)

        # Create table
        self.invoice_table = QTableWidget()
        self.invoice_table.setRowCount(4)  # Room price, electric, water, garbage
        self.invoice_table.setColumnCount(9)

        # Set headers
        headers = ["STT", "Tên dịch vụ", "Đơn vị tính", "Số lượng", "Đơn giá",
                   "Thành tiền chưa thuế", "Thuế suất", "Tiền thuế GTGT", "Tổng cộng"]
        self.invoice_table.setHorizontalHeaderLabels(headers)

        # Adjust column widths
        self.invoice_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.invoice_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.invoice_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.invoice_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.invoice_table.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)

        # Populate table with data
        self.populateInvoiceTable()

        table_layout.addWidget(self.invoice_table)
        parent_layout.addWidget(table_group)

    def populateInvoiceTable(self):
        # Calculate values
        # TODO nếu nạp dữ liệu từ service thì chỉnh sửa phần này lại
        electric_used = self.invoice_data['curr_electric'] - self.invoice_data['prev_electric']
        water_used = self.invoice_data['curr_water'] - self.invoice_data['prev_water']

        # Row 1: Room Fee
        self.setTableItem(0, 0, "1")
        self.setTableItem(0, 1, f"Tiền thuê {self.room_data['room_name']}")
        self.setTableItem(0, 2, "Tháng")
        self.setTableItem(0, 3, "1")
        self.setTableItem(0, 4, f"{self.invoice_data['room_price']:,.0f}")

        room_fee_base = self.invoice_data['room_price']
        room_fee_tax = room_fee_base * 0.1
        room_fee_total = room_fee_base + room_fee_tax

        self.setTableItem(0, 5, f"{room_fee_base:,.0f}")
        self.setTableItem(0, 6, "10%")
        self.setTableItem(0, 7, f"{room_fee_tax:,.0f}")
        self.setTableItem(0, 8, f"{room_fee_total:,.0f}")

        # Row 2: Electric Fee
        self.setTableItem(1, 0, "2")
        self.setTableItem(1, 1, "Tiền điện")
        self.setTableItem(1, 2, "kWh")
        self.setTableItem(1, 3, f"{electric_used}")
        self.setTableItem(1, 4, f"{self.invoice_data['electric_price']:,.0f}")

        electric_fee_base = electric_used * self.invoice_data['electric_price']
        electric_fee_tax = electric_fee_base * 0.1
        electric_fee_total = electric_fee_base + electric_fee_tax

        self.setTableItem(1, 5, f"{electric_fee_base:,.0f}")
        self.setTableItem(1, 6, "10%")
        self.setTableItem(1, 7, f"{electric_fee_tax:,.0f}")
        self.setTableItem(1, 8, f"{electric_fee_total:,.0f}")

        # Row 3: Water Fee
        self.setTableItem(2, 0, "3")
        self.setTableItem(2, 1, "Tiền nước")
        self.setTableItem(2, 2, "m³")
        self.setTableItem(2, 3, f"{water_used}")
        self.setTableItem(2, 4, f"{self.invoice_data['water_price']:,.0f}")

        water_fee_base = water_used * self.invoice_data['water_price']
        water_fee_tax = water_fee_base * 0.1
        water_fee_total = water_fee_base + water_fee_tax

        self.setTableItem(2, 5, f"{water_fee_base:,.0f}")
        self.setTableItem(2, 6, "10%")
        self.setTableItem(2, 7, f"{water_fee_tax:,.0f}")
        self.setTableItem(2, 8, f"{water_fee_total:,.0f}")

        # Row 4: Garbage Fee
        self.setTableItem(3, 0, "4")
        self.setTableItem(3, 1, "Phí rác")
        self.setTableItem(3, 2, "Tháng")
        self.setTableItem(3, 3, "1")
        self.setTableItem(3, 4, f"{self.invoice_data['garbage_fee']:,.0f}")

        garbage_fee_base = self.invoice_data['garbage_fee']
        garbage_fee_tax = garbage_fee_base * 0.1
        garbage_fee_total = garbage_fee_base + garbage_fee_tax

        self.setTableItem(3, 5, f"{garbage_fee_base:,.0f}")
        self.setTableItem(3, 6, "10%")
        self.setTableItem(3, 7, f"{garbage_fee_tax:,.0f}")
        self.setTableItem(3, 8, f"{garbage_fee_total:,.0f}")

        # Row 5: Garbage Fee
        self.setTableItem(4, 0, "5")
        self.setTableItem(4, 1, "Phí Internet")
        self.setTableItem(4, 2, "Tháng")
        self.setTableItem(4, 3, "1")
        self.setTableItem(4, 4, f"{self.invoice_data['internet_fee']:,.0f}")

        internet_fee_base = self.invoice_data['internet_fee']
        internet_fee_tax = internet_fee_base
        garbage_fee_total = internet_fee_tax

        self.setTableItem(4, 5, f"{internet_fee_base:,.0f}")
        self.setTableItem(4, 6, "10%")
        self.setTableItem(4, 7, f"{internet_fee_tax:,.0f}")
        self.setTableItem(4, 8, f"{garbage_fee_total:,.0f}")

    def setTableItem(self, row, col, text):
        item = QTableWidgetItem(str(text))
        item.setTextAlignment(Qt.AlignCenter)
        self.invoice_table.setItem(row, col, item)

    def createTotalsSection(self, parent_layout):
        # Calculate totals
        self.calculateTotals()

        totals_group = QGroupBox("💰 Tổng cộng")
        totals_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold; border: 1px solid #3498db;
                border-radius: 10px; margin-top: 15px; padding-top: 15px;
                background-color: #f2f9fb;
            }
            QGroupBox::title {
                subcontrol-origin: margin; left: 10px;
                padding: 0 10px; font-size: 16px;
                background-color: white; border-radius: 5px; color: #2c3e50;
            }
            QLabel {
                padding: 5px;
            }
        """)

        totals_layout = QVBoxLayout(totals_group)

        # Total without tax
        base_layout = QHBoxLayout()
        base_label = QLabel("Tổng tiền chưa có thuế GTGT:")
        base_label.setStyleSheet("font-weight: bold;")
        base_value = QLabel(f"{self.total_base:,.0f} VNĐ")
        base_layout.addWidget(base_label)
        base_layout.addStretch()
        base_layout.addWidget(base_value)
        totals_layout.addLayout(base_layout)

        # Discount
        if self.invoice_data['discount'] > 0:
            discount_layout = QHBoxLayout()
            discount_label = QLabel("Giảm giá:")
            discount_label.setStyleSheet("font-weight: bold; color: #27ae60;")
            discount_value = QLabel(f"-{self.invoice_data['discount']:,.0f} VNĐ")
            discount_value.setStyleSheet("color: #27ae60;")
            discount_layout.addWidget(discount_label)
            discount_layout.addStretch()
            discount_layout.addWidget(discount_value)
            totals_layout.addLayout(discount_layout)

        # Tax
        tax_layout = QHBoxLayout()
        tax_label = QLabel("Tổng tiền thuế GTGT:")
        tax_label.setStyleSheet("font-weight: bold;")
        tax_value = QLabel(f"{self.total_tax:,.0f} VNĐ")
        tax_layout.addWidget(tax_label)
        tax_layout.addStretch()
        tax_layout.addWidget(tax_value)
        totals_layout.addLayout(tax_layout)

        # Total grand
        total_layout = QHBoxLayout()
        total_label = QLabel("Tổng tiền thanh toán:")
        total_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #e74c3c;")
        total_value = QLabel(f"{self.total_amount:,.0f} VNĐ")
        total_value.setStyleSheet("font-weight: bold; font-size: 16px; color: #e74c3c;")
        total_layout.addWidget(total_label)
        total_layout.addStretch()
        total_layout.addWidget(total_value)
        totals_layout.addLayout(total_layout)

        # Amount in words
        words_layout = QHBoxLayout()
        words_label = QLabel("Số tiền viết bằng chữ:")
        words_label.setStyleSheet("font-weight: bold;")
        words_value = QLabel("...")  # This would need a separate function to convert number to words
        words_layout.addWidget(words_label)
        words_layout.addWidget(words_value, 1)
        totals_layout.addLayout(words_layout)

        parent_layout.addWidget(totals_group)

    def calculateTotals(self):
        # Calculate values for invoice table
        electric_used = self.invoice_data['curr_electric'] - self.invoice_data['prev_electric']
        water_used = self.invoice_data['curr_water'] - self.invoice_data['prev_water']

        # Calculate base amounts
        room_fee_base = self.invoice_data['room_price']
        electric_fee_base = electric_used * self.invoice_data['electric_price']
        water_fee_base = water_used * self.invoice_data['water_price']
        garbage_fee_base = self.invoice_data['garbage_fee']

        # Calculate tax amounts
        room_fee_tax = room_fee_base * 0.1
        electric_fee_tax = electric_fee_base * 0.1
        water_fee_tax = water_fee_base * 0.1
        garbage_fee_tax = garbage_fee_base * 0.1

        # Calculate totals
        self.total_base = room_fee_base + electric_fee_base + water_fee_base + garbage_fee_base
        self.total_tax = room_fee_tax + electric_fee_tax + water_fee_tax + garbage_fee_tax

        # Apply discount
        discount = self.invoice_data['discount'] if 'discount' in self.invoice_data else 0
        self.total_amount = self.total_base + self.total_tax - discount

    def createSignatureSection(self, parent_layout):
        signature_group = QGroupBox("✍️ Chữ ký xác nhận")
        signature_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold; border: 1px solid #3498db;
                border-radius: 10px; margin-top: 15px; padding-top: 15px;
                background-color: #f2f9fb;
            }
            QGroupBox::title {
                subcontrol-origin: margin; left: 10px;
                padding: 0 10px; font-size: 16px;
                background-color: white; border-radius: 5px; color: #2c3e50;
            }
        """)

        signature_layout = QHBoxLayout(signature_group)

        # Buyer signature
        buyer_sign = QVBoxLayout()
        buyer_label1 = QLabel("Người mua hàng")
        buyer_label1.setAlignment(Qt.AlignCenter)
        buyer_label1.setStyleSheet("font-weight: bold;")

        buyer_label2 = QLabel("(Ký, ghi rõ họ tên)")
        buyer_label2.setAlignment(Qt.AlignCenter)

        buyer_sign.addWidget(buyer_label1)
        buyer_sign.addWidget(buyer_label2)
        buyer_sign.addStretch(2)  # Space for signature
        signature_layout.addLayout(buyer_sign)

        # Seller signature
        seller_sign = QVBoxLayout()
        seller_label1 = QLabel("Người bán hàng")
        seller_label1.setAlignment(Qt.AlignCenter)
        seller_label1.setStyleSheet("font-weight: bold;")

        seller_label2 = QLabel("(Ký, ghi rõ họ tên)")
        seller_label2.setAlignment(Qt.AlignCenter)

        seller_label3 = QLabel(" ")
        seller_label3.setAlignment(Qt.AlignCenter)

        seller_label4 = QLabel("(đã ký)")
        seller_label4.setAlignment(Qt.AlignCenter)
        seller_label4.setStyleSheet("font-style: italic;")

        seller_sign.addWidget(seller_label1)
        seller_sign.addWidget(seller_label2)
        seller_sign.addWidget(seller_label3)
        seller_sign.addWidget(seller_label4)
        signature_layout.addLayout(seller_sign)

        parent_layout.addWidget(signature_group)

    def createFooterSection(self, parent_layout):
        footer_label = QLabel("(Cần kiểm tra, đối chiếu khi lập, nhận hóa đơn)")
        footer_label.setStyleSheet("color: #7f8c8d; font-style: italic; padding: 10px 0;")
        footer_label.setAlignment(Qt.AlignRight)
        parent_layout.addWidget(footer_label)

    def createActionButtons(self, parent_layout):
        button_layout = QHBoxLayout()

        # Exit button
        exit_btn = QPushButton("Thoát")
        exit_btn.setFixedSize(120, 40)
        exit_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a33025;
            }
        """)
        exit_btn.clicked.connect(self.close)

        # Save button
        save_btn = QPushButton("Xuất hóa đơn")
        save_btn.setFixedSize(120, 40)
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
        save_btn.clicked.connect(self.saveInvoice)

        button_layout.addStretch()
        button_layout.addWidget(exit_btn)
        button_layout.addWidget(save_btn)

        parent_layout.addLayout(button_layout)

    def saveInvoice(self):
        """Lưu và xuất hóa đơn"""
        from PyQt5.QtWidgets import QFileDialog, QMessageBox
        from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
        from PyQt5.QtGui import QPainter, QPixmap

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Lưu Hóa Đơn", f"Hoa_Don_{self.invoice_data['invoice_code']}_{self.invoice_data['invoice_id']}",
            "PDF Files (*.pdf);;PNG Files (*.png);;All Files (*)", options=options
        )

        if file_name:
            try:
                # Determine if we're saving as PDF or PNG
                if file_name.lower().endswith('.pdf'):
                    printer = QPrinter(QPrinter.HighResolution)
                    printer.setOutputFormat(QPrinter.PdfFormat)
                    printer.setOutputFileName(file_name)

                    # Create a painter to paint the widget onto the PDF
                    painter = QPainter()
                    if painter.begin(printer):
                        self.render(painter)
                        painter.end()

                        # Emit signal with invoice ID to notify any listeners
                        self.invoice_saved.emit(self.invoice_data['invoice_id'])

                        QMessageBox.information(self, "Thành công", f"Hóa đơn đã được lưu tại:\n{file_name}")
                    else:
                        QMessageBox.critical(self, "Lỗi", "Không thể tạo file PDF.")

                elif file_name.lower().endswith('.png'):
                    # Capture widget as image
                    pixmap = QPixmap(self.size())
                    self.render(pixmap)

                    # Save as PNG
                    if pixmap.save(file_name, "PNG"):
                        # Emit signal with invoice ID to notify any listeners
                        self.invoice_saved.emit(self.invoice_data['invoice_id'])

                        QMessageBox.information(self, "Thành công", f"Hóa đơn đã được lưu tại:\n{file_name}")
                    else:
                        QMessageBox.critical(self, "Lỗi", "Không thể lưu file PNG.")
                else:
                    QMessageBox.warning(self, "Chú ý",
                                        "Định dạng file không được hỗ trợ. Vui lòng sử dụng .pdf hoặc .png")

            except Exception as e:
                QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi khi lưu hóa đơn: {str(e)}")

    def numberToWords(self, number):
        """Chuyển đổi số thành chữ tiếng Việt"""
        if number == 0:
            return "Không đồng"

        units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
        teens = ["", "mười một", "mười hai", "mười ba", "mười bốn", "mười lăm", "mười sáu", "mười bảy", "mười tám",
                 "mười chín"]
        tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi",
                "chín mươi"]

        def readGroup(num):
            result = ""
            hundred = num // 100
            remainder = num % 100

            if hundred > 0:
                result += units[hundred] + " trăm "

            if remainder > 0:
                if remainder < 10:
                    if hundred > 0:  # Nếu có hàng trăm
                        result += "lẻ "
                    result += units[remainder]
                elif remainder < 20:
                    result += teens[remainder - 10]
                else:
                    ten = remainder // 10
                    unit = remainder % 10
                    result += tens[ten]
                    if unit > 0:
                        if unit == 1:
                            result += " mốt"
                        elif unit == 5:
                            result += " lăm"
                        else:
                            result += " " + units[unit]

            return result.strip()

        result = ""
        billion = number // 1000000000
        million = (number % 1000000000) // 1000000
        thousand = (number % 1000000) // 1000
        remainder = number % 1000

        if billion > 0:
            result += readGroup(billion) + " tỷ "

        if million > 0:
            result += readGroup(million) + " triệu "

        if thousand > 0:
            result += readGroup(thousand) + " nghìn "

        if remainder > 0:
            result += readGroup(remainder)

        return result.strip() + " đồng"


# main.py
import sys
from PyQt5.QtWidgets import QApplication
from datetime import datetime


def main():
    # Create QApplication instance
    app = QApplication(sys.argv)

    # Sample data for invoice
    invoice_data = {
        'invoice_id': 12345,
        'invoice_code': '2B25HCM',
        'date': datetime.now().strftime('%d/%m/%Y'),
        'prev_electric': 1250,
        'curr_electric': 1420,
        'prev_water': 45,
        'curr_water': 52,
        'room_price': 3500000,
        'electric_price': 3500,
        'water_price': 25000,
        'garbage_fee': 50000,
        'discount': 100000
    }

    # Sample landlord data
    landlord_data = {
        'name': 'Nguyễn Văn An',
        'cccd': '8234567890',
        'address': 'Khu Phố 6, Phường Linh Trung, Thành phố Thủ Đức, TP Hồ Chí Minh',
        'phone': '0901234567',
        'bank_account': '314.100.01210304 - Vietcombank'
    }

    # Sample tenant data
    tenant_data = {
        'full_name': 'Trần Thị Bình',
        'citizen_id': '079201012345',
        'address': '123 Đường Nguyễn Văn Cừ, Quận 5, TP Hồ Chí Minh',
        'phone': '098565341',

    }

    # Sample room data
    room_data = {
        'room_name': 'P201'
    }

    # Create and show the invoice view
    invoice_view = InvoiceView(
        invoice_data=invoice_data,
        landlord_data=landlord_data,
        tenant_data=tenant_data,
        room_data=room_data
    )

    # Define a callback function for the invoice_saved signal
    def on_invoice_saved(invoice_id):
        print(f"Invoice #{invoice_id} has been successfully saved!")

    # Connect the signal to the callback
    invoice_view.invoice_saved.connect(on_invoice_saved)

    # Show the window
    invoice_view.show()

    # Start the event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()