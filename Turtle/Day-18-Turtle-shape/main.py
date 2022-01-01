from turtle import Turtle, Screen
import random
tim = Turtle()

# for _ in range(4):

# walk 100 unit
# timy_turtle.forward(100)

# turn right 90 degree
# timy_turtle.right(90)
"""
for _ in range(15):
    timy_turtle.forward(10)
    timy_turtle.penup()
    timy_turtle.forward(10)
    timy_turtle.pendown()
"""

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)


def draw_shape(number_of_side):
    angle = 360 / number_of_side
    change_color()
    for _ in range(number_of_side):
        tim.forward(100)
        tim.right(angle)


for number_of_shape in range(3,11):
    draw_shape(number_of_shape)


Screen().exitonclick()
