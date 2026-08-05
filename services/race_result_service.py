from models.race_result import RaceResult

def process_race_results(api_response):

    results = []

    races = (
        api_response["MRData"]
        ["RaceTable"]
        ["Races"]
    )

    if not races:
        return results

    race_data = races[0]

    season = api_response["MRData"]["RaceTable"]["season"]
    round = api_response["MRData"]["RaceTable"]["round"]

    race_name = race_data["raceName"]

    result_data = race_data["Results"]

    for result in result_data:

        driver = result["Driver"]
        constructor = result["Constructor"]

        race_result = RaceResult(
            season=season,
            round=round,
            race_name=race_name,
            position=result.get("position"),
            points=result.get("points"),
            grid=result.get("grid"),
            laps=result.get("laps"),
            status=result.get("status"),
            driver_id=driver.get("driverId"),
            constructor_id=constructor.get("constructorId")
        )

        results.append(race_result)

    return results