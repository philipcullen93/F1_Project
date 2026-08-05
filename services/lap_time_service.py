from models.lap_time import LapTime

def process_lap_times(api_response):

    lap_times = []

    races = (
        api_response["MRData"]
        ["RaceTable"]
        ["Races"]
    )

    if not races:
        return lap_times

    race = races[0]

    laps = race.get(
        "Laps",
        []
    )

    for lap in laps:

        timings = lap.get(
            "Timings",
            []
        )

        for timing in timings:

            lap_time = LapTime(
                season = race["season"],
                round = race["round"],
                race_name = race["raceName"],
                driver_id= timing["driverId"],
                lap = lap["number"],
                position = timing["position"],
                time = timing["time"]
            )

            lap_times.append(
                lap_time
            )

    return lap_times
