import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv() # Load environment variables from .env file

# ------------------- CONSTANTS ------------------- #
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# ------------------- STEP 1: Get Stock Data ------------------- #
# Request daily stock prices for the given stock symbol
stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

# Extract the last two closing prices using list comprehension
closing_price = [float(value['4. close']) for (date, value) in stock_data.items()]

yesterday_closing = closing_price[0]       # Closing price yesterday
day_before_closing = closing_price[1]      # Closing price the day before yesterday

# ------------------- STEP 2: Calculate Price Change ------------------- #
price_diff = yesterday_closing - day_before_closing

up_down = "💹" if price_diff > 0 else "📉" # Add indicator emoji for up or down_trend

percentage_change = round((price_diff * 100)/day_before_closing) # Calculate percentage change

# ------------------- STEP 3: Get News if Change is Significant ------------------- #
# Only fetch news if absolute change is greater than 1%
if abs(percentage_change) > 1:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]

    three_articles = news_data[:3] # Select top 3 articles

    # Format the articles into messages
    formatted_articles = [
            f"{STOCK_NAME}: {up_down}{percentage_change}%\n"
            f"Headlines: {article['title']}.\n"
            f"Brief: {article['description']}"
        for article in three_articles
    ]

    # ------------------- STEP 4: Send SMS via Twilio ------------------- #
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_= "TWILIO_VIRTUAL_NUM",  # Replace with your Twilio number in E.164 format
            to= "YOUR_NUMBER"             # Replace with your verified phone number in E.164 format
        )