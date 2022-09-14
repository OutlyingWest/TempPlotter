import sys
from PySide6.QtWidgets import QApplication
import parser_log as prs
import design

def main():
    path = r'C:\Users\Alex\Work\Projects\VisualStudio\TempPlotter\putty.log'

    # Creation of new data frame
    data_frame = prs.DataFrame(12)

    # Set path to log file
    data_frame.set_path(path)

    # Get and parse data from log
    sensors = data_frame.get_structured_data()

    # Show data in console
    # data_frame.show_sensors_data()
    # data_frame.show_sensors_structured_data()

    prs.clean_data_saver(sensors)

    # Interface
    app = QApplication()
    main_window = design.MainWindow(sensors)
    main_window.show()
    sys.exit(app.exec())
    


if __name__ == "__main__":
    main()
