import pyrosim.pyrosim as pyrosim

# tells pyrosim name of object file
pyrosim.Start_SDF("box.sdf")

# sets the initial position and size of a cube in object file. measured in metres.
# size parameters
length = 1
width = 2
height = 3

# position parameters
x = 0               # red
y = 0               # green
z = 0               # blue

pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length, width, height])

pyrosim.End()
