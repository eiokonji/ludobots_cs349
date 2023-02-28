import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
import time
from world import WORLD


class SIMULATION:

    def __init__(self, directOrGUI, solID):
        self.directOrGUI = directOrGUI

        # set up environment
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # load world & robot
        p.setGravity(0,0,c.gravity)
        self.world = WORLD()
        self.robot = ROBOT(solID)

    def Run(self):
        # keep the world open for c.iterations long
        for it in range(c.iterations): 
            p.stepSimulation()
            # allow the robot to sense, pass down current timestep
            self.robot.Sense(it)
            # allow the robot to think, does nothing NOW
            self.robot.Think()
            # allow the robot to move, pass down current timestep
            self.robot.Act(it)
            if self.directOrGUI == "GUI":
                time.sleep(1/2400)

    def Get_Fitness(self, id):
        self.robot.Get_Fitness(id)
        
    def __del__(self):
        # destructor: disconnect from the simulator
        p.disconnect()
        