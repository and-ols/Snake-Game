from turtle import Turtle

#Set starting positions
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
# Set how far the snake moves
MOVE_DISTANCE = 20

# Set directions based off the Turtle documentation
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Handles all of the logic for the Snake

    Methods:
    - create_snake
    - extend
    - add_segment
    - move
    - up
    - down
    - left
    - right
    - reset
    """

    def __init__(self):
        self.segments = []
        self.create_snake()
        # Sets the head to the first element in the list of segments
        self.head = self.segments[0]

    
    def create_snake(self):
        """Creates the snake and places it on the screen."""

        # Loops through each position of the starting positions, then sets shape, color,
        # sends it to the position in the loop, and adds it to the segment list
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        """Adds the new segment to the snake"""

        #Gets the item at the end of the list (-1)
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        """Creates a segment to add to the snake"""

        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    
    def move(self):
        """Moves the snake"""
        # Takes each segment and loops through, gets the position of the last segment and 
        # sets the new position foe that segment.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def reset(self):
        """Resets the snake to the start the snake"""

        # Removes the old segments from the screen
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    
    def up(self):
        """Moves the snake up as long as it is not facing down"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def down(self):
        """Moves the snake down as long as it is not facing up"""
        if self.head.heading() != UP:
         self.head.setheading(DOWN)

    
    def left(self):
        """Moves the snake left as long as it is not facing right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        """Moves the snake right as long as it is not facing left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




