import os
import serial
import logging


def read_microtops(logger, outputfile):
    # get maybe port automatically... or passing
    ser = serial.Serial(port, timeout=2)
    logger.debug("Initialization %s" % ser)
    ser.write("\r\n")
    logger.info(ser.readlines())
    ser.write("P")
    data = ser.readlines()
    ser.close()
    logger.debug(data)
    with open(outputfile, 'w') as fp:
        fp.write(data)    


def create_logger(log_level):
    logger = logging.getLogger('eval')
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s - %(funcName)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.setLevel(log_level)
    return logger



if __name__ == "__main__":
    import argparse
    verbose = {True: DEBUG, False: INFO}
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', default=False, action=store_true,  help='Pass ini-file for processing configurations')
    parser.add_argument('-o', '--output_file')
    args = parser.parse_args()
    logger = create_logger(verbos[args.verbose])
    read_microtops(logger) 
