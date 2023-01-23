import constants as c
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim


class MOTOR:
    def __init__(self, jointName) -> None:
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.iterations)

    def Set_Value(self, desiredAngle, robotId):
        # simulating motors
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.forceBackLeg)

