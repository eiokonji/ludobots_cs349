from robot import ROBOT
from simulation import SIMULATION
import sys
from world import WORLD

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()

world = WORLD()
robot = ROBOT(solutionID)

simulation.Get_Fitness()



