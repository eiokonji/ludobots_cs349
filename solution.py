import constants as c
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random as r
import time

# sets the initial position and size of a cube in object file. measured in metres.
# size parameters
length = 1
width = 1
height = 1

# position parameters
x = 0               # red
y = 0               # green
z = 0.5             # blue

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

    def Wait_For_Simulation_To_End(self):
        # check simulation is finished and fitness file ready to be read OTHERWISE sleep search.py
        # DONT CHANGE THE TIME SLEEP PERIOD
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(1/100)
        
        # read in the fitness value
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        # print(" ")
        # print(self.myID, ": ", self.fitness)
        f.close()

        # delete fitness file once done reading it
        os.system("del fitness"+str(self.myID)+".txt")

    def Create_World(self):
        # tells pyrosim name of object file
        pyrosim.Start_SDF("world.sdf")
        #  create a single block at origin
        pyrosim.Send_Cube(name="Box", pos=[x-2,y+2,z], size=[length, width, height])

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        # creating the robot
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # send values from sensors to neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = c.numMotorNeurons , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron(name = c.numSensorNeurons , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = c.numSensorNeurons , weight = -1.5 )
        pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = c.numSensorNeurons , weight = -1.5 )
        pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.5 )
        pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = -1.5 )

        # fully connected neural network
        for currentRow in range(c.numSensorNeurons):
            for currentColumnn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumnn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumnn] )

        pyrosim.End()

    def Mutate(self):
        randomRow = r.randint(0,2)
        randomColumn = r.randint(0,1)
        self.weights[randomRow][randomColumn] = r.random() * 2 - 1 

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
