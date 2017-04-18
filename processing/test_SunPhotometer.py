import numpy as np
from numpy.testing import assert_array_equal
from SunPhotometer import SunPhotometer
from calibration.calibration import parse_sunphotometer_calibration


def test_SunPhotometer():
    filename = '../calibration_files/sunphotometer_8409_calibration_backup.csv'
    cal_constants = parse_sunphotometer_calibration(filename)
    sun_data = '20161129_Sunphotometer_SN8409_Dach.TXT'
    sun = SunPhotometer(cal_constants)
    parse(sun, sun_data)


def parse(sun, sun_data):
    raw = sun.parse(sun_data)
    assert_array_equal(SIG380, raw['sun']['SIG380'])


SIG380 = np.array([232.78,
 230.80,
 231.80,
 227.21,
 229.47,
 224.05,
 228.09,
 170.86,
 170.75,
 171.42,
 169.94,
 170.85,
 171.87,
 169.02,
 122.49,
 122.99,
 122.56,
 123.30,
 122.09,
 121.29,
  65.61,
  64.83,
  63.16,
  62.69,
  62.29,
  61.61,
  39.53,
  38.96,
  38.10,
  37.65,
  37.16,
  18.30,
  17.74,
  17.51,
  16.87,
  16.04])

