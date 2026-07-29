import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def get_current_drivers():
    # Retrieves the current list of drivers from Jolpica API
    url = f"{BASE_URL}/current/drivers"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()