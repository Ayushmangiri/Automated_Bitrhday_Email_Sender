##################### Automated Birthday Wishing Email Project ######################
import datetime as dt
import pandas as pd
import smtplib
from random import randint

MY_EMAIL = "pythontest164@gmail.com"
PASSWORD = "Ayushman@22"


# TODO 1 Starting files => 1)main.py 2)3 random letter templates 3)birthdays.csv containing name,email,birthday entries


# TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from
#  birthdays.csv Send the letter generated to that person's email address.
def send_email(name, email):
    # Get random email letter from template
    random_letter_number = randint(1, 3)  # generates random number among 1, 2 and 3
    print(random_letter_number)
    random_letter = f"letter_templates/letter_{random_letter_number}.txt"
    with open(random_letter) as file:
        content = file.read()
        content = content.replace("[NAME]", name)
    # We now have name email and content of email We can send email now
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=email,msg=f"Subject: Happy Birthday!!\n\n{content}")
# Lets check
# Bad Network ....
# NOw we shall automate it by using python anywhere free account.
# We shall check by running We shall schedule it daily...
# Thank You all.....


# TODO 2 get current date and time and check if today matches a birthday in the birthdays.csv for every entry
now = dt.datetime.now()
month = now.month
day = now.day

# Read CSV file using pandas
birthdays = pd.read_csv("birthdays.csv")
# Iterate over each entry in birthdays csv file
for index, row in birthdays.iterrows():
    # Check if the day and month from each entry is equal to current day and month
    if day == row['day'] and month == row['month']:
        send_email(name=row['name'], email=row['email'])