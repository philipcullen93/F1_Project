from models.race import Race

def process_races(api_response):

    races = []

    race_list = (
        api_response["MRData"]
        ["RaceTable"]
        ["Races"]
    )

    for race_data in race_list:

        circuit = race_data["Circuit"]

        race = Race(
            season=race_data.get("season"),
            round=int(race_data.get("round")),
            raceName=race_data.get("raceName"),
            date=race_data.get("date"),
            time=race_data.get("time"),
            circuit_id=circuit.get("circuitId"),
            circuit_name=circuit.get("circuitName"),
            url=race_data.get("url")
        )

        races.append(race)

    return races

def load_races(race_data):

    return [
        Race.from_dict(data)
        for data in race_data
    ]