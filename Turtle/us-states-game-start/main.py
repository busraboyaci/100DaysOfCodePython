import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guesses_states = []
while len(guesses_states) < 50:
    answer_state = screen.textinput(title=f"{len(guesses_states)}/50", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guesses_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guesses_states.append(answer_state)
        # write state name on a boar
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        get_correct_state = data[data.state == answer_state]
        t.goto(int(get_correct_state.x), int(get_correct_state.y))
        t.write(answer_state)



# states to learn.csv

