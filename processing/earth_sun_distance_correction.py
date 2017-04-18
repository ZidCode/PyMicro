import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def get_earth_sun_distance_correction(JulianDay):
    """!
    Calculation of the corrected sun earth distance in
    astronomical units (AU)

    @param JulianDay DateTime: python datetime object

    @rtype: float
    @return Return corrected earth sun distance
    """
    e = 0.0167

    if type(JulianDay) == datetime:
        tt = JulianDay.timetuple()
        JulianDay = tt.tm_yday
    sd1 = (1 - e * np.cos(2 * np.pi * (JulianDay - 2.84) / 365)) ** 2
    return sd1


if __name__ == "__main__":
    days_of_year = np.arange(1,365)
    get_earth_sun_distance_correction(date)
