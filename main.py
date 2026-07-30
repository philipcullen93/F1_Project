from api.jolpica import get_current_drivers
from services.driver_service import process_drivers
from services.data_service import save_json


def main():

    print("Retrieving F1 drivers...")

    data = get_current_drivers()

    drivers = process_drivers(data)

    driver_data = [
        driver.to_dict()
        for driver in drivers
    ]

    save_json(
        driver_data,
        "data/2026/drivers.json"
    )

    print(
        f"Saved {len(drivers)} drivers to database."
    )


if __name__ == "__main__":
    main()
