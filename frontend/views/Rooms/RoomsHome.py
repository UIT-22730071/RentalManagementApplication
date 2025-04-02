from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from QLNHATRO.RentalManagementApplication.frontend.Component.DashboardCard import DashboardCard


class RoomsHome(QWidget):
    def __init__(self, main_window, room_id):
        super().__init__()

        #TODO cần lắm 1 đối tượng ROOM

        self.main_window = main_window
        self.room_id = room_id

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        self.setStyleSheet("background-color: #2c3e50; border-radius: 15px; padding: 20px;")

        # ====== Label tiêu đề ======
        title = QLabel(f"📋 THÔNG TIN PHÒNG: {room_id}")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # ====== Placeholder cho biểu đồ thu nhập ======
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

        # ====== Dashboard Cards: điện, nước, giá điện, giá nước ======
        stats_layout = QHBoxLayout()

        electricity_index_card = DashboardCard("Chỉ số điện", "245 kWh", "+2%", "icons/electricity.png")
        water_index_card = DashboardCard("Chỉ số nước", "32 m³", "+1%", "icons/water.png")
        electricity_price_card = DashboardCard("Giá điện", "3.500 VNĐ/kWh", "0%", "icons/price-tag.png")
        water_price_card = DashboardCard("Giá nước", "12.000 VNĐ/m³", "0%", "icons/price-tag.png")

        stats_layout.addWidget(electricity_index_card)
        stats_layout.addWidget(water_index_card)
        stats_layout.addWidget(electricity_price_card)
        stats_layout.addWidget(water_price_card)

        main_layout.addLayout(stats_layout)

        self.setLayout(main_layout)
