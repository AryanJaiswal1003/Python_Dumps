## ISS Overhead Notifier

This Python script notifies you by email when the International Space Station (ISS) is overhead **at your location** and it's currently dark outside.

---

## Features
    - Fetches real-time ISS position using [Open Notify API](http://api.open-notify.org).
    - Checks sunrise and sunset times using [Sunrise-Sunset API](https://sunrise-sunset.org/api).
    - Sends you an email if:
        1. The ISS is within ±5° of your location.
        2. It is currently dark at your location.

---

## Notes

    * The script checks every 60 seconds.
    * Times from the Sunrise-Sunset API are in UTC, but the script currently uses local time (datetime.now()).For maximum 
            accuracy, consider converting local time to UTC.
    * The email may appear in your Spam folder the first time.