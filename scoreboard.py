from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):
    """
    Creates and handles all logic relating to the scoreboard

    Methods:
    - display_scoreboard
    - update_scoreboard
    - game_over
    """

    def __init__(self):
        # Gets the init function from Turtle
        super().__init__()
        # Sets score to 0, and sets the color and hides the turtle, pos, and calls the display
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=275)
        self.display_scoreboard()
    
    def display_scoreboard(self):
        """Creates the scoreboard using the built in write method"""
        
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        """Updates the scoreboard by clearing it, adding the score and calling the display"""

        self.clear()
        self.score += 1
        self.display_scoreboard()

    def game_over(self):
        """Displays game over text"""
        
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)