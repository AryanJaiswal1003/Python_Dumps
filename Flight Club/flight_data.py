class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(data, return_date):
    # Handle empty data if no flight data is returned.
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    # Combine best_flights and other_flights into one list.
    all_flights = data.get("best_flights", []) + data.get("other_flights", [])
    cheapest_flight = None

    for flight in all_flights:
        price = flight.get("price")
        segments = flight.get("flights")
        if price is None or not isinstance(segments, list) or not segments:
            print("--- No price available for flight. ---")
            continue

        if cheapest_flight is None or price < cheapest_flight.price:
            first_segment = segments[0]
            last_segment = segments[-1]
            origin = first_segment["departure_airport"]["id"]
            destination = last_segment["arrival_airport"]["id"]
            out_date = first_segment["departure_airport"]["time"].split(" ")[0]
            stops = len(segments) - 1
            cheapest_flight = FlightData(
                price, origin, destination, out_date, return_date, stops
            )
            print(f"Lowest price to {destination} is GBP {price}")

    if cheapest_flight is None:
        print("No usable priced flight itineraries were returned.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")
    return cheapest_flight
