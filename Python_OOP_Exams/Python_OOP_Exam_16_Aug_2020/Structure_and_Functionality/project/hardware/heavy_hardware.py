"""
In the file heavy_hardware.py implement the HeavyHardware class:
⦁	Heavy hardware is a type of hardware, and its type is "Heavy"
⦁	It has twice more capacity than the given value
⦁	Its memory is 75% from the given value. The result should be rounded down to the nearest integer.

"""
import math

from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Heavy", capacity, memory)

        self.capacity *= 2
        self.memory = math.floor(self.memory * 0.75)
