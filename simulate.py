import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time

physicsCLient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

# setup for sensors
pyrosim.Prepare_To_Simulate(robotId)

# opening the window using for loop 1000 times
iterations = 3000
p.loadSDF("world.sdf")
for i in range(iterations):
    p.stepSimulation()
    time.sleep(1/60)

# adding sensors
backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

p.disconnect()