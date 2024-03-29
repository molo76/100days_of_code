from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^', '[', ']']
passwd = ''


def gen_pwd():
    global passwd
    passwd = ''
    letter_chars = [choice(letters) for _ in range(randint(8, 10))]
    number_chars = [choice(numbers) for _ in range(randint(2, 4))]
    symbol_chars = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = letter_chars + number_chars + symbol_chars
    shuffle(password_list)
    passwd = ''.join(password_list)
    pwd_entry.delete(0, END)
    pwd_entry.insert(0, string=passwd)
    pyperclip.copy(passwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_text_entry.get()
    email_uname = email_uname_entry.get()
    pwd = pwd_entry.get()
    if len(website) == 0 or len(pwd) == 0 or len(email_uname) == 0:
        messagebox.showinfo(title='empty fields detected', message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\n '
                                                      f'Email: {email_uname}\n Password: {pwd}\nIs it ok to save?')
        if is_ok:
            f = open('saved_pwds.txt', 'a')
            f.write(f'{website}|{email_uname}|{pwd}\n')
            website_text_entry.delete(0, END)
            pwd_entry.delete(0, END)
            website_text_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('MyPass Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, heigh=200, highlightthickness=0)
app_logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=app_logo)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0 )

website_text_entry = Entry(width=39)
website_text_entry.grid(row=1, column=1, columnspan=2)
website_text_entry.focus()
email_uname_label = Label(text='Email/Username:')
email_uname_label.grid(row=2, column=0)

email_uname_entry = Entry(width=39)
email_uname_entry.grid(row=2, column=1, columnspan=2)
email_uname_entry.insert(0, 'myname@email.com')

pwd_label = Label(text='Password:')
pwd_label.grid(row=3, column=0)

pwd_entry = Entry(width=21)
pwd_entry.grid(row=3, column=1)

gen_pwd_button = Button(text='Generate Password', command=gen_pwd)
gen_pwd_button.grid(row=3, column=2)

add_button = Button(text='Add', width=37, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
