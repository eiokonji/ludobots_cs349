# A6: Kinematic Chain aka Snake

## Describing the Chain
A kinematic chain (or snake) is spawned at the start of the program. The snake consists of conjoint cuboids; each cuboid has randomly generated dimensions. 

*![Snake 1](<img width="176" alt="image" src="https://user-images.githubusercontent.com/116220220/218651790-f82da150-3aac-49f2-b09f-3882c08b90e7.png">)*

These cuboids are connected by --- joints and each joint has a motor which can drive its movement. The motion is largely in the --- plane. The links may have sensors or not, but all sensors are synaptically connected to the motors.

*[insert image(s) of showing joint motor direction]*

Each link must have a minimum length of --- and a maximum length of ---. The links with sensors are color green ([insert color code]) while those without are blue ([insert color code]).

*[insert image(s) of snake measurement and colors + legend]*

## How Was It Made
---


## How Can You Replicate It
1. Clone the repository.
2. Navigate to your source folder.
3. Run ```python3 simulate.py GUI 0``` in your terminal.

**Note:** The program will spawn only one kinematic chain per run. To observe multiple randomly generated morphologies, repeat steps 1-3 above.

## Get More Information
- [Ludobots MOOC](https://www.reddit.com/r/ludobots/wiki/finalproject/)
- [Video showing Evolution](https://www.youtube.com/watch?v=yeb4aDyHc9s&list=PLrKF7RjvM_gn4lMEKNgkdVZTz8rV0q325&index=15)
- [Pyrosim (forked)](https://github.com/jbongard/pyrosim)
