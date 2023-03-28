# A5: Legs in Air

## What Does It Do
A four-legged, four-armed robot is spawned. It tries to get unto its head using only its legs, such that its legs are in the air.

## How Did I Do It
I used a parallel hill climber optimization method to "evolve" the robots over generations. I included a simple sinusoidal pattern generator to evolve a different walking gait in the robots. I also adjusted the fitness function to allow evolution that caused the robot to land on its head. The robot has sensors (neurons) only in its four feet/legs, joints between each leg and the torso. Its neural map is made of synapses interconnecting the neurons and joints.

Here is a link to the [video deliverable](https://youtube.com/shorts/yeb4aDyHc9s?feature=share).

## How Can You Replicate It
1. Clone the repository.
2. Modify the ```constants.py``` folder to observe evolution after ```numberOfGenerations``` generations.
3. Run the ```search.py``` file .
   - **Alternatively** type in ```python3 search.py GUI``` into the terminal after navigating to the source folder.

## Get More Information
- [Dr. Bongard's Ludobots MOOC](https://www.reddit.com/r/ludobots/wiki/finalproject/)
- [Link to Dr. Bongard's GitHub Pyrosim Repository](https://github.com/jbongard/pyrosim.git)
- [Understanding Pybullet's Coordinate System](https://docs.google.com/presentation/d/1zvZzFyTf8PBNjzQZx_gZk84aUntZo2bUKhpe78yT4OY/edit#slide=id.p)
