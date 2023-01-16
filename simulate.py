import constants as c
from robot import ROBOT
from simulation import SIMULATION
from world import WORLD



simulation = SIMULATION()
simulation.Run()

world = WORLD()
robot = ROBOT()








# # saving sensor data, sine values to a file
# # numpy.save('data/backlegsensor', backLegSensorValues)
# # numpy.save('data/frontlegsensor', frontLegSensorValues)
# numpy.save('data/targetanglesbackleg', targetAnglesBackLeg)
# numpy.save('data/targetanglesfrontleg', targetAnglesFrontLeg)

# # print("back", backLegSensorValues)
# # print("front", frontLegSensorValues)
# p.disconnect()
