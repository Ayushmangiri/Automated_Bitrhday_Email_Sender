import smtplib

try:
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=10) as connection:
        connection.starttls()
        connection.login(user="pythontest164@gmail.com", password="dvaf yowd eigg qgph")
        print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)
