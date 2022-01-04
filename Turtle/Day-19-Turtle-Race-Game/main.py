import tkinter
from turtle import Turtle, Screen, textinput
import random
from tkinter import messagebox

screen = Screen()
screen.setup(width=500, height=400)
# pop up shows
is_game_on = False
user_guess = Screen().textinput("chose color", "Which color do you want to be?")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
print(user_guess)
y_position = [-70, -10, -40, 50, 80, 20]
# creating 6 turtle with different colors
all_turtles = []
for index_turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index_turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[index_turtle])
    all_turtles.append(new_turtle)

if user_guess:
    is_game_on = True


def play_game():
    global is_game_on
    while is_game_on:

        for turtle in all_turtles:
            if turtle.xcor() >= 230:
                is_game_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_guess:
                    print(f"you won! The {winning_color} turtle is the winner")
                else:
                    print(f"you lose. The {winning_color} turtle is the winner")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

play_game()
wanna_play = True
while wanna_play:
    if not is_game_on:
        another_game = tkinter.messagebox.askokcancel("Wanna play again?",
                                                      "If you press yes you will play again else it's quit.")
        if another_game:
            is_game_on = True
            for turtle_index in range(len(all_turtles)):
                all_turtles[turtle_index].goto(x=-230, y=y_position[turtle_index])
            user_guess = Screen().textinput("chose color", "Which color do you want to be?")
            play_game()
        else:
            wanna_play = False
            tkinter.messagebox.showinfo("Quit Game", "The game will be quit...")
            screen.bye()
# screen.exitonclick()
