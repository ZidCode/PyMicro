import numpy as np
from parser import parse_sunphotometer_calibration
from numpy.testing import assert_array_equal


def test_parse_sunphotometer_calibration():

    filename = '../calibration_files/sunphotometer_8409_calibration_backup.csv'
    data = parse_sunphotometer_calibration(filename)
    rayleigh_ozone = np.array([0.449, 0.241, 0.144, 0.042, 0.015])
    assert_array_equal(rayleigh_ozone, data['rayleigh_ot'])
