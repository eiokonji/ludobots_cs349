import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName) -> None:
        self.linkName = linkName
        self.values = np.zeros(c.iterations)
        
    def Get_Value(self, it):
        # store the sensor value of current link in timestep-indexed list
        self.values[it] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Value(self):
        dst = 'data/' + self.linkName + 'Sensor'
        np.save(dst, self.values)