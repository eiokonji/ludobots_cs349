import constants as c
import copy
import os
from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:
    def __init__(self) -> None:
        self.parents = {}

        for pop in range(c.populationSize):
            self.parents[pop] = SOLUTION()
        
        
    def Evolve(self):
        # self.parent.Evaluate("GUI")

        # # repeat spawn, mutate, evaluate, select for several generations
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()

        for pop in range(c.populationSize):
            self.parents[pop].Evaluate("GUI")

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
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

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass
