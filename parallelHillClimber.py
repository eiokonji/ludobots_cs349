import constants as c
import copy
import os
from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:
    def __init__(self) -> None:
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")

        self.nextAvailableID = 0
        self.parents = {}

        for pop in range(c.populationSize):
            self.parents[pop] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Evolve(self):
        # self.parent.Evaluate("GUI")
        self.Evaluate(self.parents)

        # # repeat spawn, mutate, evaluate, select for several generations
        # for currentGeneration in range(c.numberOfGenerations):
        self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        # spawn, mutate, evaluate, select for one gen
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        # self.Print()
        # self.Select()
        

    def Spawn(self):
        # # spawn a copy of parent -> child
        # self.child = copy.deepcopy(self.parent)
        # self.child.Set_ID(self.nextAvailableID)
        # self.nextAvailableID += 1

        self.children = {}

        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        # mutate each child
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        # parent <- child if parent is less fit
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print("p: ", self.parent.fitness, "| c: ", self.child.fitness)

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass

    def Evaluate(self, solutions):
        # solutions is a SOLUTION object
        # start the simulations in parallel for all parents
        for pop in range(c.populationSize):
            solutions[pop].Start_Simulation("DIRECT")

        # retrieve fitness values for each parent
        for pop in range(c.populationSize):
            solutions[pop].Wait_For_Simulation_To_End()
        
