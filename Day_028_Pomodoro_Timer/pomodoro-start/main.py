from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 5
checkmark = ''
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    print(reps)
    if reps in [1, 3, 5, 7]:
        title_label.config(text='Work')
        count_down(work_sec)
    elif reps in [2, 4, 6]:
        title_label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        title_label.config(text='Break', fg=RED)
        count_down(long_break_sec)
        reps = 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global checkmark
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'
    canvas.itemconfig(timer_text, text=f'{count_minute}:{count_seconds}')
    if count > 0:
        window.after(1000, count_down, count -1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark += '✔'
            check_label.config(text=checkmark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, heigh=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45))
title_label.grid(column=1, row=0)

start_button = Button(text='Start', highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightbackground=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

check_label = Label(text=checkmark, bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()