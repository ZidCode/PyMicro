from SunPhotometer import SunPhotometer
from OzoneMeter import OzoneMeter
from DeviceHybrid import Hybrid


class DeviceIniFactory:

    def __init__(self, device_dict):
       self.device_dict = device_dict

    def getObject(self):
        objects = []
        if self.device_dict['sunphotometer']:
            object_ = SunPhotometer
        if self.device_dict['ozonemeter']:
            object_ = OzoneMeter
        if self.device_dict['ozonemeter'] & self.device_dict['sunphotometer']:
            object_ = Hybrid
        return object_
