## Stock News Notifier

This Python project checks Tesla (TSLA) stock prices using the Alpha Vantage API. If the stock price moves more than 1% 
    compared to the previous day, it fetches the latest news headlines from the News API and sends them as SMS alerts using Twilio.

---

## Features

    * Fetches daily stock data from Alpha Vantage.
    * Calculates percentage price change between yesterday and the day before.
    * Fetches top 3 news articles related to the company when stock changes significantly.
    * Sends formatted news summaries via Twilio SMS.

---

## Tech Stack

1. [Alpha Vantage API](https://www.alphavantage.co/) (Stock Prices)

2. [News API](https://newsapi.org/) (Company News)

3. [Twilio API](https://www.twilio.com/) (SMS Messaging)

4. [dotenv](https://pypi.org/project/python-dotenv/) (Environment Variables)

---