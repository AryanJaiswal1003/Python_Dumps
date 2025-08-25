import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv
import time

load_dotenv() # Load environment variables from .env file

MY_LAT = -22.572645
MY_LONG = 88.363892
ISS_ENDPOINT = os.getenv("ISS_ENDPOINT") # ISS API endpoint

USERNAME = "your_email@gmail.com" # Your email
PASSWORD = os.getenv("GMAIL_APP_PASSWORD") # App password (stored in .env)


def is_iss_overhead():
    """Check if ISS is within +5/-5 degrees of your position."""

    iss_response = requests.get(url=ISS_ENDPOINT)
    iss_response.raise_for_status()
    data = iss_response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Return True if ISS is overhead
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return False


def is_night():
    """Check if it's currently dark at your location."""

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Extract sunrise/sunset in UTC
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour # Current hour (local time — ⚠️ should adjust to UTC for accuracy)

    if time_now >= sunset or time_now <= sunrise:  # It's night if time is after sunset OR before sunrise
        return True
    return False


while True:
    time.sleep(60) # Main loop: check every 60 seconds

    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)

            connection.sendmail(
                from_addr=USERNAME,
                to_addrs=USERNAME,
                msg="Subject:LooK Up!!\n\nThe ISS is above you in the Sky.."
            ) # Send the email