import constants as c
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random
import time

# pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])

tester = True

class SOLUTION:
    def __init__(self, nextAvailableID) -> None:
        self.myID = nextAvailableID
        self.links = random.randint(3, 5)
        self.sensorsMatrix = np.random.randint(3, size=self.links+1)

        self.nMotors = self.links
        self.nSensors = np.count_nonzero(self.sensorsMatrix)
        self.weights = np.random.rand(self.nSensors, self.nMotors) * 2 - 1

        self.joints = []
    
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

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        l = random.random() + .25
        w = random.random() + .25
        h = random.random() + .25

        if self.sensorsMatrix[0] == 1:
            pyrosim.Send_Cube(name=f"0", pos=[0,0,h/2] , size=[l,w,h], color="green")
        else:
            pyrosim.Send_Cube(name=f"0", pos=[0,0,h/2] , size=[l,w,h], color="cyan")

        for i in range(self.links):
            # create joint at random point on parent cube
            jointName = f"0_{i+1}"
            self.joints.append(jointName)

            d = random.randint(0, 4)
        
            if d == 0:
                pos = [l/2, random.random()*w - w/2, random.random()*h]
                pyrosim.Send_Joint( name = jointName , parent= str(0) , child = str(i+1) , type = "revolute", position = pos, jointAxis = "0 0 1")

                x = random.random() + .5
                y = random.random() * .5
                z = random.random() * .5

                if self.sensorsMatrix[i+1] == 1:
                    pyrosim.Send_Cube(name=f"{i+1}", pos=[x/2,0,0] , size=[x,y,z], color="green")
                else:
                    pyrosim.Send_Cube(name=f"{i+1}", pos=[x/2,0,0] , size=[x,y,z], color="cyan")
                

            elif d == 1:
                pos = [-l/2, random.random()*w - w/2, random.random()*h]
                pyrosim.Send_Joint( name = jointName , parent= str(0) , child = str(i+1) , type = "revolute", position = pos, jointAxis = "0 0 1")

                x = random.random() + .5
                y = random.random() * .5
                z = random.random() * .5

                if self.sensorsMatrix[i+1] == 1:
                    pyrosim.Send_Cube(name=f"{i+1}", pos=[-x/2,0,0] , size=[x,y,z], color="green")
                else:
                    pyrosim.Send_Cube(name=f"{i+1}", pos=[-x/2,0,0] , size=[x,y,z], color="cyan")


            elif d == 2:
                pos = [random.random()*l - l/2, w/2, random.random()*h]
                pyrosim.Send_Joint( name = jointName , parent= str(0) , child = str(i+1) , type = "revolute", position = pos, jointAxis = "0 0 1")

                x = random.random() * .5
                y = random.random() + .5
                z = random.random() * .5

                if self.sensorsMatrix[i+1] == 1:
                    pyrosim.Send_Cube(name=f"{i+1}", pos=[0,y/2,0] , size=[x,y,z], color="green")
                else:
                    pyrosim.Send_Cube(name=f"{i+1}", pos=[0,y/2,0] , size=[x,y,z], color="cyan")
                

            elif d == 3:
                pos = [random.random()*l - l/2, -w/2, random.random()*h]
                pyrosim.Send_Joint( name = jointName , parent= str(0) , child = str(i+1) , type = "revolute", position = pos, jointAxis = "0 0 1")

                x = random.random() * .5
                y = random.random() + .5
                z = random.random() * .5

                if self.sensorsMatrix[i+1] == 1:
                    pyrosim.Send_Cube(name=f"{i+1}", pos=[0,-y/2,0] , size=[x,y,z], color="green")
                else:
                    pyrosim.Send_Cube(name=f"{i+1}", pos=[0,-y/2,0] , size=[x,y,z], color="cyan")
                

            elif d == 4:
                pos = [random.random()*l - l/2, random.random()*w - w/2, h]
                pyrosim.Send_Joint( name = jointName , parent= str(0) , child = str(i+1) , type = "revolute", position = pos, jointAxis = "1 0 0")
                
                x = random.random() * .5
                y = random.random() * .5
                z = random.random() + .5

                if self.sensorsMatrix[i+1] == 1:
                    pyrosim.Send_Cube(name=f"{i+1}", pos=[0,0,z/2] , size=[x,y,z], color="green")
                else:
                    pyrosim.Send_Cube(name=f"{i+1}", pos=[0,0,z/2] , size=[x,y,z], color="cyan")

        pyrosim.End()
    


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        nameNumber = 0
        
        for i in range(self.links+1):
            if self.sensorsMatrix[i] == 1:
                pyrosim.Send_Sensor_Neuron(name = nameNumber , linkName = str(i))  
                nameNumber += 1

        for i in range(self.links):
            pyrosim.Send_Motor_Neuron(name = nameNumber , jointName = self.joints[i])
            nameNumber += 1

        for s in range(self.nSensors):
            for m in range(self.nMotors):
                pyrosim.Send_Synapse( sourceNeuronName = s , targetNeuronName = m + self.nSensors , weight = self.weights[s][m])
    
        pyrosim.End()