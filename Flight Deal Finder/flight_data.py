class FlightData:
    """Store the fields needed to compare a fare and describe the selected trip."""

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheap_flight(data, return_date):
    """Choose the least expensive result and return it as a FlightData object."""
    # Keep the caller's flow predictable when the API has no usable flight results.
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No Flight Data Available")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    # The API separates recommended and other fares; compare both groups.
    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    # Seed the minimum with the first result, then replace it only with cheaper fares.
    first_flight = all_flights[0]
    lowest_price = first_flight["price"]
    origin = first_flight["flights"][0]["departure_airport"]["id"]
    destination = first_flight["flights"][-1]["arrival_airport"]["id"]
    out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

    # Store the first fare in the same shape that callers use for notifications.
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    for flight in all_flights:
        # Ignore malformed entries without a price, but continue checking other results.
        try:
            price = flight["price"]
        except KeyError:
            print("------- NO PRICE AVAILABLE FOR THE FLIGHT -------")
            continue

        if price < lowest_price:
            # Extract the selected itinerary's endpoints and outbound date for the alert.
            lowest_price = price
            origin = flight["flights"][0]["departure_airport"]["id"]
            destination = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest Price to {destination} is GBP {lowest_price}")

    return cheapest_flight