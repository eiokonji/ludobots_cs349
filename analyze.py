import matplotlib.pyplot as mp
import numpy

# load date, numpy
backLegSensorValues = numpy.load("./data/backlegsensor.npy")
frontLegSensorValues = numpy.load("./data/frontlegsensor.npy")

# visualize data, matplotlib
mp.plot(backLegSensorValues, label="Back Leg", linewidth=1.2)
mp.plot(frontLegSensorValues, label="Front Leg", lw= 0.8)

mp.legend(loc='upper right')
mp.show()