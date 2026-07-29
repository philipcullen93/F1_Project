from api.jolpica import get_current_drivers
from services.driver_service import process_drivers
import json

def main():

    print("Retrieving F1 drivers...")

    data = get_current_drivers()

    drivers = process_drivers(data)

    print("\nCurrent F1 Drivers")
    print("------------------")

    for driver in drivers:
        print(driver)


if __name__ == "__main__":
    main()