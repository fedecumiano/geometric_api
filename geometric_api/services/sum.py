"""
from abc import ABC, abstractmethod

# ABC = Abstract Base Class

class SumOperation(ABC):
    @abstractmethod
    def calculate(self, figures: list) -> float:
        pass


class PerimeterSum(SumOperation):
    def calculate(self, figures: list) -> float:
        return sum([f.calculate_perimeter() for f in figures])


class AreaSum(SumOperation):
    def calculate(self, figures: list) -> float:
        return sum([f.calculate_area() for f in figures])
"""


def _area(figures: list) -> float:
    return sum([f.calculate_area() for f in figures])


def _perimeter(figures: list) -> float:
    return sum([f.calculate_perimeter() for f in figures])


operations = {
    "area": _area,
    "perimeter": _perimeter,
}
