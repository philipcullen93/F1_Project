from models.driver import Driver


def process_drivers(api_response):
    drivers = []

    # Show what is inside DriverTable
    print("DriverTable keys:")
    print(api_response["MRData"]["DriverTable"].keys())
    print()

    driver_list = api_response["MRData"]["DriverTable"]["Drivers"]

    for driver_data in driver_list:

        # Print each driver's raw data
        print("Processing driver:")
        print(driver_data)
        print("-" * 50)

        driver = Driver(
            driver_id=driver_data.get("driverId"),
            first_name=driver_data.get("givenName"),
            last_name=driver_data.get("familyName"),
            abbreviation=driver_data.get("code", "N/A"),
            number=int(driver_data["permanentNumber"]) if driver_data.get("permanentNumber") else None,
            nationality=driver_data.get("nationality", "Unknown"),
            date_of_birth=driver_data.get("dateOfBirth"),
        )

        drivers.append(driver)

    return drivers