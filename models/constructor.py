class Constructor:

    def __init__(
        self,
        constructor_id,
        name,
        nationality=None,
        url=None,
        ):


        self.constructor_id = constructor_id
        self.name = name
        self.nationality = nationality
        self.url = url

    def __str__(self):

        return f"{self.name} | {self.nationality}"  

    def to_dict(self):

        return{
            "constructor_id": self.constructor_id,
            "name": self.name,
            "nationality": self.nationality,
            "url": self.url
        }

    @classmethod

    def from_dict(cls, data):

        return cls(
            constructor_id = data.get("constructor_id"),
            name = data.get("name"),
            nationality = data.get("nationality"),
            url = data.get("url")
        )