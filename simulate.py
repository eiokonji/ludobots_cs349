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
backLegSensorValues = numpy.zeros(3000)

# opening the window using for loop 1000 times
iterations = 3000
p.loadSDF("world.sdf")
for i in range(iterations):
    p.stepSimulation()
    
    # add, print sensors
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    time.sleep(1/60)

# saving sensor data to a file
numpy.save('backlegsensor.npy', backLegSensorValues)

print(backLegSensorValues)
p.disconnect()