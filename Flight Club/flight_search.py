import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

FLIGHTS_ENDPOINT = "https://app.100daysofpython.dev/v1/flights/search"


class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["FLIGHTS_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct = True):
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._api_key,
        }

        # Only executes if the stop parameter is True
        if is_direct:
            query["stops"] = "1"

        try:
            response = requests.get(
                url=FLIGHTS_ENDPOINT,
                params=query,
                timeout=30,
            )
            response.raise_for_status()
        except requests.RequestException as error:
            raise RuntimeError(
                f"Flight search request failed (HTTP "
                f"{error.response.status_code if error.response is not None else 'unavailable'})."
            ) from error

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type.lower():
            raise RuntimeError(
                "Flight search returned a non-JSON response "
                f"(HTTP {response.status_code}, Content-Type: "
                f"{content_type or 'unknown'}). Verify the flight API endpoint."
            )

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as error:
            raise RuntimeError(
                f"Flight search returned invalid JSON (HTTP {response.status_code})."
            ) from error

        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data
