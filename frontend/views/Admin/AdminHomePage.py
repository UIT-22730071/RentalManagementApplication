from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from QLNHATRO.RentalManagementApplication.frontend.Component.DashboardCard import DashboardCard

class AdminHome(QWidget):
    def __init__(self, main_window=None, summary_data=None, chart=None):
        super().__init__()
        self.main_window = main_window
        self.summary_data = summary_data or {
            "num_landlords": 0,
            "num_tenants": 0,
            "num_rooms": 0,
            "num_paid_invoices": 0
        }
        self.chart = chart

        self.setStyleSheet("background-color: #2c3e50; border-radius: 15px; padding: 20px;")
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)

        # Tiêu đề chính
        title = QLabel("📊 THỐNG KÊ HỆ THỐNG")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Biểu đồ placeholder
        chart_placeholder = QLabel("🔶 Biểu đồ phân tích hệ thống (Hiển thị sau)")
        chart_placeholder.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        chart_placeholder.setStyleSheet("""
            background-color: #1F1F1F;
            color: white;
            padding: 80px;
            border-radius: 15px;
            font-size: 18px;
        """)
        chart_placeholder.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(chart_placeholder)

        # Card thống kê
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(20)

        landlord_card = DashboardCard("Chủ trọ", str(self.summary_data["num_landlords"]), "0%")
        tenant_card = DashboardCard("Người thuê", str(self.summary_data["num_tenants"]), "0%")
        room_card = DashboardCard("Phòng trọ", str(self.summary_data["num_rooms"]), "0%")
        invoice_card = DashboardCard("Hóa đơn đã thanh toán", str(self.summary_data["num_paid_invoices"]), "0%")

        stats_layout.addWidget(landlord_card)
        stats_layout.addWidget(tenant_card)
        stats_layout.addWidget(room_card)
        stats_layout.addWidget(invoice_card)

        main_layout.addLayout(stats_layout)
        self.setLayout(main_layout)
