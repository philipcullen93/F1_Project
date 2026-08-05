from models.qualifying_result import QualifyingResult

def process_qualifying_results(api_response):

    results = []

    races = (
        api_response["MRData"]
        ["RaceTable"]
        ["Races"]
    )

    if not races:
        return results

    race = races[0]

    qualifying_results = race["QualifyingResults"]

    for result in qualifying_results:

        driver = result["Driver"]
        constructor = result["Constructor"]

        qualifying = QualifyingResult(
            season = race["season"],
            round = race["round"],
            race_name = race["raceName"],
            position = result["position"],
            driver_id = driver["driverId"],
            constructor_id = constructor["constructorId"],
            q1 = result.get("Q1"),
            q2 = result.get("Q2"),
            q3 = result.get("Q3")
        )

        results.append(qualifying)

    return results