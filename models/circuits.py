class Circuits:

    def __init__(
        self,
        circuit_id,
        name,
        locality,
        country,
        latitude,
        longitude,
        url=None
    ):

        self.circuit_id = circuit_id
        self.name = name
        self.locality = locality
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.url = url


    def __str__(self):

        return f"{self.name} | {self.locality}, {self.country}"


    def to_dict(self):

        return {
            "circuit_id": self.circuit_id,
            "name": self.name,
            "locality": self.locality,
            "country": self.country,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "url": self.url
        }


    @classmethod
    def from_dict(cls, data):

        return cls(
            circuit_id=data.get("circuit_id"),
            name=data.get("name"),
            locality=data.get("locality"),
            country=data.get("country"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            url=data.get("url")
        )