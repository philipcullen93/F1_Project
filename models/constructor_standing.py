class ConstructorStanding:

    def __init__(
            self,
            season,
            round,
            position,
            points,
            wins,
            constructor_id
    ):

        self.season = season
        self.round = round
        self.position = position
        self.points = points
        self.wins = wins
        self.constructor_id = constructor_id

    def __str__(self):

        return (
            f"{self.position}."
            f"{self.constructor_id} - "
            f"{self.points} points"
        )

    def to_dict(self):

        return{
            "season": self.season,
            "round": self.round,
            "position": self.position,
            "points": self.points,
            "wins": self.wins,
            "constructor_id": self.constructor_id
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            season = data.get("season"),
            round = data.get("round"),
            position = data.get("position"),
            points = data.get("points"),
            wins = data.get("wins"),
            constructor_id = data.get("constructor_id")
        )