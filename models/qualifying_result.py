class QualifyingResult:

    def __init__(
            self,
            season,
            round,
            race_name,
            position,
            driver_id,
            constructor_id,
            q1,
            q2,
            q3
    ):

        self.season = season
        self.round = round
        self.race_name = race_name
        self.position = position
        self.driver_id = driver_id
        self.constructor_id = constructor_id
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

    def __str__(self):

        return (
            f"{self.position}."
            f"{self.driver_id}"
        )

    def to_dict(self):

        return {
            "season": self.season,
            "round": self.round,
            "race_name": self.race_name,
            "position": self.position,
            "driver_id": self.driver_id,
            "constructor_id": self.constructor_id,
            "q1": self.q1,
            "q2": self.q2,
            "q3": self.q3
        }

    @classmethod

    def from_dict(cls, data):

        return cls(
            season = data.get("season"),
            round = data.get("round"),
            race_name = data.get("race_name"),
            position = data.get("position"),
            driver_id = data.get("driver_id"),
            constructor_id = data.get("constructor_id"),
            q1 = data.get("q1"),
            q2 = data.get("q2"),
            q3 = data.get("q3")
        )