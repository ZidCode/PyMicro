import numpy as np
import pandas as pd
from utils.converters import _convert_to_dict


def parse_sunphotometer_calibration(filename):
    read_data = np.genfromtxt(filename, delimiter=',', skip_header=4, names=True)
    return _convert_to_dict(read_data)


if __name__ == "__main__":
    filename = '../calibration_files/sunphotometer_8409_calibration_backup.csv'
    data = parse_sunphotometer_calibration(filename)
