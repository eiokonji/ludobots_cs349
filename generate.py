import pyrosim.pyrosim as pyrosim

# sets the initial position and size of a cube in object file. measured in metres.
# size parameters
length = 1
width = 1
height = 1

# position parameters
x = 0               # red
y = 0               # green
z = 0.5             # blue

def Create_World():
    # tells pyrosim name of object file
    pyrosim.Start_SDF("world.sdf")
    #  create a single block at origin
    pyrosim.Send_Cube(name="Box", pos=[x-2,y+2,z], size=[length, width, height])

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Link0", pos=[x,y,z], size=[length, width, height])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[x, y, z + 0.5])
    pyrosim.Send_Cube(name="Link1", pos=[x, y, z], size=[length, width, height])

    pyrosim.End()

Create_World()
Create_Robot()
