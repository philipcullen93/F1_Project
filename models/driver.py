class Driver:
    def __init__(
            self,
            driver_id,
            first_name,
            last_name,
            abbreviation,
            number,
            nationality,
            date_of_birth,
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
            f"{self.number} | "
            f"{self.abbreviation} | "
            f"{self.full_name}"
        )


