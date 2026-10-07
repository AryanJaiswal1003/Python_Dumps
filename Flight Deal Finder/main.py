# pprint makes progress and result dictionaries easier to read in the console.
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheap_flight
from notification_manager import NotificationManager


# Load the saved destination list, then prepare the API clients used below.
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data) # Printing the sheet_data to verify that it includes the airport IATA codes for each city

flight_search = FlightSearch()
notification_manager = NotificationManager() # Creating an instance of the NotificationManager

# Search from tomorrow through roughly six months ahead.
tomorrow = datetime.now() + timedelta(days=1)
six_months_after = datetime.now() + timedelta(days=(6 * 30))

ORIGIN_CITY_IATA = "LHR"  # IATA code for London Heathrow, the departure airport.

"""

# ====================== FLIGHT SEARCH ======================
flights = flight_search.check_flight(
    origin_code = "LHR",
    destination_code = "CDG",
    from_time = tomorrow,
    to_time = six_months_after
)

# pprint(flights)

# ====================== SHOWING THE CHEAPEST FLIGHT ======================
cheapest_flight = find_cheap_flight(flights, return_date = six_months_after.strftime("%Y-%m-%d"))
pprint(f"{sheet_data[0]['city']}: GBP {cheapest_flight.price}")

if cheapest_flight.price != "N/A" and cheapest_flight.price < sheet_data[0]["lowestPrice"]:
    pprint(f"Lowest Price Flight found to {sheet_data[0]['city']}!")
    data_manager.update_low_price(sheet_data[0]['id'], cheapest_flight.price)

"""

# Check each destination from the sheet against its stored target price.

for destination in sheet_data:
    pprint(f"Getting Flights for {destination['city']}.....")

    flights = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time = tomorrow,
        to_time = six_months_after
    )

    cheapest_flight = find_cheap_flight(flights, return_date = six_months_after.strftime("%Y-%m-%d"))
    pprint(f"{destination["city"]}: GBP {cheapest_flight.price}")

    # Only write a new low price and send an alert when a real fare beats the saved target.
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower Price Flight found to {destination["city"]}!")
        data_manager.update_low_price(destination['id'], cheapest_flight.price)

        # On a Twilio trial this sends an approved generic template; a paid account can send the details.
        notification_manager.send_sms(
            message_body = f"Lowest Price Alert! Only GBP {cheapest_flight.price} to Fly "
                            f"From {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                            f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )

        # Uncomment this block after configuring the WhatsApp Sandbox or an approved sender.
        """
        notification_manager.send_whatsapp(
            message_body = f"Lowest Price Alert! Only GBP {cheapest_flight.price} to Fly "
                                        f"From {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                                        f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
        """