import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim


class MOTOR:
    def __init__(self, jointName) -> None:
        self.jointName = jointName

    def Set_Value(self, robotId, desiredAngle):
        # simulating motors
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForce)

