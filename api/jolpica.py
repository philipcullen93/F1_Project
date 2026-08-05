import requests
import time

BASE_URL = "https://api.jolpi.ca/ergast/f1"


def make_request(endpoint):

    url = f"{BASE_URL}/{endpoint}?limit=1000"

    while True:

        try:

            response = requests.get(
                url,
                timeout=30
            )

            if response.status_code == 429:

                print(
                    "Rate limit reached. Waiting 30 seconds..."
                )
                time.sleep(30)
                continue

            response.raise_for_status()

            return response.json()


        except requests.exceptions.ConnectionError:

            print(
                "Connection interrupted. Retrying in 10 seconds..."
            )
            time.sleep(10)


        except requests.exceptions.Timeout:

            print(
                "Request timed out. Retrying in 10 seconds..."
            )
            time.sleep(10)

def get_current_drivers():
    # Retrieves the current list of drivers from Jolpica API
    return make_request(
        "current/drivers.json"
    )

def get_current_constructors():
    return make_request(
        "current/constructors.json"
    )

def get_current_circuits():
    return make_request(
        "current/circuits.json"
    )

def get_current_schedule():

    return make_request(
        "current.json"
    )

def get_driver_standings(season):

    return make_request(
        f"{season}/driverStandings.json"
    )

def get_constructor_standings(season):

    return make_request(
        f"{season}/constructorStandings.json"
    )

def get_race_results(season, round):

    return make_request(
        f"{season}/{round}/results.json"
    )

def get_qualifying_results(season, round):

    return make_request(
        f"{season}/{round}/qualifying.json"
    )

def get_pit_stops(season, round):

    return make_request(
        f"{season}/{round}/pitstops.json"
    )

def get_lap_times(season, round, driver_id):

    return make_request(
        f"{season}/{round}/drivers/{driver_id}/laps.json"
    )