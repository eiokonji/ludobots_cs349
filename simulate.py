import pybullet as p
import time

physicsCLient = p.connect(p.GUI)

# opening the window using for loop 1000 times
iterations = 1000
p.loadSDF("box.sdf")
for i in range(iterations):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()