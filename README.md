# A7: Kinematic 3D Creature

## What Is The 3D Creature
A creature existing in a 3D morphospace is spawned after the program is run. The creature is made up of conjoint cuboids (aka links) protuding in the x-y-z plane, and these links have randomly generated dimensions. 

![Image of Random 3D Creature Spawn](/3d1.png)

These links are connected by revolute joints and each joint has a motor which can drive its movement. The links may or may not sensors, but all sensors are synaptically connected to all motors. Generated creatures do not have hidden neurons or cross-synaptic connections.

![Brain Genesis: 3d Creature](/3d2.png)

The 3D creature can have links spawned on five of its faces (the bottom face is ignored, see F1-F5 on image below), and aims to have minimal intersection with its own links. For example, the root link can have links on any of its top five faces and successive links can have links on any of their five "free" faces provided there is not self-intersection while they're being spawned.

![Link Addition: 3d Creature](/3d3.png)

Each link must have a minimum length of 0.1m and a maximum length of 0.6m. The links with sensors are green while those without are blue, see earlier images for examples.

## How Was It Made
- Attached links randomly as long as below set ```maxLinks``` variable.
- Avoided self intersection by mapping to dict and crosschecking dict.
- Calculated joint location and spawned new links at those locations.

## How Can You Replicate It
1. Clone the repository.
2. Navigate to your source folder.
3. Run ```python3 simulate.py GUI``` in your terminal.
   - You can alternatively navigate to and run the ```search.py``` file using an IDE.

**Note:** The program will spawn only one 3D creature per run. To observe multiple randomly generated morphologies, repeat steps 1-3 above as many times as you'd like.  

## Get More Information
- [Ludobots MOOC](https://www.reddit.com/r/ludobots/wiki/finalproject/)
- [Pyrosim (forked)](https://github.com/jbongard/pyrosim)
- [Video showing 3D Creature](https://youtu.be/4bhEToQSuz8)
