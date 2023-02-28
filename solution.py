import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import math

class SOLUTION:
    def __init__(self, nextAvailableId):
        self.myID = nextAvailableId

        # links with appendages
        # [totalNum, x, y, z]
        self.noLimbed = 0
        self.limbedData = [
            random.randint(1, 3),
            random.random() * 0.25 + 0.02,
            random.random() * 0.25 + 0.02,
            random.random() * 0.25 + 0.02
        ]

        # appendages
        # [totalNum, x, y, z]
        self.noLimbs = 0
        self.LimbsData = [
            random.randint(1, 4),
            random.random() * 0.25 + 0.02,
            random.random() * 0.25 + 0.02,
            random.random() * 0.25 + 0.02
        ]

        # links without appendages
        # [totalNum, x, y, z]
        self.noLimbless = 0
        self.LimblessData = [
            random.randint(0, 2),
            random.random() * 0.25 + 0.02,
            random.random() * 0.25 + 0.02,
            random.random() * 0.25 + 0.02
        ]

        self.sensorNeurons = []     # links 
        self.motorNeurons = []      # joint names 
        self.synapses = []          # (sensorNumber, motorNumber)
        self.weights = {}           # (sensorNumber, motorNumber): weights 
            
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

    # ----------------------------------------------------------
    #                       create world/sim
    # ----------------------------------------------------------

    def Set_ID(self, nextAvailableId):
        self.myID = nextAvailableId
    
    def Start_Simulation(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain()
        # suppress errors
        os.system(f"start /B python simulate.py {directOrGUI} {self.myID} >nul 2>&1")
        
    def Wait_For_Simulation_To_End(self):
        # check simulation is finished and fitness file ready to be read OTHERWISE sleep search.py
        # DONT CHANGE THE TIME SLEEP PERIOD
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(1/100)

        # read in the fitness value
        while True:
            try:
                f = open(f"fitness{self.myID}.txt", "r")
                break
            except:
                pass
        self.fitness = float(f.read())
        f.close()

    def Create_World(self):
        # tells pyrosim name of object file
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    # ----------------------------------------------------------
    #                            mutation
    # ----------------------------------------------------------

    def Mutate(self):
        # modify the body and the brain
        self.Mutate_Body()
        self.Mutate_Brain()

    def Mutate_Body(self):
        # what body part is changing?
        what = random.random()

        # the limbed links
        if what <= 0.25:
            self.limbedData = self.Mutate_Dims(self.limbedData)

        # the limbless links
        elif what <= 0.5:
            self.LimblessData = self.Mutate_Dims(self.LimblessData)

        # the limbs
        elif what <= 0.75:
            self.LimbsData = self.Mutate_Dims(self.LimbsData)

        else:
            self.tipsData = self.Mutate_Dims(self.tipsData)

    def Mutate_Dims(self, dim):
        # what are you changing: total number of type, length, width, height
        what = random.random()

        # change total number of types
        if what <= 0.25:
            delta = dim[0] + random.choice((1, -1))
            if delta != 0:
                dim[0] = delta
            else:
                dim[0] = 1

        # change length
        elif what <= 0.5: 
            delta = dim[1] + (random.random() * 0.22 - 0.11)
            if delta > 0:
                dim[1] = delta

        # change width 
        elif what <= 0.75:
            delta = dim[2] + (random.random() * 0.22 - 0.11)
            if delta > 0:
                dim[2] = delta

        # change height
        else:
            delta = dim[3] + (random.random() * 0.22 - 0.11)
            if delta > 0:
                dim[3] = delta

        return dim

    def Mutate_Brain(self):
        # turn listofKeys -> listofTuples, choose a random pair and change its weight
        keysTuple = tuple(self.weights.keys())
        self.weights[keysTuple[random.randint(0, len(keysTuple)-1)]] = random.random() * 2 - 1

    # ----------------------------------------------------------
    #                     create body + brain
    # ----------------------------------------------------------

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        # create a sensor neuron in each tip
        for i in range(len(self.sensorNeurons)):
            pyrosim.Send_Sensor_Neuron(f"sensor{i}", f"tip{self.sensorNeurons[i]}")

        # create motor neurons in each joint
        for i in range(len(self.motorNeurons)):
            pyrosim.Send_Motor_Neuron(f"motor{i}", self.motorNeurons[i])

        # connect each sensor neurons to the motor joints along its corresponding limbed and no-limb joints
        for tup in self.synapses:
            pyrosim.Send_Synapse(f"sensor{tup[0]}", f"motor{tup[1]}", self.weights[tup])

        pyrosim.End()

    def Create_Body(self):  
        pyrosim.Start_URDF(f"body{self.myID}.urdf")

        # root link should have largest height
        self.rootHeight = self.tipsData[0]*2*self.tipsData[3]
        largeZ = max(self.limbedData[3], self.LimblessData[3], self.LimbsData[3])
        if largeZ > self.rootHeight:
            self.rootHeight = largeZ

        # reset all initialized terms in each run
        self.noLimbless = 0
        self.noTips = 0
        self.noLimbs = 0
        self.noLimbed = 0
        self.sensorNeurons.clear()
        self.motorNeurons.clear()
        self.synapses.clear()

        # create limbed link, absolute position (root)
        self.Create_Limbed_Link([0, 0, self.rootHeight])
        
        pyrosim.End()

    def Create_Limbed_Link(self, pos):
        # create limbed link && update noLimbed everytime a new limbed link is created
        pyrosim.Send_Cube(name=f"limbed{self.noLimbed}", pos=pos, size=[2*self.limbedData[1], 2*self.limbedData[2], 2*self.limbedData[3]], color="cyan")
        self.noLimbed += 1

        # create limbs on either side of link
        for i in (1, -1): 
            jointPos = [self.limbedData[1], i*self.limbedData[2], 0]

            # different behavior for adding limbs to root link - absolute ref
            if self.noLimbed == 1: 
                jointPos[2] = self.rootHeight 
                jointPos[0] = 0
            
            # create joint Limbed_Limb && need to send motor neuron && create limb
            pyrosim.Send_Joint(name=f"limbed{self.noLimbed-1}_limb{self.noLimbs}", parent=f"limbed{self.noLimbed-1}", child=f"limb{self.noLimbs}", type="revolute" ,position=jointPos, jointAxis="1 0 0")
            self.motorNeurons.append(f"limbed{self.noLimbed-1}_limb{self.noLimbs}")
            self.Create_Limb([0, i*self.LimbsData[2], 0], 0, i)

        # if time: add links in +ve z direction ??

        # check that all links with limbs were created
        if self.noLimbed < self.limbedData[0]:
            # absolute ref for root
            jointPos = [2*self.limbedData[1], 0, 0]
            if self.noLimbed == 1: 
                jointPos[2] = self.rootHeight
                jointPos[0] = self.limbedData[1]

            # alternate limbs and no-limbs segments if it exists; otherwise create limbs segment
            if self.LimblessData[0] > 0: 
                # create joint Limbed_Limbless && need to send motor neuron && create limbless
                pyrosim.Send_Joint(name=f"limbed{self.noLimbed-1}_limbless{self.noLimbless}", parent=f"limbed{self.noLimbed-1}", child=f"limbless{self.noLimbless}", type="revolute", position=jointPos, jointAxis="0 0 1")
                self.motorNeurons.append(f"limbed{self.noLimbed-1}_limbless{self.noLimbless}")
                self.Create_Limbless_Link([self.LimblessData[1], 0, 0], 0)

            else: 
                # create joint Limbed_Limbed && need to send motor neuron && create limbed
                pyrosim.Send_Joint(name=f"limbed{self.noLimbed-1}_limbed{self.noLimbed}", parent=f"limbed{self.noLimbed-1}", child=f"limbed{self.noLimbed}", type="revolute", position=jointPos, jointAxis="0 0 1")
                self.motorNeurons.append(f"limbed{self.noLimbed-1}_limbed{self.noLimbed}")
                self.Create_Limbed_Link([self.limbedData[1], 0, 0])

    def Create_Limbless_Link(self, pos, count):
        # create limbless link, update no of limbless links created
        pyrosim.Send_Cube(name=f"limbless{self.noLimbless}", pos=pos, size=[2*self.LimblessData[1], 2*self.LimblessData[2], 2*self.LimblessData[3]], color="cyan")
        self.noLimbless += 1

        # determine joint location
        jointPos = [2*self.LimblessData[1], 0, 0]

        # have all limbless links been made?
        if count < self.LimblessData[0] - 1:
            # no -> make more (joint Limbless_Limbless - motor neuron - limbless link)
            pyrosim.Send_Joint(name=f"limbless{self.noLimbless - 1}_limbless{self.noLimbless}", parent=f"limbless{self.noLimbless-1}", child=f"limbless{self.noLimbless}", type="revolute", position=jointPos, jointAxis="0 0 1")
            self.motorNeurons.append(f"limbless{self.noLimbless - 1}_limbless{self.noLimbless}")
            # have to update the number or limbless that need to be done
            self.Create_Limbless_Link([self.LimblessData[1], 0, 0], count + 1)

        else: 
            # yes -> make a limbed link (joint Limbless_Limbed - motor neuron - limbed link)
            pyrosim.Send_Joint(name=f"limbless{self.noLimbless - 1}_limbed{self.noLimbed}", parent=f"limbless{self.noLimbless-1}", child=f"limbed{self.noLimbed}", type="revolute", position=jointPos, jointAxis="0 0 1")
            self.motorNeurons.append(f"limbless{self.noLimbless - 1}_limbed{self.noLimbed}")
            self.Create_Limbed_Link([self.limbedData[1], 0, 0])

    def Create_Limb(self, pos, count, mult):
        # create the limb link, update no of limbs created in creature
        pyrosim.Send_Cube(name=f"limb{self.noLimbs}", pos=pos, size=[2*self.LimbsData[1], 2*self.LimbsData[2], 2*self.LimbsData[3]], color="cyan")
        self.noLimbs += 1

        # where should joint be?
        yPos = mult * self.LimbsData[2] 
        
        # have all limbs been created?
        if count < self.LimbsData[0] - 1:
            # no: make more (joint Limbed_Limb - motor neuron - limb)
            pyrosim.Send_Joint(name=f"limb{self.noLimbs-1}_limb{self.noLimbs}", parent=f"limb{self.noLimbs-1}", child=f"limb{self.noLimbs}", type="revolute", position=[0, 2*yPos, 0], jointAxis="1 0 0")
            self.motorNeurons.append(f"limb{self.noLimbs-1}_limb{self.noLimbs}")
            self.Create_Limb([0, yPos, 0], count+1, mult)

        else: 
            # yes: make tips (joint Limb_Tip - motor neuron - tip)
            if self.tipsData[0] > 0:
                pyrosim.Send_Joint(name=f"limb{self.noLimbs-1}_tip{self.noTips}", parent=f"limb{self.noLimbs-1}", child=f"tip{self.noTips}", type="revolute", position=[0, 2*yPos, 0], jointAxis="0 1 0")
                self.motorNeurons.append(f"limb{self.noLimbs-1}_tip{self.noTips}")
                
        color = "cyan"
        if count == self.tipsData[0] - 1:
            color = "green"
            self.sensorNeurons.append(self.noTips)

        pyrosim.Send_Cube(name=f"tip{self.noTips}", pos=pos, size=[2*self.tipsData[1], 2*self.tipsData[2], 2*self.tipsData[3]], color=color)
        self.noTips += 1
        
        if count < self.tipsData[0] - 1:
            pyrosim.Send_Joint(name=f"tip{self.noTips-1}_tip{self.noTips}", parent=f"tip{self.noTips-1}", child=f"tip{self.noTips}", type="revolute", position=[0, 0, -2 * self.tipsData[3]], jointAxis="0 1 1")
            self.motorNeurons.append(f"tip{self.noTips-1}_tip{self.noTips}")
            self.Create_Limb([0, 0, -1], self.tipsData[3], count+1)

        for s in range(self.sensorNeurons):
            for m in range(self.motorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = s , targetNeuronName = m + self.sensorNeurons , weight = self.weights[(s, m)])
