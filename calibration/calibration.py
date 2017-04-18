import logging
from parser import parse_sunphotometer_calibration


class Calibration:

    def __init__(self, calibration_files, bool_process, logger=logging):
        keys = ['sun', 'ozone']
        self.calibration_constants = dict()
        self.calibration_constants = dict.fromkeys(keys)
        if bool_process['sunphotometer']:
            logger.debug('Calibration sunphotometer: %s' % calibration_files['sunphotometer'])
            f_ = calibration_files['sunphotometer']
            data = parse_sunphotometer_calibration(f_)
            self.calibration_constants['sun'] = data
        if bool_process['ozonemeter']:
            logger.debug('Calibration ozonemeter: %s' % calibration_files['ozonemeter'])
            self.calibration_constants['ozone'] = None

    def get_constants(self):
        return self.calibration_constants
