from dataclasses import dataclass
from math import pi


@dataclass
class Figure:

    name: str

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


@dataclass
class Circle(Figure):

    radius: float

    def calculate_area(self):
        return pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * pi * self.radius


@dataclass
class Triangle(Figure):

    sides: list

    def calculate_area(self):
        s = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        area = (s * (s - self.sides[0]) * (s - self.sides[1]) *
                (s - self.sides[2]))**0.5
        return area

    def calculate_perimeter(self):
        return self.sides[0] + self.sides[1] + self.sides[2]


@dataclass
class Rectangle(Figure):

    side1: float
    side2: float

    def calculate_area(self):
        return self.side1 * self.side2

    def calculate_perimeter(self):
        return self.side1 * 2 + self.side2 * 2


@dataclass
class Square(Figure):

    side: float

    def calculate_area(self):
        return self.side**2

    def calculate_perimeter(self):
        return self.side * 4
