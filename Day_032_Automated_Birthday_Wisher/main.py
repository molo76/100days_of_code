import smtplib, ssl, email_creds
import datetime as dt
from random import choice

 
def pick_quote():
    with open('monday_quotes.txt') as f:
        quotes = f.read()
        quote_list = quotes.split('\n')
    return choice(quote_list)


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


port = 587
smtp_server = email_creds.smtp_server
sender_email = email_creds.sender_email
password = email_creds.password
receiver_email = email_creds.receiver_email
context = ssl.create_default_context()
today = dt.datetime.now()

if today.strftime("%A") == 'Monday':
    quote = pick_quote()
    SUBJECT = 'Todays words of wisdom'
    MESSAGE = quote
    message = f'Subject: {SUBJECT}\n\n{MESSAGE}'
    print(quote)
    send_mail(sender_email, receiver_email, message)





