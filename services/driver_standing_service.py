from models.driver_standing import DriverStanding

def process_driver_standings(api_response):

    standings = []

    standings_table = (
        api_response["MRData"]
        ["StandingsTable"]
        ["StandingsLists"][0]
        ["DriverStandings"]
    )

    for standing_data in standings_table:

        driver = standing_data["Driver"]

        constructor = standing_data["Constructors"][0]

        standing = DriverStanding(
            season = api_response["MRData"]["StandingsTable"]["season"],
            round = api_response["MRData"]["StandingsTable"]["StandingsLists"][0]["round"],
            position = standing_data.get("position"),
            points = standing_data.get("points"),
            wins = standing_data.get("wins"),
            driver_id = driver.get("driverId"),
            constructor_id = constructor.get("constructorId")
        )

        standings.append(standing)

    return standings

