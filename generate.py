import pyrosim.pyrosim as pyrosim

# sets the initial position and size of a cube in object file. measured in metres.
# size parameters
length = 1
width = 1
height = 1

# position parameters
x = 0             # red
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

    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])

    pyrosim.End()

Create_World()
Create_Robot()
