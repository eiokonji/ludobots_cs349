# N. The Quadruped
## Summary
In this section of the course, I applied my parallelized implementation of the hill climber algorithm to evolution of a quadruped robot. For more information on my implementation of the hill climbing algorithm and my parallelization, please see the [hill climber branch](https://github.com/eiokonji/ludobots_cs349/tree/l-hillclimber) and the [parallel hill climber branch](https://github.com/eiokonji/ludobots_cs349/tree/m-parallelhillclimber).

The major challenge in this section was building the robot's morphology, that is designing how the robot would look. Using the provided reference to pybullet's coordinate system, I determined the absolute and relative locations of the robot's component links and joints to ensure all parts of the robot were correctly interconnected. Also, I only included sensor neurons in the robot's feet since these were the only sensors that interacted with the world in any discernible, measurable way (based on how I simulated the world i.e. the forces and planes involved).

## Deliverables
You can observe evolutionary improvement in the [video deliverable](https://youtu.be/A-ZIh8Rs_To).

## Resources
- [Link to Dr. Bongard's Reddit Course](https://www.reddit.com/r/ludobots/wiki/quadruped/)
- [Link to Dr. Bongard's GitHub Pyrosim Repository](https://github.com/jbongard/pyrosim.git)
- [More on Pybullet's Coordinate System](https://docs.google.com/presentation/d/1zvZzFyTf8PBNjzQZx_gZk84aUntZo2bUKhpe78yT4OY/edit#slide=id.g10dad2fba23_2_257)
