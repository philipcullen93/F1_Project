from api.jolpica import get_lap_times
from services.lap_time_service import process_lap_times


data = get_lap_times(
    "2026",
    "1",
    "russell"
)

lap_times = process_lap_times(data)

print(len(lap_times))

for lap in lap_times[:5]:
    print(lap)