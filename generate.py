import pyrosim.pyrosim as pyrosim

# tells pyrosim name of object file
pyrosim.Start_SDF("box.sdf")

# sets the initial position and size of a cube in object file. measured in metres.
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5], size=[1,1,1])


