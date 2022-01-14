from tkinter import *

def calculate():
    result_label.config(text=round(float(text_input.get()) * 1.6, 2))

window = Tk()
window.title('Mile / KM Converter')
window.minsize(width=300, height=200)
window.config(padx=10, pady=10)


empty_label = Label()
empty_label.grid(column=0, row=0)
empty_label.config(padx=40, pady=0)

text_input = Entry(width=10, text='0')
text_input.insert(END, string="0")
text_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

empty_label2 = Label()
empty_label.grid(column=0, row=3)
empty_label.config(padx=40, pady=0)

button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)

window.mainloop()