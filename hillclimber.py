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
        self.Print()
        self.Select()

    def Spawn(self):
        # spawn a copy of parent -> child
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        # parent <- child if parent is less fit
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print("p: ", self.parent.fitness, "| c: ", self.child.fitness)
