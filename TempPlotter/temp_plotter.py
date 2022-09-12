import parser_log as prs


def main():
    path = r'putty.log' # C:\Users\Alex\Work\Projects\Current Progects\VisualStudio\WaveFormsArr\Output stm32\putty.log

    # Creation of new data frame
    data_frame = prs.DataFrame(12)

    data_frame.set_path('putty.log')
    data_frame._parse_log_strings(12)



if __name__ == "__main__":
    main()
