class Driver:

    def __init__(
        self,
        driver_id,
        first_name,
        last_name,
        abbreviation=None,
        number=None,
        nationality=None,
        date_of_birth=None,
    ):

        self.driver_id = driver_id
        self.first_name = first_name
        self.last_name = last_name
        self.abbreviation = abbreviation
        self.number = number
        self.nationality = nationality
        self.date_of_birth = date_of_birth


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):

        number = self.number if self.number else "-"
        code = self.abbreviation if self.abbreviation else "---"

        return (
            f"{number} | "
            f"{code} | "
            f"{self.full_name}"
        )


    def to_dict(self):

        return {
            "driver_id": self.driver_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "abbreviation": self.abbreviation,
            "number": self.number,
            "nationality": self.nationality,
            "date_of_birth": self.date_of_birth
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            driver_id = data.get("driver_id"),
            first_name = data.get("first_name"),
            last_name = data.get("last_name"),
            abbreviation = data.get("abbreviation"),
            number = data.get("number"),
            nationality = data.get("nationality"),
            date_of_birth = data.get("date_of_birth"),
        )


