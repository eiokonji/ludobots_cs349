# L. Hill Climber
## Summary
In this section of the course, I explored using the hill climber evolutionary strategy to determine the "best" set of synaptic weights in the robots' neural network that would ensure it accomplished the desired goal.

Hill climbing is a search algorithm which iteratively makes incremental changes to a problem's initial solution in the hopes of finding a better solution. To measure improvement over each iteration, I used a "fitness" variable which described the distance travelled by the robot in the desired direction. This algorithm continued for as many generations as specified in the ```constants.py``` file.

In my implementation, I initially generated a random set of synaptic weights for a robot's neural network and determined (and stored) its fitness. This robot would then spawn a child who would differ from its parent by **one** of its synaptic weights. The child and parent's fitnesses would then be compared and the fitter robot would become the parent of the next generation and the algorithm would repeat itself.

## Deliverables
You can observe the evolutionary improvement in the [video deliverable](https://youtu.be/AWeH8Vg24wA).

## Resources
- [Link to Dr. Bongard's Reddit Course](https://www.reddit.com/r/ludobots/wiki/hillclimber/)
- [Link to Dr. Bongard's GitHub Pyrosim Repository](https://github.com/jbongard/pyrosim.git)
- [More on Hill Climbing Strategy](https://en.wikipedia.org/wiki/Hill_climbing)
- [Guide to Pybullet](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit)
- [Using the OS Library](https://docs.python.org/3/library/os.html)
