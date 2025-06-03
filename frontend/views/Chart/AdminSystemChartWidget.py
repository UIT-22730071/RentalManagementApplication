from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle

class AdminSystemChartWidget(QWidget):
    def __init__(self, monthly_data, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.figure = Figure(figsize=(14, 6), dpi=100)
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
            landlords = [item['landlord'] for item in monthly_data]
            tenants = [item['tenant'] for item in monthly_data]
            rooms = [item['room'] for item in monthly_data]
            invoices = [item['invoice'] for item in monthly_data]

            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(months, landlords, marker='o', color='#2158B6', label='Chủ trọ', linewidth=2)
            ax.plot(months, tenants, marker='s', color='#3DB2FF', label='Người thuê', linewidth=2)
            ax.plot(months, rooms, marker='D', color='#F6645A', label='Phòng trọ', linewidth=2)
            ax.plot(months, invoices, marker='^', color='#62C370', label='Hóa đơn', linewidth=2)

            ax.set_facecolor("#F5F5FA")
            self.figure.set_facecolor(GlobalStyle.MAIN_BG)
            ax.set_title("Thống kê hệ thống theo tháng", fontsize=16, fontweight='bold', color=GlobalStyle.TEXT_COLOR, pad=20)
            ax.set_xlabel("Tháng", fontsize=13, color=GlobalStyle.TEXT_COLOR)
            ax.set_ylabel("Số lượng", fontsize=13, color=GlobalStyle.TEXT_COLOR)
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
        ax.set_title("Thống kê hệ thống theo tháng", fontsize=15, fontweight='bold', color=GlobalStyle.TEXT_COLOR)
        ax.set_facecolor("#F5F5FA")
        self.figure.set_facecolor(GlobalStyle.MAIN_BG)
        self.figure.tight_layout()
        self.canvas.draw()
