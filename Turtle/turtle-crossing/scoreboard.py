from turtle import Turtle

FONT = ("Courier", 24, "normal")
STARTING_POINT = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(-280, 250)
        self.hideturtle()
        self.level = STARTING_POINT
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align="left")

    def level_up(self):
        self.level += STARTING_POINT
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")