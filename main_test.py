from api.jolpica import get_lap_times


data = get_lap_times(
    "2026",
    "1",
    "russell"
)

print(type(data))
print(data)