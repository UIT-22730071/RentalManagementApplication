from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTabWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


class AnalyticsChartWidget(QWidget):
    def __init__(self, analytics_data, parent=None):
        super().__init__(parent)
        self.analytics_data = analytics_data

        # Layout chính
        main_layout = QVBoxLayout(self)

        # Tạo tab widget để chuyển đổi giữa các biểu đồ
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        if analytics_data:
            self.create_all_charts()
        else:
            self.create_empty_chart()

    def create_all_charts(self):
        """Tạo tất cả các biểu đồ trong các tab khác nhau"""

        # Tab 1: Thu nhập hàng tháng
        income_widget = self.create_income_chart()
        self.tab_widget.addTab(income_widget, "📈 Thu nhập")

        # Tab 2: Số phòng đã thuê
        rooms_widget = self.create_rooms_chart()
        self.tab_widget.addTab(rooms_widget, "🏠 Phòng thuê")

        # Tab 3: Giá thuê trung bình
        price_widget = self.create_price_chart()
        self.tab_widget.addTab(price_widget, "💰 Giá thuê")

        # Tab 4: Tỷ lệ tăng trưởng
        growth_widget = self.create_growth_chart()
        self.tab_widget.addTab(growth_widget, "📊 Tăng trưởng")

        # Tab 5: Tổng quan (multiple charts)
        overview_widget = self.create_overview_chart()
        self.tab_widget.addTab(overview_widget, "🔍 Tổng quan")

    def create_income_chart(self):
        """Biểu đồ thu nhập hàng tháng"""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        figure = Figure(figsize=(10, 6), dpi=100)
        canvas = FigureCanvas(figure)
        layout.addWidget(canvas)

        try:
            months = [item['month'] for item in self.analytics_data['monthly_income']]
            values = [item['total_income'] for item in self.analytics_data['monthly_income']]

            ax = figure.add_subplot(111)

            # Vẽ biểu đồ cột và đường
            bars = ax.bar(months, values, alpha=0.7, color='#3498db', label='Thu nhập')
            line = ax.plot(months, values, marker='o', color='#e74c3c', linewidth=2, markersize=6, label='Xu hướng')

            # Thêm giá trị lên từng cột
            for bar, value in zip(bars, values):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2., height + height * 0.01,
                        f'{value / 1_000_000:.1f}M',
                        ha='center', va='bottom', fontsize=9)

            ax.set_title("Thu nhập hàng tháng", fontsize=16, fontweight='bold', pad=20)
            ax.set_xlabel("Tháng", fontsize=12)
            ax.set_ylabel("Thu nhập (VNĐ)", fontsize=12)
            ax.yaxis.set_major_formatter(plt.FuncFormatter(self.format_currency))
            plt.setp(ax.get_xticklabels(), rotation=45)
            ax.grid(True, alpha=0.3)
            ax.legend()

            figure.tight_layout()
            canvas.draw()

        except Exception as e:
            print(f"Lỗi tạo biểu đồ thu nhập: {e}")

        return widget

    def create_rooms_chart(self):
        """Biểu đồ số phòng đã thuê"""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        figure = Figure(figsize=(10, 6), dpi=100)
        canvas = FigureCanvas(figure)
        layout.addWidget(canvas)

        try:
            months = [item['month'] for item in self.analytics_data['room_occupancy']]
            rooms = [item['rented_rooms'] for item in self.analytics_data['room_occupancy']]

            ax = figure.add_subplot(111)

            # Biểu đồ cột
            bars = ax.bar(months, rooms, color='#2ecc71', alpha=0.8)

            # Thêm số lượng lên từng cột
            for bar, value in zip(bars, rooms):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
                        f'{value}',
                        ha='center', va='bottom', fontsize=10, fontweight='bold')

            ax.set_title("Số phòng đã cho thuê", fontsize=16, fontweight='bold', pad=20)
            ax.set_xlabel("Tháng", fontsize=12)
            ax.set_ylabel("Số phòng", fontsize=12)
            ax.set_ylim(0, max(rooms) + 2)
            plt.setp(ax.get_xticklabels(), rotation=45)
            ax.grid(True, alpha=0.3)

            figure.tight_layout()
            canvas.draw()

        except Exception as e:
            print(f"Lỗi tạo biểu đồ phòng: {e}")

        return widget

    def create_price_chart(self):
        """Biểu đồ giá thuê trung bình"""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        figure = Figure(figsize=(10, 6), dpi=100)
        canvas = FigureCanvas(figure)
        layout.addWidget(canvas)

        try:
            months = [item['month'] for item in self.analytics_data['average_price']]
            prices = [item['average_price'] for item in self.analytics_data['average_price']]

            ax = figure.add_subplot(111)

            # Biểu đồ đường với area fill
            ax.plot(months, prices, marker='s', color='#f39c12', linewidth=3, markersize=8)
            ax.fill_between(months, prices, alpha=0.3, color='#f39c12')

            ax.set_title("Giá thuê trung bình", fontsize=16, fontweight='bold', pad=20)
            ax.set_xlabel("Tháng", fontsize=12)
            ax.set_ylabel("Giá thuê (VNĐ)", fontsize=12)
            ax.yaxis.set_major_formatter(plt.FuncFormatter(self.format_currency))
            plt.setp(ax.get_xticklabels(), rotation=45)
            ax.grid(True, alpha=0.3)

            figure.tight_layout()
            canvas.draw()

        except Exception as e:
            print(f"Lỗi tạo biểu đồ giá: {e}")

        return widget

    def create_growth_chart(self):
        """Biểu đồ tỷ lệ tăng trưởng"""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        figure = Figure(figsize=(10, 6), dpi=100)
        canvas = FigureCanvas(figure)
        layout.addWidget(canvas)

        try:
            months = [item['month'] for item in self.analytics_data['growth_rate']]
            growth = [item['growth_rate'] for item in self.analytics_data['growth_rate']]

            ax = figure.add_subplot(111)

            # Màu sắc theo giá trị (xanh nếu dương, đỏ nếu âm)
            colors = ['#27ae60' if g >= 0 else '#e74c3c' for g in growth]
            bars = ax.bar(months, growth, color=colors, alpha=0.8)

            # Thêm giá trị lên từng cột
            for bar, value in zip(bars, growth):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2.,
                        height + (0.2 if height >= 0 else -0.5),
                        f'{value:.1f}%',
                        ha='center', va='bottom' if height >= 0 else 'top',
                        fontsize=9, fontweight='bold')

            ax.set_title("Tỷ lệ tăng trưởng hàng tháng", fontsize=16, fontweight='bold', pad=20)
            ax.set_xlabel("Tháng", fontsize=12)
            ax.set_ylabel("Tỷ lệ tăng trưởng (%)", fontsize=12)
            ax.axhline(y=0, color='black', linestyle='-', alpha=0.3)
            plt.setp(ax.get_xticklabels(), rotation=45)
            ax.grid(True, alpha=0.3)

            figure.tight_layout()
            canvas.draw()

        except Exception as e:
            print(f"Lỗi tạo biểu đồ tăng trưởng: {e}")

        return widget

    def create_overview_chart(self):
        """Biểu đồ tổng quan - 4 biểu đồ nhỏ trong 1"""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        figure = Figure(figsize=(12, 8), dpi=100)
        canvas = FigureCanvas(figure)
        layout.addWidget(canvas)

        try:
            # Tạo 4 subplot
            months = [item['month'] for item in self.analytics_data['raw_data']]
            income = [item['total_income'] for item in self.analytics_data['raw_data']]
            rooms = [item['rented_rooms'] for item in self.analytics_data['raw_data']]
            prices = [item['average_price'] for item in self.analytics_data['raw_data']]
            growth = [item['growth_rate'] for item in self.analytics_data['raw_data']]

            # Thu nhập
            ax1 = figure.add_subplot(2, 2, 1)
            ax1.plot(months, income, marker='o', color='#3498db', linewidth=2)
            ax1.set_title("Thu nhập", fontweight='bold')
            ax1.tick_params(axis='x', rotation=45)
            ax1.grid(True, alpha=0.3)

            # Số phòng
            ax2 = figure.add_subplot(2, 2, 2)
            ax2.bar(months, rooms, color='#2ecc71', alpha=0.8)
            ax2.set_title("Số phòng thuê", fontweight='bold')
            ax2.tick_params(axis='x', rotation=45)
            ax2.grid(True, alpha=0.3)

            # Giá trung bình
            ax3 = figure.add_subplot(2, 2, 3)
            ax3.plot(months, prices, marker='s', color='#f39c12', linewidth=2)
            ax3.fill_between(months, prices, alpha=0.3, color='#f39c12')
            ax3.set_title("Giá thuê TB", fontweight='bold')
            ax3.tick_params(axis='x', rotation=45)
            ax3.grid(True, alpha=0.3)

            # Tăng trưởng
            ax4 = figure.add_subplot(2, 2, 4)
            colors = ['#27ae60' if g >= 0 else '#e74c3c' for g in growth]
            ax4.bar(months, growth, color=colors, alpha=0.8)
            ax4.axhline(y=0, color='black', linestyle='-', alpha=0.3)
            ax4.set_title("Tăng trưởng (%)", fontweight='bold')
            ax4.tick_params(axis='x', rotation=45)
            ax4.grid(True, alpha=0.3)

            figure.suptitle("Tổng quan Analytics", fontsize=16, fontweight='bold')
            figure.tight_layout()
            canvas.draw()

        except Exception as e:
            print(f"Lỗi tạo biểu đồ tổng quan: {e}")

        return widget

    def create_empty_chart(self):
        """Tạo biểu đồ trống khi không có dữ liệu"""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        figure = Figure(figsize=(10, 6), dpi=100)
        canvas = FigureCanvas(figure)
        layout.addWidget(canvas)

        ax = figure.add_subplot(111)
        ax.text(0.5, 0.5, 'Không có dữ liệu analytics để hiển thị',
                horizontalalignment='center', verticalalignment='center',
                transform=ax.transAxes, fontsize=16)
        ax.set_title("Analytics Dashboard", fontsize=16, fontweight='bold')

        figure.tight_layout()
        canvas.draw()

        self.tab_widget.addTab(widget, "Không có dữ liệu")

    def format_currency(self, x, pos):
        """Format số tiền thành định dạng dễ đọc"""
        if x >= 1_000_000:
            return f'{x / 1_000_000:.1f}M'
        elif x >= 1_000:
            return f'{x / 1_000:.0f}K'
        else:
            return f'{x:.0f}'