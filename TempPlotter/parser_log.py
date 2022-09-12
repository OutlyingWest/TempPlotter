import re


class TmpSensor:
    '''
    Data class contains number and buffer of temperatures
    '''
    def __init__(self, number : int):
        self.number = number
        self.temp_list = []


class DataFrame:
    '''
        Class which capable parse log file and produce any 
        TmpSensor() class instances for storing temperature measurements 
    '''
    def __init__(self, size : int):
        self.path_to_log = ''
        self.sensors_data = []
        self.size = size

    def set_path(self, path_to_log : str):
        self.path_to_log = path_to_log

    def get_path(self):
        return self.path_to_log

    def _parse_log_strings(self, size) -> list:
        '''
        Returns list of strings with number of sensor and it's temperature 
        '''

        regex_sensor_num = r'(tmp,\d+,\d+\.\d+)'

        with open(self.path_to_log, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                expr_finded = re.search(regex_sensor_num, line)
                if expr_finded:
                    strp_line = line.rstrip('\n ,')
                    splt_line = strp_line.split(', ')
                    self.sensors_data.extend(splt_line)
        print(self.sensors_data)
        return self.sensors_data

    def get_sensors_data():
        pass
        





            

    