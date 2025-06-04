from dataclasses import dataclass


@dataclass
class Rotta:
    a1: int
    a2: int
    totDistance: float
    nVoli: int

    def __post_init__(self):
        self.avgDistance = float(self.totDistance / self.nVoli)

    def __eq__(self, other):
        return self.a1 == other.a1 and self.a2 == other.a2

    def __hash__(self):
        return hash((self.a1, self.a2))

    def __str__(self):
        return f"{self.a1} - {self.a2}"