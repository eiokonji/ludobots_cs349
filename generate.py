import pyrosim.pyrosim as pyrosim

# tells pyrosim name of object file
pyrosim.Start_SDF("world.sdf")

# sets the initial position and size of a cube in object file. measured in metres.
# size parameters
length = 1
width = 1
height = 1

# position parameters
x = 0               # red
y = 0               # green
z = 0.5             # blue

#  create a single block at origin
pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length, width, height])

pyrosim.End()
