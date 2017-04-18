#!/usr/bin/env python
import logging
import ConfigParser
import numpy as np
from datetime import datetime
from ast import literal_eval
from calibration.calibration import Calibration
from utils.converters import convert_to_dict
from processing.DeviceIniFactory import DeviceIniFactory

"""
Microtops Evaluation Package
"""

def parse_ini_config(ini_file):
    config = ConfigParser.ConfigParser()
    config.read(ini_file)
    config_dict = {s: dict(config.items(s)) for s in config.sections()}
    config_dict['Data']['files'] = convert_to_dict(config_dict['Data']['files'], str)
    config_dict['Logging']['logging'] = literal_eval(config_dict['Logging']['logging'])
    config_dict['Output']['show'] = literal_eval(config_dict['Output']['show'])
    config_dict['Processing']['sunphotometer'] = literal_eval(config_dict['Processing']['sunphotometer'])
    config_dict['Processing']['ozonemeter'] = literal_eval(config_dict['Processing']['ozonemeter'])
    config_dict['Processing']['reference_wavelength'] = float(config_dict['Processing']['reference_wavelength'])
    return config_dict


def create_logger(log_config):
    logger = logging.getLogger('microtops_eval')
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s - %(funcName)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.setLevel(log_config['logging_level'])
    return logger


def microtops_evaluation(config, logger):
    # Calibration_data
    cal = Calibration(config['Calibration'], config['Processing'], logger)
    calibration_constants = cal.get_constants()
    print(calibration_constants['sun']) 
    factory = DeviceIniFactory(config['Processing'])
    object_device = factory.getObject() 
    device = object_device(calibration_constants, logger)
    device.parse(config['Data']['files'])
    # # Presentation
    frame = device.get_raw()
    aots = device.calculate_AOT()
    print(aots)
    alphas = device.calculate_aengstrom_exponent()
    print(frame['TIME'])
    print(alphas)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='config.ini', help='')
    parser.add_argument('-f', '--filename', help='')
    args = parser.parse_args()
    config = parse_ini_config(args.config)
    logger = create_logger(config['Logging'])
    microtops_evaluation(config, logger)
