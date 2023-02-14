from robot import ROBOT
from simulation import SIMULATION
import sys
from world import WORLD
import os

directOrGUI = sys.argv[1]

simulation = SIMULATION(directOrGUI)
simulation.Run()

world = WORLD()
robot = ROBOT()




