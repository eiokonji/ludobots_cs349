import constants as c
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random as r
import time

# pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])

tester = True

class SOLUTION:
    def __init__(self, nextAvailableID) -> None:
        # initialize ID, motors, links
        self.myID = nextAvailableID
        self.links = np.random.randint(3, 9)
        self.motors = self.links - 1

        # sensors and weights
        # self.sensormatrix -> random array of 0,1 saying which links get sensors and which dont
        self.sensorsMatrix = np.random.randint(3, size=self.links)
        self.sensors = np.count_nonzero(self.sensorsMatrix)
        self.weights = np.random.rand(self.sensors, self.motors) * 2 - 1

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
        pyrosim.End()

    def Create_Body(self):
        # building robot body
        pyrosim.Start_URDF("body.urdf")

        # ROOT LINK: absolute referencing
        # name, length, width, height, x, y, z
        name = 0
        length = np.random.rand() * 0.5 + 0.1
        width = np.random.rand() * 0.5 + 0.1
        height = np.random.rand() * 0.5 + 0.1

        u_range = 0.6
        x = 0
        y = 0
        z = u_range/2

        # link: check for not-sensor (0) or sensor (1)
        if self.sensorsMatrix[0] == 0:
            pyrosim.Send_Cube(name= f"Link{name}", pos=[x, y, z], size=[length, width, height], color="cyan")
        else:
            pyrosim.Send_Cube(name= f"Link{name}", pos=[x, y, z], size=[length, width, height], color="green")
        # joint: create joint to next link
        pyrosim.Send_Joint(name=f"Link{name}_Link{name+1}", parent=f"Link{name}", child=f"Link{name+1}", type="revolute", position=[0, width/2, z], jointAxis="1 0 0")

        # OTHER LINKS IN CHAIN: relative referencing
        for l in range(1, self.links):
            # send joint but only for L1_L2 and above
            if l > 1:
                pyrosim.Send_Joint(name=f"Link{l-1}_Link{l}", parent=f"Link{l-1}", child=f"Link{l}", type="revolute", position=[0, width*2, 0], jointAxis="1 0 0")

            # generate new random measurements per run
            length = np.random.rand() * 0.5 + 0.1
            width = np.random.rand() * 0.5 + 0.1
            height = np.random.rand() * 0.5 + 0.1

            # create link
            if self.sensorsMatrix[l] == 1:
                pyrosim.Send_Cube(name= f"Link{l}", pos=[0, width, 0], size=[length*2, width*2, height*2], color="green")
            else:
                pyrosim.Send_Cube(name= f"Link{l}", pos=[0, width, 0], size=[length*2, width*2, height*2], color="cyan")

        pyrosim.End()

    
    def Create_Brain(self):
        # send values from sensors, motors to neurons
        pyrosim.Start_NeuralNetwork("brain.nndf")

        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "0")
        # pyrosim.Send_Motor_Neuron(name = 5 , jointName = "Torso_BackLeft")
        
        # motors
        for m in range(self.motors):
            pyrosim.Send_Motor_Neuron(name = m , jointName = f"Link{m}_Link{m+1}")

        # sensors: sensormatrix!
        for s in range(self.links):
            if self.sensorsMatrix[s] == 1:
                pyrosim.Send_Sensor_Neuron(name = s , linkName = f"Link{s}")

        # fully connected neural network
        # synapses
        for s in range(self.sensors):
            for m in range(self.motors):
                pyrosim.Send_Synapse( sourceNeuronName = s , targetNeuronName = m , weight = self.weights[s][m] )

        pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
