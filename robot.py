import constants as c
from motor import MOTOR
import os
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

# os.system delete call in this file! - brain

class ROBOT:
    def __init__(self, solutionID) -> None:
        self.nn = NEURAL_NETWORK("brain"+str(solutionID)+".nndf")
        self.solutionID = solutionID
        # os.system("del brain"+str(solutionID)+".nndf")

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
        # self.nn.Print()

    def Prepare_To_Act(self):
        self.motors = {}

        # store each link and its sensor in self.sensors dict
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, it, robotId):
        # ...?
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(c.motorJointRange * desiredAngle, robotId)

    def Get_Fitness(self, robotId):
        stateOfLinkZero = p.getLinkState(robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        # # write x-coordinate to a new temporary file
        # f = open("fitness" + str(self.solutionID) + ".txt", "w")
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system("rename tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")

        # print("xcoord: ", xCoordinateOfLinkZero)
        exit()
