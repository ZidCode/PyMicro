import numpy as np
import copy
from datetime import datetime
from numpy.testing import assert_equal, assert_array_equal, assert_almost_equal
from PyMicro.processing.earth_sun_distance_correction import get_earth_sun_distance_correction


def test_get_earth_sun_distance_correction():
    date = datetime.strptime('2016-09-10', '%Y-%m-%d')
    sdcorr = get_earth_sun_distance_correction(date)
    assert_almost_equal(sdcorr, 1.012, 2)
