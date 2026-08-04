class RaceResult:

    def __init__(
        self,
        season,
        round,
        race_name,
        position,
        points,
        grid,
        laps,
        status,
        driver_id,
        constructor_id
    ):

        self.season = season
        self.round = round
        self.race_name = race_name
        self.position = position
        self.points = points
        self.grid = grid
        self.laps = laps
        self.status = status
        self.driver_id = driver_id
        self.constructor_id = constructor_id

    def __str__(self):

        return (
            f"{self.position}."
            f"{self.driver_id} - "
            f"{self.points} points"
        )

    def to_dict(self):

        return {
            "season": self.season,
            "round": self.round,
            "race_name": self.race_name,
            "position": self.position,
            "points": self.points,
            "grid": self.grid,
            "laps": self.laps,
            "status": self.status,
            "driver_id": self.driver_id,
            "constructor_id": self.constructor_id
        }

    @classmethod

    def from_dict(cls, data):

        return cls(
            season=data.get("season"),
            round=data.get("round"),
            race_name=data.get("race_name"),
            position=data.get("position"),
            points=data.get("points"),
            grid=data.get("grid"),
            laps=data.get("laps"),
            status=data.get("status"),
            driver_id=data.get("driver_id"),
            constructor_id=data.get("constructor_id")
        )