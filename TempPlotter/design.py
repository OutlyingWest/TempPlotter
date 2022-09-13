
import matplotlib

matplotlib.use('Qt5Agg')

from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QVBoxLayout, QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes_1 = fig.add_subplot(2, 1, 1)
        self.axes_2 = fig.add_subplot(2, 1, 2)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=10, height=4, dpi=90)
        sc.axes_1.plot([0, 1, 2, 3, 5], [1, 10, 3, 20, 40])
        sc.axes_2.plot([0, 1, 2, 3, 5], [10, 1, 20, 3, 40])
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar2QT(sc, self)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
