#!/usr/bin/env python
import numpy as np
from math import cos, radians
from numpy.testing import assert_approx_equal
'''
This module determines the atmospheric path length or Air mass
due to Young (1994)
'''


def get_air_mass(zenith):
    a = 0.50572
    b = 6.07995
    c = -1.6364

    theta_rad = np.radians(zenith)
    AM_inv = np.cos(theta_rad) + a * (b + 90 - zenith) ** c
    return 1 / AM_inv


def get_ozone_path_length(zenith, lat, h):
    """!
    Calculation of the corrected sun earth distance in
    astronomical units (AU)

    @param zenith float: sun zenith angle degrees
    @param lat float: latitude degrees

    @rtype: float
    @return Return air mass for ozone
    """
    R = 6371.
    r = h / 1000
    theta_rad = np.radians(zenith)
    h = 26 - lat * 0.1
    v = (R + r) ** 2 / (R + h) ** 2
    m_o_inv = np.sqrt(1 - v * np.sin(theta_rad) ** 2)
    return 1 / m_o_inv


if __name__ == "__main__":
    zenith = 53.1836240528
    assert_approx_equal( get_air_mass(zenith), 1.66450160404, 5)
