# Birthday Wisher

A Python script that automatically sends **personalized birthday wishes** via email.  
It checks today’s date, looks up a list of birthdays from a CSV file, picks a random letter template, replaces the 
    placeholder `[NAME]` with the person’s real name, and sends the email.

---

## Features
    - Reads birthday details (name, email, date) from `birthdays.csv`.
    - Compares today’s date with stored birthdays.
    - Selects a random birthday letter template from `letter_templates/`.
    - Automatically personalizes the message with the recipient’s name.
    - Sends the message using **Gmail’s SMTP server**.

---

## How It Works

    1. Script checks today’s month and day.
    2. If a birthday exists for today in `birthdays.csv`, it selects that person.
    3. Chooses one of three random letter templates (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`).
    4. Replaces `[NAME]` with the birthday person’s actual name.
    5. Sends an email greeting to the recipient.

---

## 📡 SMTP Connections

1. By default, the script uses Gmail’s SMTP server:

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
    
2. Other providers can also be used by changing the SMTP host:

        --> Outlook / Hotmail: smtplib.SMTP("smtp.office365.com", port=587)
        
        --> Yahoo: smtplib.SMTP("smtp.mail.yahoo.com", port=587)
        
        --> Custom Domain: smtplib.SMTP("mail.yourdomain.com", port=587)

---