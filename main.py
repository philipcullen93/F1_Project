from api.jolpica import get_current_drivers
from services.driver_service import process_drivers, load_drivers
from services.data_service import save_json, load_json
from models.constructor import Constructor

def test_constructor():

    constructor = Constructor(
        "red_bull",
        "Red Bull Racing",
        "Austrian"
    )

    print(constructor)


if __name__ == "__main__":
    test_constructor()

def import_drivers():

    print("\nImporting Drivers")

    data = get_current_drivers()
    drivers = process_drivers(data)

    driver_data = [driver.to_dict() for driver in drivers]

    save_json(driver_data, "data/2026/drivers.json")
    print(f"{len(drivers)} drivers imported successfully")

def list_drivers():

    print("\nCurrent Drivers")
    print("-----------")

    driver_data = load_json("data/2026/drivers.json")
    drivers = load_drivers(driver_data)

    for driver in drivers:
        print(driver)

def main():

    while True:

        print("\n=========================")
        print("F1 Data Management")
        print("=========================")
        print("1. Import Drivers")
        print("2. List Drivers")
        print("3. Import Constructors")
        print("4. List Constructors")
        print("0. Exit")

        choice = input("\nSelect an Option:")

        if choice == "1":
            import_drivers()

        elif choice == "2":
            list_drivers()

        elif choice == "3":
            import_constructors()

        elif choice == "4":
            list_constructors()

        elif choice == "0":
            print("\nGoodbye")
            break

        else:
            print("\nInvalid option, please select a valid option")

if __name__ == "__main__":
    main()

