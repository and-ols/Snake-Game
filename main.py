from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Sets the screen up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Detects the arrow keys being pressed
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # Refreshes the screen every .1 seconds
    screen.update()
    time.sleep(.1)

    snake.move()

    # Detects collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_scoreboard()

    # Checks to see if the snake head has hit the border of the screen
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    # Detects collision with tail skipping the first element
    for segment in snake.segments[1:]:
        # Checks if the snake head is less then 10 from another segment
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()