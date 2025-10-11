##################### Extra Hard Starting Project ######################
import csv
import datetime as dt
import random
import smtplib
from mailpass import Password

password = Password()

# 1. Update the birthdays.csv


with open('/home/gentes/Documents/My 100 days pycodes/32/032/birthdays.csv') as csvfile:
    birthdays = list(csv.DictReader(csvfile))  


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for row in birthdays:
    if int(row['month']) == now.month and int(row['day']) == now.day:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_number = random.randint(1,3)
        with open(f'/home/gentes/Documents/My 100 days pycodes/32/032/letter_templates/letter_{letter_number}.txt', 'r') as letter:
            lines = letter.readlines()
        lines[0] = f"Dear {row['name']}\n"
        final_msg = "".join(lines)

# 4. Send the letter generated in step 3 to that person's email address.


        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user= password.my_email, password= password.mailtoken)
            connection.sendmail(from_addr= password.my_email, to_addrs= row['email'] , msg=f"Subject: HAPPY BIRTHDAY\n\n {final_msg}")

