import constants as c
import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName) -> None:
        self.linkName = linkName
        self.values = numpy.zeros(c.iterations)
    
    def Get_Value(self, it):
        self.values[it] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # if it == 999:
        #     print(self.values)