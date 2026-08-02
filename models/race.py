class Race:

    def __init__(
        self,
        season,
        round,
        raceName,
        date,
        time,
        circuit_id,
        circuit_name,
        url = None
    ):

        self.season = season
        self.round = round
        self.raceName = raceName
        self.date = date
        self.time = time
        self.circuit_id = circuit_id
        self.circuit_name = circuit_name
        self.url = url

    def __str__(self):

        return f"Round {self.round}: {self.raceName} | {self.circuit_name}"

    def to_dict(self):

        return {
            "season": self.season,
            "round" : self.round,
            "raceName": self.raceName,
            "date": self.date,
            "time": self.time,
            "circuit_id": self.circuit_id,
            "circuit_name": self.circuit_name,
            "url": self.url
        }

    @classmethod

    def from_dict(cls, data):

        return cls(
            season = data.get("season"),
            round = data.get("round"),
            raceName = data.get("raceName"),
            date = data.get("date"),
            time = data.get("time"),
            circuit_id = data.get("circuit_id"),
            circuit_name = data.get("circuit_name"),
            url = data.get("url")
        )