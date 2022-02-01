from turtle import Turtle


class WriteBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_on_board(self):
        self.write()