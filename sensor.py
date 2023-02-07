import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName) -> None:
        self.linkName = linkName
        self.values = np.zeros(c.iterations)
    
    def Get_Value(self, it):
        # store the sensor value of current link in timestep-indexed list
        self.values[it] = np.sin(c.gaitSpeed*it)

    def Save_Value(self):
        dst = 'data/' + self.linkName + 'Sensor'
        np.save(dst, self.values)