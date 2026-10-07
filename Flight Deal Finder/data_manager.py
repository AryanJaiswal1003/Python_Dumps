import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load credentials from the environment so secrets stay outside the source code.
load_dotenv()

# Sheety endpoint for the destination-price worksheet.
SHEETY_ENDPOINT = "https://api.sheety.co/0a65d0e14010e31a8f1a949a3af3e46e/flightDeals/prices"

class DataManager:
    """Read destinations and update their tracked lowest fares through Sheety."""

    def __init__(self):
        # Sheety uses HTTP Basic Auth; do not print or log these credential values.
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Fetch all destination rows so main.py can search each airport.
        if SHEETY_ENDPOINT is None:
            raise ValueError("SHEETY_ENDPOINT_FLIGHT is not set")
        response = requests.get(url=SHEETY_ENDPOINT, auth=self._authorization)
        data = response.json()
        # Sheety wraps the worksheet rows in a key named "prices".
        self.destination_data = data['prices']

        return self.destination_data

    def update_low_price(self, row_id, new_price):
        # Sheety expects the updated columns nested under the singular "price" row key.
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        # The row ID selects which destination's lowestPrice value is updated.
        requests.put(
            url = f"{SHEETY_ENDPOINT}/{row_id}",
            json = new_data,
            auth = self._authorization
        )
