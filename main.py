from api.jolpica import get_current_drivers
from api.jolpica import get_current_constructors
from api.jolpica import get_current_circuits
from services.driver_service import process_drivers, load_drivers
from services.data_service import save_json, load_json
from services.constructors_service import process_constructors
from services.circuits_services import process_circuits
from models.constructor import Constructor
from models.circuits import Circuits

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
        "data/2026/constructor.json"
    )

    print(
        f"{len(constructors)} constructors imported successfully"
    )

def list_constructors():

    print("\nCurrent Constructors")
    print("------------------------")

    constructor_data = load_json(
        "data/2026/constructor.json"
    )

    constructors = [
        Constructor.from_dict(data)
        for data in constructor_data
    ]

    for constructor in constructors:
        print(constructor)

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
        "data/2026/circuits.json"
    )
    
    print(
        f"{len(circuits)} circuits imported successfully"
    )

def list_circuits():

    print("\nCurrent Circuits")
    print("-------------------------")

    circuit_data = load_json(
        "data/2026/circuits.json"
    )

    circuits = [
        Circuits.from_dict(data)
        for data in circuit_data
    ]

    for circuit in circuits:
        print(circuit)

def main():

    while True:

        print("\n=========================")
        print("F1 Data Management")
        print("=========================")
        print("1. Import Drivers")
        print("2. List Drivers")
        print("3. Import Constructors")
        print("4. List Constructors")
        print("5. Import Circuits")
        print("6. List Circuits")
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

        elif choice == "5":
            import_circuits()

        elif choice == "6":
            list_circuits()

        elif choice == "0":
            print("\nGoodbye")
            break

        else:
            print("\nInvalid option, please select a valid option")

if __name__ == "__main__":
    main()

