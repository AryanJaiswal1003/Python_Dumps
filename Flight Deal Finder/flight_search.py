import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load the shared repository .env file, regardless of the current working directory.
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# The API returns flight search results in a SerpAPI-compatible format.
FLIGHT_API_ENDPOINT = "https://app.100daysofpython.dev/v1/flights/search"

class FlightSearch:
    """Build requests to the Flights API and return validated JSON results."""

    def __init__(self):
        # Fail early with a useful message instead of raising a KeyError later.
        self._api_key = os.getenv("FLIGHTS_API_KEY")
        if not self._api_key:
            raise ValueError(
                "FLIGHTS_API_KEY is missing. Add it to the repository .env file "
                "or configure it as an environment variable."
            )

    def check_flight(self, origin_code, destination_code, from_time, to_time):
        # These query parameters follow the Flights API's documented request format.
        params = {
            "engine": "google_flights",
            "departure_id": origin_code,
            "arrival_id": destination_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._api_key,
        }

        try:
            # A timeout prevents a stalled API connection from blocking the program forever.
            response = requests.get(
                url=FLIGHT_API_ENDPOINT,
                params=params,
                timeout=30,
            )
        except requests.RequestException as error:
            raise RuntimeError("Could not connect to the Flights API.") from error

        # Report HTTP failures before attempting to parse a likely non-JSON error page.
        if response.status_code != 200:
            print(f"check_flight() Response Code: {response.status_code}")
            return None

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as error:
            # Include response metadata to help identify redirects or server error pages.
            content_type = response.headers.get("Content-Type", "unknown")
            raise RuntimeError(
                "The Flights API returned a non-JSON response "
                f"(HTTP {response.status_code}, Content-Type: {content_type}). "
                "Verify the API endpoint and try again."
            ) from error

        # Downstream code expects a JSON object containing flight result lists.
        if not isinstance(data, dict):
            raise RuntimeError("The Flights API returned an unexpected response format.")

        # Keep the status check as a safeguard if the accepted HTTP statuses change.
        if not response.ok:
            detail = data.get("error", f"HTTP {response.status_code}")
            raise RuntimeError(f"The Flights API rejected the request: {detail}")

        # The API can also encode an error in its JSON body.
        if "error" in data:
            raise RuntimeError(f"The Flights API returned an error: {data['error']}")

        return data