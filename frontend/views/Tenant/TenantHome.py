from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy, QTableWidget, QTableWidgetItem, \
    QHeaderView
from PyQt5.QtCore import Qt
from QLNHATRO.RentalManagementApplication.frontend.Component.DashboardCard import DashboardCard


class TenantHome(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        self.setStyleSheet("background-color: #2c3e50; border-radius: 15px; padding: 20px;")


        # Tiêu đề chính
        title = QLabel("📊 THỐNG KÊ TIÊU DÙNG")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Placeholder cho biểu đồ tiền điện tiền nước
        chart_placeholder = QLabel("🔶 Biểu đồ chi phí điện nước hàng tháng (Hiển thị sau)")
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
        from QLNHATRO.RentalManagementApplication.backend.Analyst import UtilityChartWidget
        # Thay thế Placeholder bằng biểu đồ tiền điện tiền nước thực tế
        chart_widget = UtilityChartWidget()
        main_layout.addWidget(chart_widget)
        '''

        # Layout chứa các card thống kê
        stats_layout = QHBoxLayout()

        # Thẻ Dashboard cho người thuê
        electricity_card = DashboardCard("Tiền điện", "320.000 VNĐ", "+5%", "icons/electricity.png")
        water_card = DashboardCard("Tiền nước", "85.000 VNĐ", "-3%", "icons/water.png")
        total_cost_card = DashboardCard("Tổng chi phi", "2.500.000 VNĐ", "0%", "icons/wifi.png")
        # Thay đổi từ "" sang "0%" để tránh lỗi chuyển đổi
        due_date_card = DashboardCard("Ngày đến hạn", "25/04/2025", "0%", "icons/calendar.png")

        stats_layout.addWidget(electricity_card)
        stats_layout.addWidget(water_card)
        stats_layout.addWidget(total_cost_card)
        stats_layout.addWidget(due_date_card)

        main_layout.addLayout(stats_layout)


        self.setLayout(main_layout)