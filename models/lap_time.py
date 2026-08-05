class LapTime:

    def __init__(
        self,
        season,
        round,
        race_name,
        driver_id,
        lap,
        position,
        time
    ):

        self.season = season
        self.round = round
        self.race_name = race_name
        self.driver_id = driver_id
        self.lap = lap
        self.position = position
        self.time = time

    def __str__(self):

        return (
            f"{self.driver_id} - "
            f"Lap {self.lap}: "
            f"{self.time}"
        )

    def to_dict(self):

        return {
            "season": self.season,
            "round": self.round,
            "race_name": self.race_name,
            "driver_id": self.driver_id,
            "lap": self.lap,
            "position": self.position,
            "time": self.time
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            season = data.get("season"),
            round = data.get("round"),
            race_name = data.get("race_name"),
            driver_id = data.get("driver_id"),
            lap = data.get("lap"),
            position = data.get("position"),
            time = data.get("time")
        )