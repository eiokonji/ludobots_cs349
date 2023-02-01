import numpy

iterations = 1000

# Back Leg constants
ampBackLeg = -numpy.pi/2
forceBackLeg = 50
freqBackLeg = 20
phaseOffsetBackLeg = 0

# Back Leg constants
ampFrontLeg = numpy.pi/2
forceFrontLeg = 50
freqFrontLeg = 20
phaseOffsetFrontLeg = 0

# Hill Climber
numberOfGenerations = 1

# Parallel Hill Climber
populationSize = 1

# Quadruped
numSensorNeurons = 3
numMotorNeurons = 2