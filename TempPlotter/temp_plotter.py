from weakref import ProxyType
import parser_log as prs


def main():
    path = r'C:\Users\Alex\Work\Projects\Current Progects\VisualStudio\WaveFormsArr\Output stm32\putty.log'

    # Creation of new data frame
    data_frame = prs.DataFrame(12)

    data_frame.set_path(path)
    dt = data_frame._parse_log_strings(12)
    print(dt)

    print(data_frame.get_structured_data())



if __name__ == "__main__":
    main()
