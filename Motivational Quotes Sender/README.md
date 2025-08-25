## Daily Quote Email Sender

This Python script automatically sends a random inspirational quote from a quotes.txt file every day via email using Gmail’s SMTP server.

---

## Features

    1. Picks a random quote from a text file (quotes.txt).
    2. Sends an email with a subject like “Monday Morning Quote”.
    3. Works with Gmail SMTP (can also work with Outlook, Yahoo, etc.).

---

## SMTP Connection Examples

1. The script currently uses Gmail SMTP:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)


2. But you can also use other providers:

A. Outlook / Hotmail:

    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)


B. Yahoo

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)


C. Custom SMTP Server

    with smtplib.SMTP("mail.yourdomain.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

---