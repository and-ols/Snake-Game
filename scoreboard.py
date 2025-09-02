from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):
    """
    Creates and handles all logic relating to the scoreboard

    Methods:
    - display_scoreboard
    - update_scoreboard
    - reset
    """

    def __init__(self):
        # Gets the init function from Turtle
        super().__init__()
        # Sets score to 0, and sets the color and hides the turtle, pos, and calls the display
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=275)
        self.display_scoreboard()
    
    def display_scoreboard(self):
        """Creates the scoreboard using the built in write method"""
        self.clear()
        
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        """Updates the scoreboard by clearing it, adding the score and calling the display"""
        self.score += 1
        self.display_scoreboard()

    def reset(self):
        """Updates the high score, and calls the update scoreboard method"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.display_scoreboard()

    # def game_over(self):
    #     """Displays game over text"""
        
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)