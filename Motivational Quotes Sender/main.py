import smtplib
import datetime as dt
import random

# Your email credentials
my_email = "your_email"
password = "your_app_password" # <-- App password, not your real Gmail password

now = dt.datetime.now() # Get the current date and time
day = now.strftime("%A") # Get full weekday name e.g. Monday, Tuesday


if True: # sends mail everyday
    with open("quotes.txt") as quotes: # Open the file and read all quotes into a list
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes).strip() # .strip() removes newline (\n) and extra spaces so the email looks clean

    # Connect to Gmail's SMTP server on port 587 (TLS)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls() # Secure the connection
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="target_email",
            msg=f"Subject:{day} Morning Quotes\n\n{quote}"
        ) # Send the email with subject + random quote