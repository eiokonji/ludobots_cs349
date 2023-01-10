import pybullet as p
import pybullet_data
import time

physicsCLient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

# opening the window using for loop 1000 times
iterations = 1000
p.loadSDF("world.sdf")
for i in range(iterations):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()