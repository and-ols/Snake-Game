# Snake-Game

## Overview
This version of the Snake game was built using the built in Turtle graphics module, documentation for this can be found below. The game starts with food in the center and the snake moving from the center of the screen, to the left. When the snake eats the food, it grows an additional tail length(which is another turtle). If the snake hits itself or a wall, the game is over. The score is placed at the top right of the screen and a point is added every time the player gets another piece of food.

## Files
- **main**: The role of the main file is to hold all the logic for the game. Main handles the initial screen setup. It also handles the checking if the snake has hit a wall, itself or a piece of food. Also it handles the keys used to control the snake.

- **snake**: The snake class handles the creation of the snake (which is stored as a list of turtles), the addition and extension of the snake (adding a new turtle to the list), and the movement of the snake (which is controlled by the head and then each segment follows the one in front of itself).

- **food**: Food contains the food class, which is a randomly moves each time it is eaten (always starts in the center).

- **scoreboard**: The scoreboard holds the scoreboard class and handles the display of each of the current score and the game over screen.

## Demos
### Snake eating food, hitting itself ending game
![Snake game demo, hitting self ending game](<Snake Game Demo.mkv.gif>)
### Snake hitting wall ending game
![Snake hitting wall ending game](<Snake Game hit wall demo.mkv.gif>)

## Documentation
- [Turtle Graphics](https://docs.python.org/3/library/turtle.html)
