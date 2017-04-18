import logging
from SunPhotometer import SunPhotometer
from OzoneMeter import OzoneMeter


class Hybrid:

    def __init__(self, calibration_frame, logger=logging):
        self.sun = Sunphotometer(calibration_frame['sun'])
        self.ozone = OzoneMeter(calibration_frame['ozone'])
        self.logger = logger
        self.data = dict()

    def parse(self, filename):
        self.data = self.sun.parse(filename)
        self.data = self.data.update(self.ozone.parse(filename))
        return self.data

    def calculate_AOT(self):
        return self.sun.calculate_AOT()

    def calculate_Ozone12(self):
        return self.ozone.calculate_Ozone12()

    def calculate_Ozone23(self):
        return self.ozone.calculate_Ozone23()

    def calculate_Ozone123(self):
        return self.ozone.calculate_Ozone123()

