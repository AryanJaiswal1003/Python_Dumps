import math
import os
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
REQUEST_TIMEOUT = 30


def required_setting(name: str) -> str:
    value = os.getenv(name)
    if not value or not value.strip():
        raise ValueError(f"{name} must be configured in the environment or repository .env file.")
    return value.strip()


def get_stock_closes() -> tuple[float, float]:
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": required_setting("ALPHA_VANTAGE_API_KEY"),
    }
    response = requests.get(STOCK_ENDPOINT, params=parameters, timeout=REQUEST_TIMEOUT)
    if not response.ok:
        raise RuntimeError(f"Alpha Vantage returned HTTP {response.status_code}.")

    try:
        payload: Any = response.json()
    except requests.exceptions.JSONDecodeError as error:
        raise RuntimeError("Alpha Vantage returned an invalid JSON response.") from error

    if not isinstance(payload, dict):
        raise RuntimeError("Alpha Vantage returned an unexpected response format.")

    time_series = payload.get("Time Series (Daily)")
    if not isinstance(time_series, dict):
        api_message = next(
            (
                payload[key]
                for key in ("Error Message", "Information", "Note")
                if isinstance(payload.get(key), str)
            ),
            "The response did not contain daily stock data.",
        )
        raise RuntimeError(f"Alpha Vantage did not return daily stock data: {api_message}")

    try:
        recent_dates = sorted(time_series, reverse=True)[:2]
        if len(recent_dates) < 2:
            raise ValueError("fewer than two daily prices were returned")
        closes = [float(time_series[date]["4. close"]) for date in recent_dates]
    except (KeyError, TypeError, ValueError) as error:
        raise RuntimeError("Alpha Vantage returned malformed daily closing prices.") from error

    if not all(math.isfinite(close) for close in closes):
        raise RuntimeError("Alpha Vantage returned a non-finite closing price.")
    if closes[1] == 0:
        raise RuntimeError("The previous closing price is zero; percentage change cannot be calculated.")

    return closes[0], closes[1]


def get_news_articles() -> list[dict[str, Any]]:
    parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": required_setting("NEWS_API_KEY"),
    }
    response = requests.get(NEWS_ENDPOINT, params=parameters, timeout=REQUEST_TIMEOUT)
    if not response.ok:
        raise RuntimeError(f"News API returned HTTP {response.status_code}.")

    try:
        payload: Any = response.json()
    except requests.exceptions.JSONDecodeError as error:
        raise RuntimeError("News API returned an invalid JSON response.") from error

    articles = payload.get("articles") if isinstance(payload, dict) else None
    if not isinstance(articles, list):
        message = payload.get("message") if isinstance(payload, dict) else None
        detail = message if isinstance(message, str) else "The response did not contain an articles list."
        raise RuntimeError(f"News API did not return articles: {detail}")

    return [article for article in articles if isinstance(article, dict)][:3]


def send_alerts(messages: list[str]) -> None:
    account_sid = required_setting("TWILIO_SID")
    auth_token = required_setting("TWILIO_AUTH_TOKEN")
    from_number = required_setting("TWILIO_FROM_NUMBER")
    to_number = required_setting("TWILIO_TO_NUMBER")

    for name, number in (("TWILIO_FROM_NUMBER", from_number), ("TWILIO_TO_NUMBER", to_number)):
        if not number.startswith("+") or not number[1:].isdigit():
            raise ValueError(f"{name} must be a phone number in E.164 format, such as +15551234567.")

    client = Client(account_sid, auth_token)
    try:
        for message in messages:
            client.messages.create(body=message, from_=from_number, to=to_number)
    except TwilioRestException as error:
        raise RuntimeError(f"Twilio could not send the alert (HTTP {error.status}). Check your account and numbers.") from error


def main() -> None:
    latest_close, previous_close = get_stock_closes()
    price_change = latest_close - previous_close
    percentage_change = price_change / previous_close * 100

    if abs(percentage_change) <= 1:
        print(f"{STOCK_NAME} changed {percentage_change:.2f}%; no alert needed.")
        return

    direction = "💹" if price_change > 0 else "📉"
    articles = get_news_articles()
    messages = [
        f"{STOCK_NAME}: {direction}{percentage_change:.2f}%\n"
        f"Headline: {article.get('title') or 'No title'}\n"
        f"Brief: {article.get('description') or 'No description'}"
        for article in articles
    ]

    if not messages:
        print("No Tesla news articles were returned; no SMS alerts sent.")
        return

    send_alerts(messages)
    print(f"Sent {len(messages)} stock alert(s).")


if __name__ == "__main__":
    main()
