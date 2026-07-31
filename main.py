from api.jolpica import get_current_drivers
from services.driver_service import process_drivers
from services.data_service import save_json
from services.data_service import load_json
from services.driver_service import load_drivers

def main():

    driver_data = load_json("data/2026/drivers.json")

    drivers = load_drivers(driver_data)

    print("Drivers loaded from database")
    print("----------------------------")

    for driver in drivers:
        print(driver)


if __name__ == "__main__":
    main()