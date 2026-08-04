from api.jolpica import get_race_results
from services.race_result_service import process_race_results


data = get_race_results(
    "2026",
    "1"
)


results = process_race_results(data)


for result in results:
    print(result)