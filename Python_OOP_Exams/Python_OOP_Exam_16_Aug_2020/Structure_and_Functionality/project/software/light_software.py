"""
In the file light_software.py implement the LightSoftware class:
⦁	The light software is a type of software, and its type is "Light"
⦁	It has 50% more capacity consumption than the given value. The result should be rounded down to the nearest integer.
⦁	It has 50% less memory consumption than the given value. The result should be rounded down to the nearest integer.

"""
import math

from project.software.software import Software


class LightSoftware(Software):

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Light", capacity_consumption, memory_consumption)

        self.capacity_consumption *= 1.5
        self.capacity_consumption = math.floor(self.capacity_consumption)
        self.memory_consumption //= 2
