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
        # List of strings with sensor data
        self.sensors_data = []
        self.size = size
        # List of sensor instances
        self.sensors_structured_data = []

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

            return self.sensors_data

    @staticmethod
    def _get_unique_numbers(numbers):
        unique = []
        size = 0
        for number in numbers:
            if number not in unique:
                unique.append(number)
                size += 1
            else:
                return unique, size

        return unique, size

    def get_structured_data(self):
        '''
        Return list of sensor instances contains
        number of sensor and temperature measurements list
        '''
        all_data = self._parse_log_strings(12)

        # Numbers of different tmp sensors
        sens_numbers = []

        # Sensor instatces list
        sensors = []

        for sensor_data in all_data:
            sensor_data_parts = sensor_data.split(',')

            # Get data from tmp strig
            # TODO: try exept or rewrite regex
            number = int(sensor_data_parts[1])
            temp = float(sensor_data_parts[2])

            # If number of sensor not already exist
            if number not in sens_numbers:
                sens_numbers.append(number)

                # Create sensor instance
                sensor_inst = TmpSensor(number)
                sensors.append(sensor_inst)

            for sensor in sensors:
                if sensor.number == number:
                    sensor.temp_list.append(temp)

            self.sensors_structured_data = sensors

        return self.sensors_structured_data

    def set_path(self, path_to_log : str):
        self.path_to_log = path_to_log

    def get_path(self):
        return self.path_to_log

    def get_sensors_data(self):
        return self.sensors_data

    def show_sensors_data(self):
        '''
            Show disordered data frame
        '''
        print('data frame:\n', self.sensors_data, end='\n\n')

    def show_sensors_structured_data(self):
        '''
            Show ordered data frame
        '''
        for sensor in self.sensors_structured_data:
            print('sensor number = ', sensor.number)
            print(sensor.temp_list, end='\n\n')









        





            

    