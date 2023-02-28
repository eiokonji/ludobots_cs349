import pybullet as p

class WORLD:

    def __init__(self):
        self.objects = p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")