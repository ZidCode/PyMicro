import numpy as np
import copy
from datetime import datetime
from numpy.testing import assert_equal, assert_array_equal, assert_almost_equal
from PyMicro.processing.earth_sun_distance_correction import get_earth_sun_distance_correction
from PyMicro.processing.calc_aot import calculate_AOT
from atmospheric_mass import get_air_mass, get_ozone_path_length


def test_get_earth_sun_distance_correction():
    date = datetime.strptime('2016-09-10', '%Y-%m-%d')
    sdcorr = get_earth_sun_distance_correction(date)
    assert_almost_equal(sdcorr, 1.012, 2)


def test_get_air_mass():
    zenith = 63.22
    lat = 48.086
    h = 590
    assert_almost_equal(get_air_mass(zenith), 2.21124, 3)
    assert_almost_equal(get_ozone_path_length(zenith, lat, h), 2.191142, 3)

def test_calculate_AOT():
    zenith = 63.22
    lat = 48.086
    h = 590
    signal = 499.910
    date = datetime.strptime('2016-09-10', '%Y-%m-%d')
    pcorr = 940
    theta = 63.41
    ozone = 0.2471

    aot = calculate_AOT(zenith, date, signal, lat, h, pcorr, ozone)
    assert_almost_equal(aot, 0.2784)
