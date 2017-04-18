import numpy as np
from datetime import datetime
from earth_sun_distance_correction import get_earth_sun_distance_correction
from atmospheric_mass import get_air_mass, get_ozone_path_length


tau_r = 0.449
tau_ozone = 0.000
tau_nitro = 0.00315
LNVO = 7.756


def calculate_AOT(zenith, date, signal, lat, h, pcorr, ozone=0.3316):
    """!
    Calculation of the corrected sun earth distance in
    astronomical units (AU)

    @param name type:

    @rtype: float
    @return Return
    """
    sedCorr = get_earth_sun_distance_correction(date)
    am = get_air_mass(zenith)
    amo3 = get_ozone_path_length(zenith, lat, h)
    LNsig = np.log(signal * sedCorr) + (pcorr / 1013.25) * tau_r * am + amo3 * (ozone / 0.3316 * tau_ozone  + tau_nitro)
    tau_a = (1 / am) * (LNVO - LNsig)
    return tau_a


if __name__ == "__main__":
    zenith = 63.22
    lat = 48.086
    h = 590
    signal = 499.910
    date = datetime.strptime('2016-09-10', '%Y-%m-%d')
    pcorr = 940
    ozone = 0.2471

    aot = calculate_AOT(zenith, date, signal, lat, h, pcorr, ozone)
    print(aot)
