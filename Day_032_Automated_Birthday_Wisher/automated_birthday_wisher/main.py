import smtplib, ssl, email_creds
import datetime as dt
import pandas as pd
from random import choice


def get_letter(recipient):
    letter_to_use = choice(letter_templates)
    with open(f"letter_templates/{letter_to_use}") as f:
        greetings_text = f.read()
        ready_letter = greetings_text.replace('[NAME]', recipient)
        return ready_letter


def send_mail(mail_from, mail_to, mail_content):
    global smtp_server, port
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(mail_from, mail_to, mail_content)
    except Exception as e:
        print(e)
    finally:
        server.quit()


SUBJECT = ['Happy Birthday!', 'Birthday Greetings!', 'Special Day!']
port = 587
smtp_server = email_creds.smtp_server
sender_email = email_creds.sender_email
password = email_creds.password
context = ssl.create_default_context()
today = dt.datetime.now()
month = today.month
day = today.day
letter_templates = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
data = pd.read_csv('birthdays.csv')

for index, row in data.iterrows():
    if row['month'] == month and row['day'] == day:
        letter = get_letter(row['name'])
        message = f'Subject: {choice(SUBJECT)}\n\n{letter}'
        send_mail(sender_email, row['email'], message)
