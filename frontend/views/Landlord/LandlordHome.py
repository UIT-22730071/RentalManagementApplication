from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from QLNHATRO.RentalManagementApplication.frontend.Component.DashboardCard import DashboardCard


class LandlordHome(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        self.setStyleSheet("background-color: #2C2F33; border-radius: 15px; padding: 20px;")

        # Tiêu đề chính
        title = QLabel("📊 THỐNG KÊ TỔNG QUAN")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Placeholder cho biểu đồ (lớn hơn)
        chart_placeholder = QLabel("🔶 Biểu đồ thu nhập hàng tháng (Hiển thị sau)")
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
        '''
        from QLNHATRO.RentalManagementApplication.backend.Analyst import ChartWidget
        # Thay thế Placeholder bằng biểu đồ thực tế
        chart_widget = ChartWidget()
        main_layout.addWidget(chart_widget)
        '''


        # Layout chứa các card thống kê
        stats_layout = QHBoxLayout()

        # Thẻ Dashboard
        income_card = DashboardCard("Tổng thu nhập", "1.04M VNĐ", "+15%", "icons/money.png")
        growth_card = DashboardCard("Tỉ lệ tăng thu nhập", "+15%", "+15%", "icons/growth.png")
        unpaid_card = DashboardCard("Phòng chưa đóng tiền", "3", "-2.5%", "icons/warning.png")
        due_soon_card = DashboardCard("Phòng sắp đến hạn", "2", "+1%", "icons/clock.png")

        stats_layout.addWidget(income_card)
        stats_layout.addWidget(growth_card)
        stats_layout.addWidget(unpaid_card)
        stats_layout.addWidget(due_soon_card)

        main_layout.addLayout(stats_layout)
        self.setLayout(main_layout)
