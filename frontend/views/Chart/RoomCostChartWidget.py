from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle

class RoomCostChartWidget(QWidget):
    def __init__(self, monthly_data, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.figure = Figure(figsize=(10, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.apply_global_style_matplotlib()
        if monthly_data and len(monthly_data) > 0:
            self.plot(monthly_data)
        else:
            self.plot_empty()

    def apply_global_style_matplotlib(self):
        plt.rcParams.update({
            "font.family": "sans-serif",
            "font.sans-serif": ["Be Vietnam Pro", "Inter", "Arial", "sans-serif"],
            "axes.titlesize": 14,
            "axes.labelsize": 12,
            "axes.labelcolor": GlobalStyle.TEXT_COLOR,
            "axes.edgecolor": "#E0E4EF",
            "axes.facecolor": GlobalStyle.MAIN_BG,
            "axes.titleweight": "bold",
            "xtick.color": GlobalStyle.TEXT_COLOR,
            "ytick.color": GlobalStyle.TEXT_COLOR,
            "figure.facecolor": GlobalStyle.MAIN_BG,
            "savefig.facecolor": GlobalStyle.MAIN_BG,
            "grid.color": "#E0E4EF",
        })

    def plot(self, monthly_data):
        try:
            months = [item['month'] for item in monthly_data]
            num_electricity = [item['num_electricity'] for item in monthly_data]
            num_water = [item['num_water'] for item in monthly_data]
            total = [item['total'] for item in monthly_data]

            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(months, num_electricity, marker='o', color='#2158B6', label='Số điện', linewidth=2)
            ax.plot(months, num_water, marker='s', color='#3DB2FF', label='Số nước', linewidth=2)
            ax.plot(months, total, marker='D', color='#F6645A', label='Tổng', linewidth=2)

            ax.set_facecolor("#F5F5FA")
            self.figure.set_facecolor(GlobalStyle.MAIN_BG)
            ax.set_title("Chỉ số điện/nước và tổng thu phòng", fontsize=16, fontweight='bold', color=GlobalStyle.TEXT_COLOR, pad=20)
            ax.set_xlabel("Tháng", fontsize=13, color=GlobalStyle.TEXT_COLOR)
            ax.set_ylabel("Giá trị", fontsize=13, color=GlobalStyle.TEXT_COLOR)
            ax.yaxis.set_major_formatter(plt.FuncFormatter(self.format_currency))
            plt.setp(ax.get_xticklabels(), rotation=35, ha="right")
            ax.grid(True, alpha=0.25)
            for spine in ax.spines.values():
                spine.set_edgecolor("#E0E4EF")
                spine.set_linewidth(1.2)
            ax.legend()
            self.figure.tight_layout(pad=2)
            self.canvas.draw()
        except Exception as e:
            print(f"Lỗi khi vẽ biểu đồ: {e}")
            self.plot_empty()

    def plot_empty(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.text(0.5, 0.5, 'Không có dữ liệu để hiển thị',
                horizontalalignment='center', verticalalignment='center',
                transform=ax.transAxes, fontsize=14, color=GlobalStyle.TEXT_COLOR)
        ax.set_title("Chỉ số điện/nước và tổng thu phòng", fontsize=15, fontweight='bold', color=GlobalStyle.TEXT_COLOR)
        ax.set_facecolor("#F5F5FA")
        self.figure.set_facecolor(GlobalStyle.MAIN_BG)
        self.figure.tight_layout()
        self.canvas.draw()

    def format_currency(self, x, pos):
        if x >= 1_000_000:
            return f'{x / 1_000_000:.1f}M'
        elif x >= 1_000:
            return f'{x / 1_000:.0f}K'
        else:
            return f'{x:.0f}'
