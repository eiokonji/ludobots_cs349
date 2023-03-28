# M. Parallel Hill Climber
## Summary
In this section of the course, I further explored using the hill climber algorithm in evolution by simultaneously implementing it for multiple parents and determining the fittest of all robots in the last generation. This section relied a lot on understanding the [previous branch](https://github.com/eiokonji/ludobots_cs349/tree/l-hillclimber) which can be accessed if you want to understand my implementation of the hill climbing algorithm.

This codebase parallelized the hill climbing strategy to allow for simultaneous searching for a specified number of parents over a specified number of generations (see ```constants.py``` for these specifications). Note that the hill climbing algorithm is implemented for a parent and child in isolation; each parent is compared **only** to their own child. But, after evolution is done, the fittest robot of all "families" is graphically simulated.

## Deliverables
You can observe evolutionary improvement in the [video deliverable](https://youtu.be/D4jG9y7TaKs).

## Resources
- [Link to Dr. Bongard's Reddit Course](https://www.reddit.com/r/ludobots/wiki/parallelhc/)
- [Link to Dr. Bongard's GitHub Pyrosim Repository](https://github.com/jbongard/pyrosim.git)
- [More on Hill Climbing Strategy](https://en.wikipedia.org/wiki/Hill_climbing)
