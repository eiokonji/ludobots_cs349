import constants as c
import copy
from solution import SOLUTION

class HILL_CLIMBER:
    def __init__(self) -> None:
        self.parent = SOLUTION()
        
    def Evolve(self):
        self.parent.Evaluate()

        # repeat spaen, mutate evaluate select for several generations
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Select()

    def Spawn(self):
        # spawn a copy of parent -> child
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        pass

    def Select(self):
        pass
