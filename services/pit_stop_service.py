from models.pit_stop import PitStop

def process_pit_stops(api_response, constructor_map = None):

    pit_stops = []

    races = (
        api_response["MRData"]
        ["RaceTable"]
        ["Races"]
    )

    if not races:
        return pit_stops

    race = races[0]

    stops = race.get(
        "PitStops",
        []
    )

    for stop in stops:

        driver_id = stop.get("driverId")

        constructor_id = None

        if constructor_map:
            constructor_id = constructor_map.get(
                driver_id
            )

        pit_stop = PitStop(
            season = race.get("season"),
            round = race.get("round"),
            race_name = race.get("raceName"),
            driver_id = driver_id,
            constructor_id = constructor_id,
            stop = stop.get("stop"),
            lap = stop.get("lap"),
            time = stop.get("time"),
            duration = stop.get("duration")
        )

        pit_stops.append(
            pit_stop
        )

    return pit_stops