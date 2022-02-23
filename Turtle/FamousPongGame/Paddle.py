from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.new_x = None
        self.new_y = None
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        self.new_y = self.ycor()+20
        self.new_x = self.xcor()
        self.goto(self.new_x, self.new_y)

    def down(self):
        self.new_y = self.ycor()-20
        self.new_x = self.xcor()
        self.goto(self.new_x, self.new_y)


