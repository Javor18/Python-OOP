import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.__r = r

    def calculate_area(self):
        return math.pi * self.__r * self.__r

    def calculate_perimeter(self):
        return 2 * math.pi * self.__r


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.__a = a
        self.__b = b

    def calculate_area(self):
        return self.__a * self.__b

    def calculate_perimeter(self):
        return 2 * (self.__a + self.__b)

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())