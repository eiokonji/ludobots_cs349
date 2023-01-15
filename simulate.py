import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time

physicsCLient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

# set up pyrosim
pyrosim.Prepare_To_Simulate(robotId)

# storing sensor values, numpy
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

# opening the window using for loop 1000 times
iterations = 1000
p.loadSDF("world.sdf")
for i in range(iterations):
    p.stepSimulation()
    
    # add sensors
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # simulating motors
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = 0.0,
        maxForce = 500)

    time.sleep(1/60)

# saving sensor data to a file
numpy.save('data/backlegsensor', backLegSensorValues)
numpy.save('data/frontlegsensor', frontLegSensorValues)

print("back", backLegSensorValues)
print("front", frontLegSensorValues)
p.disconnect()