import os
from pathlib import Path
from dotenv import load_dotenv
import requests
import smtplib


# -------------------- Load Environment Variables --------------------
# Make sure you have a .env file with:
# OWM_ENDPOINT=https://api.openweathermap.org/data/2.5/forecast
# OWM_API_KEY=your_openweather_api_key
# GMAIL_APP_PASSWORD=your_gmail_app_password
load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)

MY_LAT = -22.572645
MY_LONG = 88.363892

open_weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
openWeather_api_key = os.getenv("OWM_API_KEY")
if not open_weather_endpoint or not openWeather_api_key:
    raise ValueError("OWM_ENDPOINT and OWM_API_KEY must be set in the environment or .env file.")

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
    my_email = os.getenv("GMAIL_ADDRESS")
    password = os.getenv("GMAIL_APP_PASSWORD")
    if my_email is None:
        raise ValueError("GMAIL_ADDRESS must be set in the environment or .env file.")
    if password is None:
        raise ValueError("GMAIL_APP_PASSWORD must be set before sending an email.")
    password = password.replace(" ", "")
    if len(password) != 16:
        raise ValueError(
            "GMAIL_APP_PASSWORD must be a 16-character Google App Password. "
            "Create one in your Google Account and update the .env file."
        )

    # Connect to Gmail's SMTP server on port 587 (TLS)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email, # You can add multiple recipients here
            msg=f"Subject:Weather Forecast\n\nCarry an Umbrella as it is likely to Rain!!"
        )
