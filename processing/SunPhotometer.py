import logging
import numpy as np
from datetime import datetime
from earth_sun_distance_correction import get_earth_sun_distance_correction
from atmospheric_mass import get_air_mass, get_ozone_path_length
from calibration.calibration import parse_sunphotometer_calibration
from utils.converters import _convert_to_dict, date_time, time_convert


class SunPhotometer:

    def __init__(self, calibration_frame, logger=logging):
        self.signal_names = ['SIG380', 'SIG440', 'SIG500', 'SIG675', 'SIG870']
        self.calibration_frame = calibration_frame['sun']
        self.logger = logger
        self.reference_wavelength=550  # nm
        self.data = dict()
        self.__data = None
        self.signal = None

    def parse(self, filename):
        if type(filename) == dict:
            filename = filename['sun']
        data = np.genfromtxt(filename, skip_header=2, names=True, delimiter=',', converters=self.__converters(), dtype=object)
        self.data['sun'] = _convert_to_dict(data)
        self.__data = _convert_to_dict(data)
        self.date = data['DATE'][0]
        self.__create_signal_matrix()
        return self.data

    def get_raw(self):
        return self.data['sun']

    def __converters(self):
        convert_dict = {1:date_time, 2:time_convert}
        for key in np.arange(3, 32):
            convert_dict[key] = float
        return convert_dict

    def __create_signal_matrix(self):
        for key in self.signal_names:
            try:
                self.signal = np.vstack((self.signal, self.__data[key]))
            except ValueError:
                self.signal = self.__data[key]
        self.signal = np.transpose(self.signal)

    def calculate_AOT(self, ozone=0.3509):
        """!
        Calculation of the corrected sun earth distance in
        astronomical units (AU)

        @param name type:

        @rtype: float
        @return Return
        """
        print(self.__data.keys())
        zenith = self.__data['SZA']
        lat = self.__data['LATITUDE']
        h = self.__data['ALTITUDE']
        pcorr = self.__data['PRESSURE']

        sedCorr = get_earth_sun_distance_correction(self.date)
        am = get_air_mass(zenith)
        amo3 = get_ozone_path_length(zenith, lat, h)
        LNsig = np.log(self.signal * sedCorr) +\
                (pcorr.reshape((len(pcorr), 1)) / 1013.25) * self.calibration_frame['rayleigh_ot'] * am.reshape((len(am), 1)) +\
                amo3.reshape((len(amo3), 1)) * (ozone / 0.3316 * self.calibration_frame['ozone_ot']  +
                        self.calibration_frame['no2_ot'])
        self.tau_a = (1 / am.reshape((len(am), 1))) * (self.calibration_frame['lnv0'] - LNsig)
        return self.tau_a

    def calculate_aengstrom_exponent(self):

        lnlambda = np.log(self.calibration_frame['channel'] / self.reference_wavelength)
        lnaot = np.log(self.tau_a)
        import matplotlib.pyplot as plt
        plt.plot(lnlambda, np.transpose(lnaot))
        plt.show()
        print(self.signal)
        self.alphas = np.zeros(len(lnaot))
        for idx, aot_stamp in enumerate(lnaot):
            p = np.polyfit(lnlambda, aot_stamp, deg=1)
            self.alphas[idx] = p[0]
        return self.alphas



if __name__ == "__main__":
    filename = '../calibration_files/sunphotometer_8409_calibration_backup.csv'
    cal_constants = parse_sunphotometer_calibration(filename)
    sun_data = '20161129_Sunphotometer_SN8409_Dach.TXT'
    sun = SunPhotometer(cal_constants)
    sun.parse(sun_data)
