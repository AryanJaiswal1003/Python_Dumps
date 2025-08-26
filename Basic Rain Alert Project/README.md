# Rain Alert System (Python + OpenWeather + Gmail SMTP)

A simple **Python script** that checks the weather forecast using the [OpenWeatherMap API](https://openweathermap.org/)  
and emails you** alert** if it is likely to rain. ☔

---

## Features
    - Uses **OpenWeatherMap Forecast API**
    - Checks the next 12 hours (4 forecast intervals)
    - Sends an **email alert** if rain is predicted
    - Secure credentials using `.env` file
    - Portable and easy to schedule (via cron/Task Scheduler)

---

## Get API Keys

    OpenWeatherMap: Sign up and get an API key → [here](https://home.openweathermap.org/api_keys)
    
    Gmail App Password: If using Gmail, enable 2FA and generate an App Password.
    Guide: https://support.google.com/accounts/answer/185833

---

## How It Works

    * Fetches forecast for the next 4 intervals (~12 hours).
    * Checks weather[0].id:
    * IDs < 700 mean rain/snow/thunderstorm.
    * If rain is predicted → sends an email alert via Gmail SMTP.