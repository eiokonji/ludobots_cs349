import os
from hillclimber import HILL_CLIMBER

# for i in range(5):
#     # executes the generate.py, simulate.py files
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

hc = HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()