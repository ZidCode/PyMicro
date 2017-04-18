import numpy as np
from datetime import datetime
"""Converters"""


date_time = lambda x: datetime.strptime(str(x), '%m/%d/%Y')
time_convert = lambda x: datetime.strptime(str(x), '%H:%M:%S')


convert_to_array = lambda x, m : np.array([m(s) for s in x.split(',')])
convert_to_dict = lambda independent, type_: {m.split(':')[0]:type_(m.split(':')[1]) for m in independent.split(',')}


def _convert_to_dict(raw):
    data = dict()
    for key in raw.dtype.names:
        if type(raw[key][0]) == float:
            data[key] = raw[key].astype(float)
        else:
            data[key] = raw[key]
    return data


