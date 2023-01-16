import constants as c
from robot import ROBOT
from simulation import SIMULATION
from world import WORLD


import numpy
import random
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time

simulation = SIMULATION()
simulation.Run()

world = WORLD()
robot = ROBOT()







# physicsCLient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.setGravity(0, 0, -9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")

# # set up pyrosim
# pyrosim.Prepare_To_Simulate(robotId)

# # storing motor command values
# targetAnglesBackLeg = numpy.zeros(c.iterations)
# targetAnglesFrontLeg = numpy.zeros(c.iterations)

# # storing sensor values, numpy
# backLegSensorValues = numpy.zeros(c.iterations)
# frontLegSensorValues = numpy.zeros(c.iterations)

# # generate vector of sinusoidally varying values
# firstVector = numpy.linspace(0, numpy.pi * 2, c.iterations)
# # Back Leg
# for ind, each in enumerate(firstVector):
#     targetAnglesBackLeg[ind] = c.ampBackLeg * numpy.sin(c.freqBackLeg * each + c.phaseOffsetBackLeg)
# # Front Leg
# for ind, each in enumerate(firstVector):
#     targetAnglesFrontLeg[ind] = c.ampFrontLeg * numpy.sin(c.freqFrontLeg * each + c.phaseOffsetFrontLeg)

# # opening the window using for loop 1000 times
# p.loadSDF("world.sdf")
# for i in range(c.iterations):
#     p.stepSimulation()

#     # add sensors
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
#         "FrontLeg")

#     # simulating motors
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName=b'Torso_BackLeg',
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=targetAnglesBackLeg[i],
#         maxForce=c.forceBackLeg)
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName=b'Torso_FrontLeg',
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=targetAnglesFrontLeg[i],
#         maxForce=c.forceFrontLeg)

#     time.sleep(1/240)

# # saving sensor data, sine values to a file
# # numpy.save('data/backlegsensor', backLegSensorValues)
# # numpy.save('data/frontlegsensor', frontLegSensorValues)
# numpy.save('data/targetanglesbackleg', targetAnglesBackLeg)
# numpy.save('data/targetanglesfrontleg', targetAnglesFrontLeg)

# # print("back", backLegSensorValues)
# # print("front", frontLegSensorValues)
# p.disconnect()
