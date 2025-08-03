import datetime as dt
import pandas as pd
import smtplib
from random import randint

MY_EMAIL = "pythontest164@gmail.com"
PASSWORD = "dvaf yowd eigg qgph"

def send_email(name, email):
    print(f"Preparing to send birthday email to {name} at {email}")
    try:
        random_letter_number = randint(1, 3)
        random_letter = f"letter_templates/letter_{random_letter_number}.txt"
        print(f"Using template: {random_letter}")

        with open(random_letter) as file:
            content = file.read().replace("[NAME]", name.strip())

        with smtplib.SMTP("smtp.gmail.com", port=587, timeout=10) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject: Happy Birthday!!\n\n{content}"
            )

        print(f" Sent birthday email to {name}")

        with open("email_log.txt", "a") as log:
            log.write(f"Sent to {name} ({email}) on {dt.datetime.now().strftime('%Y-%m-%d')}\n")

    except Exception as e:
        print(f"Failed to send email to {name}: {e}")

today = dt.datetime.now()
month = today.month
day = today.day

birthdays = pd.read_csv("birthdays.csv")

for _, row in birthdays.iterrows():
   
    if row['month'] == month and row['day'] == day:
        send_email(name=row['name'], email=row['email'])

