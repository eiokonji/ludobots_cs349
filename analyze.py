import matplotlib.pyplot as mp
import numpy

# load date, numpy
# backLegSensorValues = numpy.load("./data/backlegsensor.npy")
# frontLegSensorValues = numpy.load("./data/frontlegsensor.npy")
# targetAngles = numpy.load("./data/targetangles.npy")
targetAnglesBackLeg = numpy.load("./data/targetanglesbackleg.npy")
targetAnglesFrontLeg = numpy.load("./data/targetanglesfrontleg.npy")

# visualize data, matplotlib
mp.plot(targetAnglesBackLeg, label="backLeg Target Angles", linewidth=1.6)
mp.plot(targetAnglesFrontLeg, label="frontLeg Target Angles", lw= 0.8)
# mp.plot(targetAngles, label="Target Angles")

mp.legend(loc='best')
mp.show()