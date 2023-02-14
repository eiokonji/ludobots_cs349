import constants as c
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random as r
import time

# sets the initial position and size of a cube in object file. measured in metres.
# size parameters
length = np.random.rand()
width = np.random.rand()
height = np.random.rand()

# position parameters
x = 0               # red
y = 0               # green
z = 0.5             # blue

# pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])

# os.system delete call in this file! - fitness

tester = True

class SOLUTION:
    def __init__(self, nextAvailableID) -> None:
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        # starts the simulation
        if tester == False or self.myID == 0:
            self.Create_Body()        
            self.Create_World()
        self.Create_Brain()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))

    def Create_World(self):
        # tells pyrosim name of object file
        pyrosim.Start_SDF("world.sdf")
        #  create a single block at origin
        # pyrosim.Send_Cube(name="Box", pos=[x-2,y+2,z], size=[length, width, height])

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        
        pyrosim.Send_Cube(name= 0, pos=[0, 0, 1], size=[length, width, height])

        ''' 
        pyrosim.Send_Joint(name=, parent="Torso", child="FrontRight", type="revolute", position=[0.5, 0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="FrontRight", pos=[0, 0, -1], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_FrontRight", parent="Torso", child="FrontRight", type="revolute", position=[0.5, 0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="FrontRight", pos=[0, 0, -1], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_FrontLeft", parent="Torso", child="FrontLeft", type="revolute", position=[-0.5, 0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="FrontLeft", pos=[0, 0, -1], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_BackRight", parent="Torso", child="BackRight", type="revolute", position=[0.5, -0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackRight", pos=[0, 0, -1], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_BackLeft", parent="Torso", child="BackLeft", type="revolute", position=[-0.5, -0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLeft", pos=[0, 0, -1], size=[0.2, 0.2, 1])
        '''

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        # send values from sensors to neurons
        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeft")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeft")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "FrontLeft")
        # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "BackRight")

        # pyrosim.Send_Motor_Neuron(name = 5 , jointName = "Torso_BackLeft")
        # pyrosim.Send_Motor_Neuron(name = 6 , jointName = "Torso_FrontRight")
        # pyrosim.Send_Motor_Neuron(name = 7, jointName = "Torso_FrontLeft")
        # pyrosim.Send_Motor_Neuron(name = 8, jointName = "Torso_BackRight")

        # # fully connected neural network
        # for currentRow in range(c.numSensorNeurons):
        #     for currentColumnn in range(c.numMotorNeurons):
        #         pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumnn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumnn] )

        pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
