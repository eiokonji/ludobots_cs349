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
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[x, y, z + 0.5])

    pyrosim.Send_Cube(name="Link2", pos=[x, y, z], size=[length, width, height])
    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[x, y + 0.5, z])

    pyrosim.Send_Cube(name="Link3", pos=[x, y + 0.5, z-0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[x, y + 1, 0])

    pyrosim.Send_Cube(name="Link4", pos=[x, y + 0.5, z-0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[x, y + 0.5, z-1])

    pyrosim.Send_Cube(name="Link5", pos=[x, y, z - 1], size=[length, width, height])
    pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[x, y, z - 2])

    pyrosim.Send_Cube(name="Link6", pos=[x, y, z - 0.5], size=[length, width, height])


    pyrosim.End()

Create_World()
Create_Robot()
