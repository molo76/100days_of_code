from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

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
    new_data = {
        website:{
            'email': email_uname,
            'pwd': pwd
        }
    }

    if len(website) == 0 or len(pwd) == 0 or len(email_uname) == 0:
        messagebox.showinfo(title='empty fields detected', message="Please don't leave any fields empty")
    else:
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent=2)
        else:
            data.update(new_data)
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=2)
        finally:
            website_text_entry.delete(0, END)
            pwd_entry.delete(0, END)
            website_text_entry.focus()


def search():
    website = website_text_entry.get()
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            password = data[website]['pwd']
            email = data[website]['email']
            pyperclip.copy(password)
            messagebox.showinfo(title='Password found', message=f'Website = {website}\n'
                                                                f'Email = {email}\nPassword = {password}\n\n'
                                                                'The password has been copied to your clipboard')
    except FileNotFoundError:
        messagebox.showinfo(title='No saved passwords', message="There are no saved passwords\n"
                                                                "Please create and save a password "
                                                                "to use the search function")
    except KeyError:
        if website:
            messagebox.showinfo(title='Password not found', message=f"No entry for {website} found")
        else: 
            messagebox.showinfo(title='Password not found', message="Please enter a website in the "
                                                                    "website box to search")


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

website_text_entry = Entry(width=21)
website_text_entry.grid(row=1, column=1)
website_text_entry.focus()

search_button = Button(text='Search', command=search, width=13)
search_button.grid(row=1, column=2)

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
