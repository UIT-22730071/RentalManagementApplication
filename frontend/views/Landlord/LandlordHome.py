from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt

from QLNHATRO.RentalManagementApplication.frontend.Component.DashboardCard import DashboardCard


class LandlordHome(QWidget):
    def __init__(self, main_window=None, id_lanlord=None, information_data=None,chart = None):
        super().__init__()
        if information_data is None:
            information_data = {
                "total_income": str(0)+" VNĐ",
                "percent_total_income_month": str(0)+" %",
                "total_number_invoice": 0,
                "total_number_room_not_teant": 0,
                "percent_grow_total_income": str(0)+" %",
                "percent_grow_total_not_invoice": str(0)+" %",
                "percent_grow_total_not_tenant": str(0)+" %"
            }
            print("kiểm tra information data None")
        else:
            print("information data không None")
            self.information_data = information_data

        self.chart = chart
        print("[DEBUG] Khởi tạo LandlordHome")
        self.main_window = main_window
        self.id_lanlord = id_lanlord

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        self.setStyleSheet("background-color: #2c3e50; border-radius: 15px; padding: 20px;")

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
        # TODO: nhét chart vào đây
        '''


        # Layout chứa các card thống kê
        stats_layout = QHBoxLayout()

        # Thẻ Dashboard
        income_card = DashboardCard("Tổng thu nhập", str(information_data['total_income']) + " VNĐ", str(information_data['percent_grow_total_income']), "icons/money.png")
        growth_card = DashboardCard("Tỉ lệ tăng thu nhập", str(information_data['percent_total_income_month']), str(information_data['percent_total_income_month']), "icons/growth.png")
        unpaid_card = DashboardCard("Phòng chưa đóng tiền", str(information_data['total_number_invoice']), str(information_data['percent_grow_total_not_invoice']), "icons/warning.png")
        due_soon_card = DashboardCard("Phòng trống", str(information_data['total_number_room_not_teant']), str(information_data['percent_grow_total_not_tenant']), "icons/clock.png")

        stats_layout.addWidget(income_card)
        stats_layout.addWidget(growth_card)
        stats_layout.addWidget(unpaid_card)
        stats_layout.addWidget(due_soon_card)

        main_layout.addLayout(stats_layout)
        self.setLayout(main_layout)
