from tkinter import *


def calculate():
    if radio_state.get() == 1:
        top_label.config(text='Miles')
        bottom_label.config(text='Km')
        result_label.config(text=round(float(text_input.get()) * 1.6, 2))
    elif radio_state.get() == 2:
        top_label.config(text='Km')
        bottom_label.config(text='Miles')
        result_label.config(text=round(float(text_input.get()) / 1.6, 2))
    else:
        pass


window = Tk()
window.title('Mile / KM Converter')
window.minsize(width=300, height=200)
window.config(padx=10, pady=10)

empty_label = Label()
empty_label.grid(column=0, row=2)
empty_label.config(padx=40, pady=0)

text_input = Entry(width=10, text='0')
text_input.insert(END, string="0")
text_input.grid(column=1, row=2)

top_label = Label(text='Miles')
top_label.grid(column=2, row=2)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=3)

result_label = Label(text=0.0)
result_label.grid(column=1, row=3)

bottom_label = Label(text='Km')
bottom_label.grid(column=2, row=3)

empty_label2 = Label()
empty_label.grid(column=0, row=5)
empty_label.config(padx=40, pady=0)

button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=4)

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Km to Miles", value=1, variable=radio_state, command=calculate)
radiobutton2 = Radiobutton(text="Miles to Km", value=2, variable=radio_state, command=calculate)
radiobutton1.grid(column=0, row=0)
radiobutton2.grid(column=0, row=1)

window.mainloop()