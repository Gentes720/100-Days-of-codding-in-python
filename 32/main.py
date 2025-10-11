import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText
from mailpass import Password

my_email =  "lontsiangelin01@gmail.com"
password = Password()
my_password = password.mailtoken
now = dt.datetime.now()

if now.weekday() == 4:
    with open('quotes.txt')as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    msg = MIMEText(quote, "plain", "utf-8")
    msg["Subject"] = "Monday Morning again"
    msg["From"] = my_email
    msg["To"] = "stormbrain612@gmail.com"



    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user= my_email, password= my_password)
        connection.sendmail(my_email, "stormbrain612@gmail.com", msg.as_string())
        print("message sent successfuly")
