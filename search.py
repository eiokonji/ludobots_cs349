import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# for i in range(5):
#     # executes the generate.py, simulate.py files
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()