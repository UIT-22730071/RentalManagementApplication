from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from QLNHATRO.RentalManagementApplication.frontend.Component.DashboardCard import DashboardCard
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.views.Chart.RoomCostChartWidget import RoomCostChartWidget


class RoomsHome(QWidget):
    def __init__(self, main_window, room_id, data_room_home,monthly_data=None):
        super().__init__()

        #TODO cần lắm 1 đối tượng ROOM
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.main_window = main_window
        self.room_id = room_id
        self.data = data_room_home

        if monthly_data is None:
            self.monthly_data = [
        {"month": "01/2024", "num_electricity": 120, "num_water": 15, "total": 700000},
        {"month": "02/2024", "num_electricity": 150, "num_water": 17, "total": 730000},
        {"month": "03/2024", "num_electricity": 130, "num_water": 16, "total": 720000},
        {"month": "04/2024", "num_electricity": 140, "num_water": 18, "total": 750000},
        {"month": "05/2024", "num_electricity": 160, "num_water": 20, "total": 800000},
        {"month": "06/2024", "num_electricity": 170, "num_water": 22, "total": 850000},
        {"month": "07/2024", "num_electricity": 180, "num_water": 25, "total": 900000},
        {"month": "08/2024", "num_electricity": 190, "num_water": 27, "total": 950000},
        {"month": "09/2024", "num_electricity": 200, "num_water": 30, "total": 1000000},
        {"month": "10/2024", "num_electricity": 210, "num_water": 32, "total": 1050000},
        {"month": "11/2024", "num_electricity": 220, "num_water": 35, "total": 1100000},
        {"month": "12/2024", "num_electricity": 230, "num_water": 37, "total": 1150000}
        ]
        else:
            self.monthly_data = monthly_data

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        #self.setStyleSheet("background-color: #2c3e50; border-radius: 15px; padding: 20px;")

        # ====== Label tiêu đề ======
        title = QLabel(f"📋 THÔNG TIN PHÒNG: {room_id}")
        title.setObjectName("Title")
        title.setFixedHeight(60)
        #title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        #title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        if monthly_data:
            chart_widget = RoomCostChartWidget(monthly_data)
            main_layout.addWidget(chart_widget)
        else:
            chart_placeholder = QLabel("📈 Biểu đồ thu nhập từ phòng này (Hiển thị sau)")
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


        # ====== Placeholder cho biểu đồ thu nhập ======


        # ====== Dashboard Cards: điện, nước, giá điện, giá nước ======
        stats_layout = QHBoxLayout()

        electricity_index_card = DashboardCard("Chỉ số điện", self.data['current_electricity'], self.data['percent_grow_num_electricity'], "icons/electricity.png")
        water_index_card = DashboardCard("Chỉ số nước", self.data['current_water'], self.data['percent_grow_num_water'], "icons/water.png")
        electricity_price_card = DashboardCard("Giá điện", self.data['electricity_price'], self.data['percent_grow_electricity_price'], "icons/price-tag.png")
        water_price_card = DashboardCard("Giá nước", self.data['water_price'], self.data['percent_grow_water_price'], "icons/price-tag.png")

        stats_layout.addWidget(electricity_index_card)
        stats_layout.addWidget(water_index_card)
        stats_layout.addWidget(electricity_price_card)
        stats_layout.addWidget(water_price_card)

        main_layout.addLayout(stats_layout)

        self.setLayout(main_layout)

