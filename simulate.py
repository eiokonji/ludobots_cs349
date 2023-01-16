import numpy
import random
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time

physicsCLient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

# set up pyrosim
pyrosim.Prepare_To_Simulate(robotId)

# iterations for for-loop
iterations = 1000
# Back Leg
ampBackLeg = numpy.pi/8
freqBackLeg = 20
phaseOffsetBackLeg = 0
targetAnglesBackLeg = numpy.zeros(iterations)
# Front Leg
ampFrontLeg = numpy.pi/4
freqFrontLeg = 20
phaseOffsetFrontLeg = 0
targetAnglesFrontLeg = numpy.zeros(iterations)

# storing sensor values, numpy
backLegSensorValues = numpy.zeros(iterations)
frontLegSensorValues = numpy.zeros(iterations)

# generate vector of sinusoidally varying values
firstVector = numpy.linspace(0, numpy.pi * 2, iterations)
# Back Leg
for ind, each in enumerate(firstVector):
    targetAnglesBackLeg[ind] = ampBackLeg * numpy.sin(freqBackLeg * each + phaseOffsetBackLeg)
# Front Leg
for ind, each in enumerate(firstVector):
    targetAnglesFrontLeg[ind] = ampFrontLeg * numpy.sin(freqFrontLeg * each + phaseOffsetFrontLeg)

# opening the window using for loop 1000 times
p.loadSDF("world.sdf")
for i in range(iterations):
    p.stepSimulation()

    # add sensors
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")

    # simulating motors
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAnglesBackLeg[i],
        maxForce=100)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAnglesFrontLeg[i],
        maxForce=100)

    time.sleep(1/240)

# saving sensor data, sine values to a file
# numpy.save('data/backlegsensor', backLegSensorValues)
# numpy.save('data/frontlegsensor', frontLegSensorValues)
numpy.save('data/targetanglesbackleg', targetAnglesBackLeg)
numpy.save('data/targetanglesfrontleg', targetAnglesFrontLeg)

# print("back", backLegSensorValues)
# print("front", frontLegSensorValues)
p.disconnect()
