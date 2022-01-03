import random as r
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
tim.speed(0)


def random_color():
    R = r.randint(0, 255)
    G = r.randint(0, 255)
    B = r.randint(0, 255)
    color = (R, G, B)
    return color


direction = [0, 90, 180, 270]

for _ in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(r.choice(direction))


Screen().exitonclick()
