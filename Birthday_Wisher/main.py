##################### Birthday Wisher Project ######################
import datetime as dt
import random
import smtplib
import pandas


# 1. Get today's date
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day) # Tuple (month, day) for easy matching

data = pandas.read_csv("birthdays.csv") # 2. Read the birthdays.csv file

# 3. Create a dictionary where the key = (month, day) and value = dict of name/email
birthdays_dict = {(value["month"], value["day"]): {"name": value["name"], "email": value["email"]}
    for (index, value) in data.iterrows()
}

if (today_month, today_day) in birthdays_dict: # 4. Check if today matches any birthday
    
    person = birthdays_dict[(today_month, today_day)] # Get details for today’s birthday person
    name = person["name"]
    email = person["email"]

    # 5. Choose a random letter template (letter_1.txt, letter_2.txt, letter_3.txt)
    letter_number = random.randint(1, 3)
    file_path = f"letter_templates/letter_{letter_number}.txt"

    with open(file_path) as letter_file: # 6. Open the letter template and replace [NAME] with actual name
        letter_contents = letter_file.read()
        personalized_letter = letter_contents.replace("[NAME]", name)

    # 7. Your Gmail credentials (App password for security)
    my_email = "your_mail@gmail.com"
    password = "your_app_password"  # <-- App password, not your real Gmail password

    # Connect to Gmail's SMTP server on port 587 (TLS)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday {name}!!\n\n{personalized_letter}"
        )  # Send the email with subject + random quote



