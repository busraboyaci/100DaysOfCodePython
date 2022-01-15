import turtle
from turtle import Turtle, Screen
import time
from snake import Snake

turtle.speed('slowest')
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Python Snake Game")
snake = Snake()

# stops the animation
screen.tracer(0)
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    # updating the screen after stops the animation.
    screen.update()
    # slowed down
    time.sleep(0.1)
    # moves snake
    snake.move()










screen.exitonclick()