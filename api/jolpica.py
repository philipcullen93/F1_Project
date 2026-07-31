import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def get_current_drivers():
    # Retrieves the current list of drivers from Jolpica API
    url = f"{BASE_URL}/current/drivers.json"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_current_constructors():
    url = f"{BASE_URL}/current/constructors.json"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_current_circuits():
    url = f"{BASE_URL}/current/circuits.json"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()