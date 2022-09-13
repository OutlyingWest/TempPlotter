import matplotlib

matplotlib.use('Qt5Agg')

from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QVBoxLayout, QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

# from parser_log import TmpSensor


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=10, height=6, dpi=100, num_plots=0):
        fig = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)

        # Number of plots in window
        self.num_plots = num_plots

        # List with subplots object instances
        self.axes = []

        # Generate subplots instances list
        for n_plot in range(self.num_plots):
            subplot = fig.add_subplot(self.num_plots, 1, n_plot+1,
                                      ylim=[0, 100],
                                      ylabel="Temp 'C",
                                      xlabel="sec",
                                      )
            subplot.grid()
            self.axes.append(subplot)

        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    '''
        Get the list of tmp sensor instances
    '''
    def __init__(self, sensors : list):
        super(MainWindow, self).__init__()
        self.setWindowTitle("TempPlotter")

        # Set number of plots same with number of temp sensors 
        self.num_plots = len(sensors)
        sc = MplCanvas(self, width=11, height=6, dpi=100, num_plots=self.num_plots)

        # Initilaize subplots
        for axe, sensor in zip(sc.axes, sensors):
            time_seqence = list(range(len(sensor.temp_list)))
            plot_inst, = axe.plot(time_seqence, sensor.temp_list)
            # For show label with number of sensor in legend
            plot_inst.set_label('Sensor ' + str(sensor.number))
            axe.legend()

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar2QT(sc, self)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
