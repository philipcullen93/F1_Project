# F1 Data Platform


# ==========================
# Imports
# ==========================

from api.jolpica import (
    get_current_drivers,
    get_current_constructors,
    get_current_circuits,
    get_current_schedule
)
from services.driver_service import (
    process_drivers, 
    load_drivers
)
from services.data_service import (
    save_json, 
    load_json
)
from services.constructors_service import (
    process_constructors
)
from services.circuits_services import (
    process_circuits
)
from models.constructor import (
    Constructor
)
from models.circuits import (
    Circuits
)
from services.race_service import (
    process_races,
    load_races
)
from models.race import(
    Race
)
from config import (
    set_current_season,
    get_data_folder
)

# ==========================
# Season Selection
# ==========================

def select_season():

    print("\nPlease Select a Season")
    print("-------------------------")
    print("1. 2026")
    print("2. 2027")
    print("0. Exit")

    choice = input("\n Select Season:")

    if choice == "1":
        set_current_season("2026")
        return True

    elif choice == "2":
        set_current_season("2027")
        return True

    elif choice == "0":
        return False

    else:
        print("Invalid Option")
        return False

# ==========================
# Driver Functions
# ==========================

def import_drivers():

    print("\nImporting Drivers")

    data = get_current_drivers()
    drivers = process_drivers(data)

    driver_data = [driver.to_dict() for driver in drivers]

    save_json(driver_data, f"{get_data_folder()}/drivers.json")
    print(f"{len(drivers)} drivers imported successfully")

def list_drivers():

    print("\nCurrent Drivers")
    print("-----------")

    driver_data = load_json(f"{get_data_folder()}/drivers.json")
    drivers = load_drivers(driver_data)

    for driver in drivers:
        print(driver)

# ==========================
# Constructor Functions
# ==========================

def import_constructors():

    print("\nImporting Constructors")

    data = get_current_constructors()
    constructors = process_constructors(data)

    constructor_data = [
        constructor.to_dict()
        for constructor in constructors
    ]

    save_json(
        constructor_data,
        f"{get_data_folder()}/constructors.json"
    )

    print(
        f"{len(constructors)} constructors imported successfully"
    )

def list_constructors():

    print("\nCurrent Constructors")
    print("------------------------")

    constructor_data = load_json(
        f"{get_data_folder()}/constructors.json"
    )

    constructors = [
        Constructor.from_dict(data)
        for data in constructor_data
    ]

    for constructor in constructors:
        print(constructor)

# ==========================
# Circuit Functions
# ==========================

def import_circuits():

    print("\nImporting Circuits")

    data = get_current_circuits()
    circuits = process_circuits(data)

    circuit_data = [
        circuit.to_dict()
        for circuit in circuits
    ]

    save_json(
        circuit_data,
        f"{get_data_folder()}/circuits.json"
    )
    
    print(
        f"{len(circuits)} circuits imported successfully"
    )

def list_circuits():

    print("\nCurrent Circuits")
    print("-------------------------")

    circuit_data = load_json(
        f"{get_data_folder()}/circuits.json"
    )

    circuits = [
        Circuits.from_dict(data)
        for data in circuit_data
    ]

    for circuit in circuits:
        print(circuit)

# ==========================
# Race Functions
# ==========================

def import_races():

    print("\nImporting Race Calender")

    data = get_current_schedule()
    races = process_races(data)

    race_data = [
        race.to_dict()
        for race in races
    ]

    save_json(
        race_data,
        f"{get_data_folder()}/races.json"
    )

    print(
        f"{len(races)} races imported successfully")

def list_races():

    print("\nCurrent Race Calender")
    print("-------------------------")

    race_data = load_json(
        f"{get_data_folder()}/races.json"
    )

    races = load_races(race_data)

    for race in races:
        print(race)

# ==========================
# Main Menu
# ==========================
def display_menu():

    print("\n=========================")
    print("F1 Data Management")
    print("=========================")
    print("1. Import Drivers")
    print("2. List Drivers")
    print("3. Import Constructors")
    print("4. List Constructors")
    print("5. Import Circuits")
    print("6. List Circuits")
    print("7. Import Race Calender")
    print("8. List Race Calender")
    print("0. Exit")

# ==========================
# Main Menu Program
# ==========================

def main():

    if not select_season():
        print("Goodbye")
        return

    while True:

        display_menu()

        choice = input("\nSelect an Option:")

        if choice == "1":
            import_drivers()

        elif choice == "2":
            list_drivers()

        elif choice == "3":
            import_constructors()

        elif choice == "4":
            list_constructors()

        elif choice == "5":
            import_circuits()

        elif choice == "6":
            list_circuits()

        elif choice == "7":
           import_races()

        elif choice == "8":
            list_races()

        elif choice == "0":
            print("\nGoodbye")
            break

        else:
            print("\nInvalid option, please select a valid option")

if __name__ == "__main__":
    main()

