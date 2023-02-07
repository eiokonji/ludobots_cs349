import numpy

iterations = 4000

# Back Leg constants
ampBackLeg = -numpy.pi/2
forceBackLeg = 100
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
populationSize = 10

# Quadruped
numSensorNeurons = 5
numMotorNeurons = 4
motorJointRange = 0.3

# Task O
gaitSpeed = 500000