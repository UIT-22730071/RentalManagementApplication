import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class ChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure, self.ax = plt.subplots(figsize=(5, 3), facecolor='#1F1F1F')
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.setStyleSheet("background-color: #1F1F1F; border-radius: 15px;")

        self.plot_chart()

    def plot_chart(self):
        """ Vẽ biểu đồ ví dụ """
        months = ["May", "June", "July"]
        values = [150000, 160000, 330000]

        self.ax.clear()
        self.ax.fill_between(months, values, color="#FF6B6B", alpha=0.7)
        self.ax.set_title("Biểu đồ doanh thu", fontsize=12, color="white")
        self.ax.set_facecolor("#1F1F1F")
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')

        self.canvas.draw()
