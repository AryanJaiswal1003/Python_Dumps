import os
from dotenv import load_dotenv
import requests
import smtplib


# -------------------- Load Environment Variables --------------------
# Make sure you have a .env file with:
# OWM_ENDPOINT=https://api.openweathermap.org/data/2.5/forecast
# OWM_API_KEY=your_openweather_api_key
# GMAIL_APP_PASSWORD=your_gmail_app_password
load_dotenv()

MY_LAT = -22.572645
MY_LONG = 188.363892

open_weather_endpoint = os.getenv("OWM_ENDPOINT")
openWeather_api_key = os.getenv("OWM_API_KEY")

# -------------------- API Parameters --------------------
parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "cnt":4, # check next 4 forecast intervals (~12 hours)
    "appid":openWeather_api_key,
}

# -------------------- API Call --------------------
response = requests.get(url=open_weather_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

# -------------------- Check Forecast --------------------
will_rain = False
for forecast in data["list"]:
    weather_id = forecast["weather"][0]["id"]

    if int(weather_id) < 700: # OpenWeather codes < 700 mean rain, snow, thunderstorm, etc.
        will_rain = True

# -------------------- Send Email Alert --------------------
if will_rain:
    # Your email credentials
    my_email = "your_email@gmail.com"
    password = os.getenv("GMAIL_APP_PASSWORD")  # <-- App password, not your real Gmail password

    # Connect to Gmail's SMTP server on port 587 (TLS)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email, # You can add multiple recipients here
            msg=f"Subject:Weather Forecast\n\nCarry an Umbrella as it is likely to Rain!!"
        )
