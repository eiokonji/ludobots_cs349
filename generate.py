import pyrosim.pyrosim as pyrosim

# tells pyrosim name of object file
pyrosim.Start_SDF("boxes.sdf")

# sets the initial position and size of a cube in object file. measured in metres.
# size parameters
length = 1
width = 1
height = 1

# position parameters
x = 0               # red
y = 0               # green
z = 0.5             # blue

# nested while loops making 5 by 5 by 10 blocks (x by y by z)
while x < 5:
    y = 0
    while y < 5:
        length = 1
        width = 1
        height = 1
        z = 0
        while z < 11:
            pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length, width, height])
            z = z + 0.5 + height
            #  reduce size of nect block by 10%
            length = 0.9 * length
            width = 0.9 * width
            height = 0.9 * height
        y = y + 1
    x = x + 1

pyrosim.End()
