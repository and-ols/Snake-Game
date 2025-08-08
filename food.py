from turtle import Turtle
import random


class Food(Turtle):
    """
    Creates and handles all logic relating to the food

    Method:
    - refresh
    """

    def __init__(self):
        # Gets the init function from Turtle
        super().__init__()

        # Sets food shape, make sit not draw, sets size, and color
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        # Creates the food quickly
        self.speed("fastest")

    def refresh(self):
        """
        Gets random x and y and places the food randomly on the screen. 
        Uses the screen width and height without going off the screen, so within 280, -280
        """
        
        # Random cords for the food
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)

        # Sets the food to a random location
        self.goto(random_x, random_y)