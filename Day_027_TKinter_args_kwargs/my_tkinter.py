from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label['text'] = text_input.get()


window = Tk()
window.title('My Cool App')
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

#Label:
my_label = Label(text="I am a label", font=("Arial", 18, "bold"))
#my_label['text'] = 'new text'
my_label.config(text='new text')
my_label.grid(column=0, row=0)


# Button:
button = Button(text='click me', command=button_clicked)
button.grid(column=1, row=1)

button_2 = Button(text='button 2')
button_2.grid(column=2, row=0)

# Entry
text_input = Entry(width=10)
print(text_input.get())
text_input.grid(column=3, row=2)



window.mainloop()