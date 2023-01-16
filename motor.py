import constants as c
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName) -> None:
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.iterations)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        # retrieve constants (all motors have same parameters)
        self.amplitude = c.ampBackLeg
        self.frequency = c.freqBackLeg
        self.offset = c.phaseOffsetBackLeg
        self.iterations = c.iterations

        # generate vector of sinusoidally varying values
        firstVector = numpy.linspace(0, numpy.pi * 2, self.iterations)
        # Back Leg
        for ind, each in enumerate(firstVector):
            self.motorValues[ind] = self.amplitude * \
                numpy.sin(self.frequency * each + self.offset)

    def Set_Value(self, it, robotId):
        # simulating motors
        pyrosim.Set_Motor_For_Joint(
            bodyIndex= robotId,
            jointName= self.jointName,
            controlMode= p.POSITION_CONTROL,
            targetPosition= self.motorValues[it],
            maxForce=c.forceBackLeg)

    def Save_Value(self):
        dst = 'data/' + self.jointName + 'Motor'
        numpy.save(dst, self.motorValues)
