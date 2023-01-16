"""
In the file power_hardware.py implement the PowerHardware class:
⦁	The power hardware is a type of hardware, and its type is "Power"
⦁	Its capacity is 25% of the given value. The result should be rounded down to the nearest integer.
⦁	It has 75% more memory than the given value. The result should be rounded down to the nearest integer.

"""

import math

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Power", capacity, memory)

        self.capacity = math.floor(self.capacity * 0.25)
        self.memory = math.floor(self.memory * 1.75)
