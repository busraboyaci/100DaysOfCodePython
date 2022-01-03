import random as r
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)


def random_color():
    R = r.randint(0, 255)
    G = r.randint(0, 255)
    B = r.randint(0, 255)
    random_color = (R, G, B)
    return random_color


def draw_circle(circle_turn_degree):
    for _ in range(int(360/circle_turn_degree)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + circle_turn_degree)


tim.speed(0)
draw_circle(5)


Screen().exitonclick()