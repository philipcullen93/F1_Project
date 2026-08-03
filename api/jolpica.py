import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def make_request(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

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