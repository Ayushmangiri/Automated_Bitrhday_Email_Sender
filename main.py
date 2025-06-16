import datetime as dt
import pandas as pd
import smtplib
from random import randint

MY_EMAIL = "pythontest164@gmail.com"
PASSWORD = "dvaf yowd eigg qgph"

def send_email(name, email):
    print(f"Preparing to send test email to {name} at {email}")
    try:
        content = f"Hi {name}, this is a test birthday email."

        with smtplib.SMTP("smtp.gmail.com", port=587, timeout=10) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject: Test Email\n\n{content}"
            )
        print(f"Sent test email to {name}")
    except Exception as e:
        print(f"Failed to send email to {name}: {e}")


# Get today's date
today = dt.datetime.now()
month = today.month
day = today.day

# Read birthday entries
birthdays = pd.read_csv("birthdays.csv")

# Check and send wishes
for _, row in birthdays.iterrows():
    if row['month'] == month and row['day'] == day:
        send_email(name=row['name'], email=row['email'])
