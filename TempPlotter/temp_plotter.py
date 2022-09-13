from PySide6.QtWidgets import QApplication
import parser_log as prs
import design

def main():
    path = r'C:\Users\Alex\Work\Projects\Current Progects\VisualStudio\WaveFormsArr\Output stm32\putty.log'

    # Creation of new data frame
    data_frame = prs.DataFrame(12)

    # Set path to log file
    data_frame.set_path(path)

    # Get and parse data from log
    sensors = data_frame.get_structured_data()
    data_frame.show_sensors_data()
    data_frame.show_sensors_structured_data()

    # Interface
    app = QApplication()
    main_window = design.MainWindow()
    main_window.show()
    app.exec()



if __name__ == "__main__":
    main()
