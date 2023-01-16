import matplotlib.pyplot as mp
import numpy

# load date, numpy
backLegSensorValues = numpy.load("./data/backlegsensor.npy")
frontLegSensorValues = numpy.load("./data/frontlegsensor.npy")
targetAngles = numpy.load("./data/targetangles.npy")

# visualize data, matplotlib
# mp.plot(backLegSensorValues, label="Back Leg", linewidth=1.2)
# mp.plot(frontLegSensorValues, label="Front Leg", lw= 0.8)
mp.plot(numpy.sin(targetAngles), label="Target Angles")

mp.legend(loc='best')
mp.show()