from api.jolpica import get_driver_standings
from services.driver_standing_service import process_driver_standings

data = get_driver_standings("2026")

standings = process_driver_standings(data)

for standing in standings:
    print(standing)
