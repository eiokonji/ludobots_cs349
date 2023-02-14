# A6: Kinematic Chain aka Snake

## What Is The Snake
A kinematic chain (or snake) is spawned at the start of the program. The snake consists of conjoint cuboids; each cuboid has randomly generated dimensions. 

![Snake 1](/img1.png)

These cuboids are connected by revolute joints and each joint has a motor which can drive its movement. The motion is in the yz plane (see black arrow) and allows movement towards the user (see red arrow). The links may have sensors or not, but all sensors are synaptically connected to the motors.

![Snake 2](/img2.png)

Each link must have a minimum length of 0.1m and a maximum length of 0.6m The links with sensors are green while those without are blue, see earlier images for examples.

## How Was It Made
- Updated files in ```pyrosim``` folder to allow color-coding based on presence (or absence) of sensors.
- Defined matrices to store sensor values for each link and its index.
- Defined motors for each link and defined joints between contiguous links.
- Built neural network of synapses between motors and sensors.

## How Can You Replicate It
1. Clone the repository.
2. Navigate to your source folder.
3. Run ```python3 simulate.py GUI``` in your terminal.
   - You can alternatively navigate to and run the ```search.py``` file using an IDE.

**Note:** The program will spawn only one kinematic chain per run. To observe multiple randomly generated morphologies, repeat steps 1-3 above as many times as you'd like.  

## Get More Information
- [Ludobots MOOC](https://www.reddit.com/r/ludobots/wiki/finalproject/)
- [Video showing Evolution](https://www.youtube.com/watch?v=yeb4aDyHc9s&list=PLrKF7RjvM_gn4lMEKNgkdVZTz8rV0q325&index=15)
- [Pyrosim (forked)](https://github.com/jbongard/pyrosim)
