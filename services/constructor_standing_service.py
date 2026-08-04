from models.constructor_standing import ConstructorStanding

def process_constructor_standing(api_response):

    standings = []

    standings_table = (
        api_response["MRData"]
        ["StandingsTable"]
        ["StandingsLists"][0]
        ["ConstructorStandings"]
    )

    for standing_data in standings_table:

        constructor = standing_data["Constructor"]

        standing = ConstructorStanding(
            season = (
                api_response["MRData"]
                ["StandingsTable"]
                ["season"]
            ),

            round = (
                api_response["MRData"]
                ["StandingsTable"]
                ["StandingsLists"][0]
                ["round"]
            ),

            points = standing_data.get("points"),
            position = standing_data.get("position"),
            wins = standing_data.get("wins"),
            constructor_id = constructor.get("constructorId")
        )

        standings.append(standing)

    return standings