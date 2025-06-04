from dataclasses import dataclass


@dataclass
class Airport:
    ID: int
    IATA_CODE: str
    AIRPORT: str

    def __eq__(self, other):
        return self.ID == other.ID

    def __hash__(self):
        return hash(self.ID)

    def __str__(self):
        return f"{self.IATA_CODE} - {self.ID}"