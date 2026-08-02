

data = get_current_schedule()

races = process_races(data)

for race in races:
    print(race)
