# I. Neurons

## Summary
In this section of the course, I implemented a version of closed loop control for locomotion which allows the robots sensors to influence its motions. This used two types of neurons available in pyrosim: sensor and motor neurons.

To do this, I generated a neural network which:
1.  Generated **sensor neurons**, allowed them to receive input from the robot's sensors and updated the sensor neurons' value at each simulation.
2.  Generated **motor neurons**, propagated the sensor neuron values to it and sent these values to the robots' joints using synapses.

## Deliverables
Here is the link to the [video deliverable](https://youtu.be/TKKg9ugYaUs).

## Resources
- [Link to Dr. Bongard's Reddit Course](https://www.reddit.com/r/ludobots/wiki/neurons/)
- [Link to Dr. Bongard's GitHub Pyrosim Repository](https://github.com/jbongard/pyrosim.git)
- [Guide to Pybullet](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit)
