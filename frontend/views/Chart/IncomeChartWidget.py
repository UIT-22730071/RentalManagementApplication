from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class IncomeChartWidget(QWidget):
    def __init__(self, monthly_income, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        # Tạo figure với kích thước phù hợp và DPI cao hơn
        self.figure = Figure(figsize=(10, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Kiểm tra dữ liệu trước khi vẽ
        if monthly_income and len(monthly_income) > 0:
            self.plot(monthly_income)
        else:
            self.plot_empty()

    def plot(self, monthly_income):
        try:
            # Lấy dữ liệu
            months = [item['month'] for item in monthly_income]
            values = [item['total_income'] for item in monthly_income]

            # Xóa các plot cũ
            self.figure.clear()

            # Tạo subplot
            ax = self.figure.add_subplot(111)

            # Vẽ biểu đồ
            ax.plot(months, values, marker='o', color='#2158B6', linewidth=2, markersize=6)

            # Thiết lập tiêu đề và labels
            ax.set_title("Thu nhập hàng tháng", fontsize=14, fontweight='bold', pad=20)
            ax.set_xlabel("Tháng", fontsize=12)
            ax.set_ylabel("Thu nhập (VNĐ)", fontsize=12)

            # Format trục Y để hiển thị số tiền dễ đọc
            ax.yaxis.set_major_formatter(plt.FuncFormatter(self.format_currency))

            # Xoay label tháng để dễ đọc
            plt.setp(ax.get_xticklabels(), rotation=45)

            # Thêm grid
            ax.grid(True, alpha=0.3)

            # Tối ưu layout
            self.figure.tight_layout()

            # Refresh canvas
            self.canvas.draw()

        except Exception as e:
            print(f"Lỗi khi vẽ biểu đồ: {e}")
            self.plot_empty()

    def plot_empty(self):
        """Vẽ biểu đồ trống khi không có dữ liệu"""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.text(0.5, 0.5, 'Không có dữ liệu để hiển thị',
                horizontalalignment='center', verticalalignment='center',
                transform=ax.transAxes, fontsize=14)
        ax.set_title("Thu nhập hàng tháng", fontsize=14, fontweight='bold')
        self.figure.tight_layout()
        self.canvas.draw()

    def format_currency(self, x, pos):
        """Format số tiền thành định dạng dễ đọc"""
        if x >= 1_000_000:
            return f'{x / 1_000_000:.1f}M'
        elif x >= 1_000:
            return f'{x / 1_000:.0f}K'
        else:
            return f'{x:.0f}'