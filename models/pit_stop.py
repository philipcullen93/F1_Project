class PitStop:

    def __init__(
            self,
            season,
            round,
            race_name,
            driver_id,
            constructor_id,
            stop,
            lap,
            time,
            duration
    ):

        self.season = season
        self.round = round
        self.race_name = race_name
        self.driver_id = driver_id
        self.constructor_id = constructor_id
        self.stop = stop
        self.lap = lap
        self.time = time
        self.duration = duration

    def __str__(self):

        return (
            f"{self.driver_id} "
            f"({self.constructor_id}) - "
            f"Stop {self.stop}: "
            f"{self.duration}s"
        )

    def to_dict(self):

        return {
            "season": self.season,
            "round": self.round,
            "race_name": self.race_name,
            "driver_id": self.driver_id,
            "constructor_id": self.constructor_id,
            "stop": self.stop,
            "lap": self.lap,
            "time": self.time,
            "duration": self.duration
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            season = data.get("season"),
            round = data.get("round"),
            race_name = data.get("race_name"),
            driver_id = data.get("driver_id"),
            constructor_id = data.get("constructor_id"),
            stop = data.get("stop"),
            lap = data.get("lap"),
            time = data.get("time"),
            duration = data.get("duration")
        )