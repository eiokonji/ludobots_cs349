from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:
    def __init__(self) -> None:
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}

        # store each link and its sensor in self.sensors dict
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, it):
        # loop through dict and run GetValue method on each sensor
        for s in self.sensors:
            self.sensors[s].Get_Value(it)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Prepare_To_Act(self):
        self.motors = {}

        # store each link and its sensor in self.sensors dict
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, it, robotId):
        # loop through dict and run SetValue method on each motor
        for m in self.motors:
            self.motors[m].Set_Value(it, robotId)