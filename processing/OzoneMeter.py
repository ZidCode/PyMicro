import numpy as np
from datetime import datetime
from earth_sun_distance_correction import get_earth_sun_distance_correction
from atmospheric_mass import get_air_mass, get_ozone_path_length
from calibration.calibration import parse_sunphotometer_calibration
from utils.converters import _convert_to_dict, date_time, time_convert 


date_time = lambda x: datetime.strptime(str(x), '%m/%d/%Y')
time_convert = lambda x: datetime.strptime(str(x), '%H:%M:%S')


class OzoneMeter:

    def __init__(self, calibration_frame, logger):
        self.calibration_frame = calibration_frame

    def parse(self, filename):
        pass

    def __converters(self):
        pass

    def calculate_Ozone12(self):
        pass

    def calculate_Ozone23(self):
        pass

    def calculate_Ozone123(self):
        pass


if __name__ == "__main__":
    pass
