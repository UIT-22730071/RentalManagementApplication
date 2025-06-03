from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy, QTableWidget, QTableWidgetItem, \
    QHeaderView
from PyQt5.QtCore import Qt
from QLNHATRO.RentalManagementApplication.frontend.Component.DashboardCard import DashboardCard
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Chart.TenantCostChartWidget import TenantCostChartWidget


class TenantHome(QWidget):
    def __init__(self, main_window=None, id_tenant=None, information_data=None, monthly_data=None):
        super().__init__()
        self.setStyleSheet(GlobalStyle.global_stylesheet())

        self.main_window = main_window
        self.id_tenant = id_tenant
        self.information_data = information_data or {

                    "tien_dien":  str(500000)+" VNĐ",
                        "tien_nuoc":  str(0)+" VNĐ",
                        "tong_chi_phi":  str(0)+" VNĐ",
                        "ngay_den_han":  "0",
                        "percent_dien": str(0)+" %",
                        "percent_nuoc": str(0)+" %",
                        "percent_total": str(0)+" %"
        }
        if monthly_data is None:
            self.monthly_data = [
                {"month": "Tháng 1", "tien_dien": 500000, "tien_nuoc": 200000, "tong": 700000},
                {"month": "Tháng 2", "tien_dien": 600000, "tien_nuoc": 250000, "tong": 850000},
                {"month": "Tháng 3", "tien_dien": 550000, "tien_nuoc": 300000, "tong": 850000},
            ]
        else:
            self.monthly_data=monthly_data

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        #self.setStyleSheet("background-color: #2c3e50; border-radius: 15px; padding: 20px;")


        # Tiêu đề chính
        title = QLabel("📊 THỐNG KÊ TIÊU DÙNG")
        #title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        title.setObjectName("Title")
        title.setFixedHeight(60)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # 1. Thay thế placeholder bằng widget biểu đồ
        if self.monthly_data:
            chart_widget = TenantCostChartWidget(self.monthly_data)
            main_layout.addWidget(chart_widget)
        else:
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


        # Placeholder cho biểu đồ tiền điện tiền nước

        '''
        from QLNHATRO.RentalManagementApplication.backend.Analyst import UtilityChartWidget
        # Thay thế Placeholder bằng biểu đồ tiền điện tiền nước thực tế
        chart_widget = UtilityChartWidget()
        main_layout.addWidget(chart_widget)
        '''

        # Layout chứa các card thống kê
        stats_layout = QHBoxLayout()


        # Thẻ Dashboard cho người thuê
        electricity_card = DashboardCard("Tiền điện", f"{self.information_data['tien_dien']} VNĐ",
                                         f"{self.information_data['percent_dien']}%", "icons/electricity.png")
        water_card = DashboardCard("Tiền nước", f"{self.information_data['tien_nuoc']} VNĐ",
                                   f"{self.information_data['percent_nuoc']}%", "icons/water.png")
        total_cost_card = DashboardCard("Tổng chi phi", f"{self.information_data['tong_chi_phi']} VNĐ",
                                        f"{self.information_data['percent_total']}%", "icons/wifi.png")

        due_date_card = DashboardCard("Ngày đến hạn", str(self.information_data['ngay_den_han']),  str(self.information_data['percent_total']), "icons/calendar.png")

        stats_layout.addWidget(electricity_card)
        stats_layout.addWidget(water_card)
        stats_layout.addWidget(total_cost_card)
        stats_layout.addWidget(due_date_card)

        main_layout.addLayout(stats_layout)


        self.setLayout(main_layout)