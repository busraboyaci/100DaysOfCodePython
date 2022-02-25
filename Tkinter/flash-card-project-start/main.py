from tkinter import *
import random
import pandas as pd
import csv


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



# ---------------------------------- Create New Flash Cards -------------------------------- #
# read data from the french_words.csv in the data folder
def create_new_flash_cards():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_img, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def save_right_answers():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn", index=False)


    create_new_flash_cards()





# ------------------------------------ USER INTERFACE -------------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right = PhotoImage(file="images/right.png")
button_right = Button(image=right, highlightthickness=0, command=save_right_answers)
button_right.grid(row=1, column=1)
wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong, highlightthickness=0, command=create_new_flash_cards)
button_wrong.grid(row=1, column=0)


create_new_flash_cards()


window.after_cancel(3)
window.mainloop()
