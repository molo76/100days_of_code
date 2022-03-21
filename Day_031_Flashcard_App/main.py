from tkinter import *
from random import choice, shuffle, randint
import math

import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'
to_learn = {}
current_card = {}

try:
    data = pd.read_csv('data/words_to_learn.csv.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def get_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    french_word = current_card['French']
    canvas.itemconfig(language_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=french_word, fill='black')
    canvas.itemconfig(background_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')
    canvas.itemconfig(background_img, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    get_word()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, heigh=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
background_img = canvas.create_image(400, 270, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
language_text = canvas.create_text(400, 150, fill='black', font=(FONT_NAME, 40, 'italic'))
word_text = canvas.create_text(400, 263, fill='black', font=(FONT_NAME, 60, 'bold'))


known_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

unknown_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_img, highlightthickness=0, command=get_word)
unknown_button.grid(row=1, column=0)

get_word()

window.mainloop()

