import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
color_list = []

tim = Turtle()
tim.speed(0)
tim.penup()
tim.setpos(-250.0, -310.0)
tim.pen()
tim.hideturtle()
dot_num = 10
gap_num = 50
dot_size = 20


def create_dot(dot_num):
    for _ in range(dot_num):
        color = random.choice(color_list)
        tim.dot(dot_size, color)
        tim.penup()
        tim.forward(gap_num)
        tim.pen()


def change_position():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)

def forward_empty(walking_point):
    tim.forward(walking_point)
    tim.right(180)
    tim.pen()

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

for _ in range(dot_num):
    create_dot(dot_num)
    change_position()
    forward_empty(dot_num*50)







Screen().exitonclick()
