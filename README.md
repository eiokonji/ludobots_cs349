# A8: Evolving for Locomotion

## What Is The Creature
This is a 3D creature as it expands in four possitble directions: -x, +y, -y, -z. It aims to maximize horizontal displacement away from the viewer (into the screen). It was evolved using the parallel hill climbing evolutionary strategy. The creature is color-coded: "green" links are innervated and in the neural network while "cyan" links are not. 

![Sample Creature](/a80.png)

### How Is It Connected
#### Neural Mapping
All joints are linked to the sensors in the same region as seen in the figure below. This means a sensor on one side of the creature can only affect the motors of the links near it. Although different joints can move in the x-z and x-y planes, it generally moves in the positive x-direction (into the screen). Visualizing this behavior may be difficult and I encourage you to watch the attached video for context.

![How are the links and sensors connected?](/a81.png)

#### Building the Creature
The creature is made of cuboidal blocks aka links. These links were connected to create multi-legged creatures. Its design is inspired by centipedes' morphology. A link could either function as a lateral link or as an appendage. Some lateral links had appendages while others did not. All sensors were located at the tip of the appendage since that was the part of the creature most often (and most likely to be) in contact with the plane.

![Karl Sims inspired diagram](/a82.jpg)

### How Was It Evolved
As mentioned earlier, this creature was evolved with the parallel hill climber evolutionary strategy. This means parents and children were compared and the fitter of them would carry on the "family legacy" - this is one generation. This cycle would repeat for as ,any generationa as specified. Multiple members of the population were simultaneously being compared and evolved. In the end, the user is presented with the fittest creature across all "families" and after a specified number of generations have passed.

Pop 1                                                            |  Pop 2
:---------------------------------------------------------------:|:-------------------------:
![image showing parallel hill climbing strategy, pt1](/a83.png)  |  ![image showing parallel hill climbing strategy, pt2](/a8_4.png)

#### Mutations
- **Brain**: Randomly selecting a neuron pair and modifying the weight assigned to their synaptic connections.
- **Body**: Randomly selecting a body part and modifying its dimensions (i.e. length, width, height)

For this codebase, there were 25 families (**population size**) and evolution occured across 80 generations (**number of generations**). Also, this codebase used a technique called seeding. This allows the user to observe a specific randomly generated families' generational evolution multiple times by passing in a seed number. Below, you can see how five different seeds evolved over 100 generations.

![a plot containing five fitness curves, each starting from a different random seed (1,2,3,4,5), showing the fitness of the best creature in the population at each generation](/plot/fCurve.png)


## How Can You Replicate It
1. Clone the repository.
2. Navigate to your source folder.

#### Viewing the Unevolved and Evolved Creatures
3. Run ```python3 search.py {population_size} {number_generations} {seed}``` in your terminal.
   - ```{population_size}```: size of the population, recommended size - **25**
   - ```{number_generations}```: number of generations, recommended size - **100**
   - ```{seed}```: seed, can be any positive, non-zero value

#### Generating the Plot
4. Run the ```analyze.py``` file (click run)

**Note:** After conducting one run, you will have data to make one plot showing evolution of one seed creature design. Plot can include information on what happens after conducting one run, how to generate plot

## Get More Information
- [Ludobots MOOC](https://www.reddit.com/r/ludobots/wiki/finalproject/)
- [Video Showing Evolution](https://youtu.be/XgiD9_P2mMk)
- [Pyrosim (forked)](https://github.com/jbongard/pyrosim)
