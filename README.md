# A7: Kinematic 3D Creature

## What Is The 3D Creature
A creature existing in a 3D morphospace is spawned after the program is run. The creature is made up of conjoint cuboids (aka links) protuding in the x-y-z plane, and these links have randomly generated dimensions. 

!/[Image of Random 3D Creature Spawn](/img1.png)

These links are connected by revolute joints and each joint has a motor which can drive its movement. The motion is in the yz plane (see black arrow) and allows movement towards the user (see red arrow). The links may have sensors or not, but all sensors are synaptically connected to all motors. Generated creatures do not have hidden neurons or cross-synaptic connections.

!/[Annotated Image of 3d Creature showing Range & Direction of Motion](/img1.png)

The 3D creature can have links spawned on --- of its faces, and aims to have minimal intersection with its own links. For example, the root link can have links on any of its six faces and successive links can have links on any of their five "free" faces provided there is not self-intersection while they're being spawned.

!/[3D Creature Genesis - Diagram](/img1.png)

Each link must have a minimum length of 0.1m and a maximum length of 0.6m. The links with sensors are green while those without are blue, see earlier images for examples.

## How Was It Made
### **TBD**
- how to avoid self-intersection
- how to ensure 3D placement
- ...

## How Can You Replicate It
1. Clone the repository.
2. Navigate to your source folder.
3. Run ```python3 simulate.py GUI``` in your terminal.
   - You can alternatively navigate to and run the ```search.py``` file using an IDE.

**Note:** The program will spawn only one 3D creature per run. To observe multiple randomly generated morphologies, repeat steps 1-3 above as many times as you'd like.  

## Get More Information
- [Ludobots MOOC](https://www.reddit.com/r/ludobots/wiki/finalproject/)
- [Video showing 3D Creature - tbd]
- [Pyrosim (forked)](https://github.com/jbongard/pyrosim)
