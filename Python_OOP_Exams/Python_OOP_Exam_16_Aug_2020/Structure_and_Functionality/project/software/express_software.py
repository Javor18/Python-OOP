"""
In the file express_software.py implement the ExpressSoftware class:
⦁	The express software is a type of software, and its type is "Express"
⦁	It has twice more memory consumption than the given value

"""

from project.software.software import Software


class ExpressSoftware(Software):

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Express", capacity_consumption, memory_consumption)

        self.memory_consumption *= 2
