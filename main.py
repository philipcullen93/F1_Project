from api.jolpica import get_current_drivers
import json

def main():
    print("Connecting to Jolpica API")
    
    data = get_current_drivers()

    print("Successfull Connection\n")
    
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()

from models.driver import Driver

def main():

    driver = Driver(
        driver_id="max_verstappen",
        first_name="Max",
        last_name="Verstappen",
        abbreviation="VER",
        number=1,
        nationality="Dutch",
        date_of_birth="1997-09-30",
    )

    print(driver)


if __name__ == "__main__":
    main()