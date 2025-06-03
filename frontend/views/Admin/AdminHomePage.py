from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from QLNHATRO.RentalManagementApplication.frontend.Component.DashboardCard import DashboardCard
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Chart.AdminSystemChartWidget import AdminSystemChartWidget


class AdminHome(QWidget):
    def __init__(self, main_window=None, summary_data=None, monthly_data=None):
        super().__init__()

        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window
        self.summary_data = summary_data or {
            'num_landlords': 0,
            'percent_landlords': 0.0,
            'num_tenants': 0,
            'percent_tenants': 0.0,
            'num_rooms': 0,
            'percent_rooms': 0.0,
            'num_paid_invoices': 0,
            'percent_paid_invoices': 0.0
        }

        if monthly_data is None:
            self.monthly_data = [
            {"month": "01/2024", "landlord": 2, "tenant": 5, "room": 8, "invoice": 15},
            {"month": "02/2024", "landlord": 3, "tenant": 6, "room": 10, "invoice": 16},
            {"month": "03/2024", "landlord": 4, "tenant": 8, "room": 13, "invoice": 20},
            {"month": "04/2024", "landlord": 4, "tenant": 10, "room": 15, "invoice": 24},
            {"month": "05/2024", "landlord": 5, "tenant": 11, "room": 18, "invoice": 28},
            {"month": "06/2024", "landlord": 6, "tenant": 13, "room": 20, "invoice": 32},
            {"month": "07/2024", "landlord": 7, "tenant": 15, "room": 22, "invoice": 35},
            {"month": "08/2024", "landlord": 8, "tenant": 17, "room": 25, "invoice": 40},
            {"month": "09/2024", "landlord": 9, "tenant": 20, "room": 28, "invoice": 45},
            {"month": "10/2024", "landlord": 10, "tenant": 22, "room": 30, "invoice": 50}]
        else:
            self.monthly_data = monthly_data


        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)

        # Tiêu đề chính
        title = QLabel("📊 THỐNG KÊ HỆ THỐNG")
        #title.setStyleSheet("font-size: 24px; font-weight: bold;")
        title.setObjectName("Title")
        title.setFixedHeight(60)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Sau khi set tiêu đề
        if monthly_data:
            chart_widget = AdminSystemChartWidget(monthly_data)
            main_layout.addWidget(chart_widget)
        else:
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

        landlord_card = DashboardCard("Chủ trọ", str(self.summary_data["num_landlords"]), str(self.summary_data["percent_landlords"]))
        tenant_card = DashboardCard("Người thuê", str(self.summary_data["num_tenants"]), str(self.summary_data["percent_tenants"]))
        room_card = DashboardCard("Phòng trọ", str(self.summary_data["num_rooms"]), str(self.summary_data["percent_rooms"]))
        invoice_card = DashboardCard("Hóa đơn đã thanh toán", str(self.summary_data["num_paid_invoices"]), str(self.summary_data["percent_paid_invoices"]))

        stats_layout.addWidget(landlord_card)
        stats_layout.addWidget(tenant_card)
        stats_layout.addWidget(room_card)
        stats_layout.addWidget(invoice_card)

        main_layout.addLayout(stats_layout)
        self.setLayout(main_layout)
