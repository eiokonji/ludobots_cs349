from motor import MOTOR
from sensor import SENSOR

class ROBOT:
    def __init__(self) -> None:
        self.motors = {}
        self.sensors = {}