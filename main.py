# F1 Data Platform


# ==========================
# Imports
# ==========================

from api.jolpica import (
    get_current_drivers,
    get_current_constructors,
    get_current_circuits,
    get_current_schedule,
    get_driver_standings,
    get_constructor_standings
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
from services.season_service import (
    get_available_seasons,
    create_season_folder,
    get_current_season_folder
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
from models.driver_standing import(
    DriverStanding
)
from services.driver_standing_service import(
    process_driver_standings
)
from models.constructor_standing import(
    ConstructorStanding
)
from services.constructor_standing_service import(
    process_constructor_standing
)
from config import (
    set_current_season,
    get_data_folder,
    season_has_data
)

# ==========================
# Season Selection
# ==========================

def select_season():

    while True:

        print("\nPlease Select a Season")
        print("-------------------------")
        seasons = get_available_seasons()
        for index, season in enumerate(seasons, start = 1):
            print(f"{index}. {season}")
        print("0. Exit")

        choice = input("\n Select Season:")

        if choice == "0":
            return False

        if choice.isdigit():
            selection = int(choice)

            if 1 <= selection <= len(seasons):
                set_current_season(
                    seasons[selection - 1]
                )

            else:
                print("Invalid Season")
                continue

        else:
            print("Invalid Option")
            continue

        if season_has_data():
            return True
        print("\nNo current data available for this season")
        print("Please select another season")

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
# Driver Standings
# ==========================

def import_driver_standings():

    print("\nImporting Driver Standings")

    data = get_driver_standings("2026")
    standings = process_driver_standings(data)

    driver_standings_data = [
        standing.to_dict()
        for standing in standings
    ]

    save_json(
        driver_standings_data,
        f"{get_data_folder()}/driver_standings.json"
    )

    print(
            f"{len(standings)} driver standings imported successfully")

def list_driver_standings():

    print("\nCurrent Driver Standings")
    print("-------------------------")

    standing_data = load_json(
        f"{get_data_folder()}/driver_standings.json"
    )

    standings = [
        DriverStanding.from_dict(data)
        for data in standing_data
    ]

    for standing in standings:
        print(standing)

# ==========================
# Constructor Standings
# ==========================

def import_constructor_standings():

    print("\nImporting Constructor Standings")

    data = get_constructor_standings("2026")
    standings = process_constructor_standing(data)

    constructor_standings_data = [
        standing.to_dict()
        for standing in standings
    ]

    save_json(
        constructor_standings_data,
        f"{get_data_folder()}/constructor_standings.json"
    )

    print(
        f"{len(standings)} constructor standings imported successfully "
    )

def list_constructor_standings():

    print("\nCurrent Constructor Standings")
    print("-------------------------")

    standing_data = load_json(
        f"{get_data_folder()}/constructor_standings.json"
    )

    standings = [
        ConstructorStanding.from_dict(data)
        for data in standing_data
    ]

    for standing in standings:
        print(standing)

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
    print("9. Import Driver Standings")
    print("10. List Driver Standings")
    print("11. Import Constructor Standings")
    print("12. List Constructor Standings")
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

        elif choice == "9":
            import_driver_standings()

        elif choice == "10":
            list_driver_standings()

        elif choice == "11":
            import_constructor_standings()

        elif choice == "12":
            list_constructor_standings()

        elif choice == "0":
            print("\nGoodbye")
            break

        else:
            print("\nInvalid option, please select a valid option")

if __name__ == "__main__":
    main()

