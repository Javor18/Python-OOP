from abc import ABC, abstractmethod


class BaseAquarium(ABC):

    def __init__(self, name: str, capacity: int):

        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fishes = []
        self.total_comfort = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        if value.strip() == '':

            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):

        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish):

        if len(self.fishes) == self.capacity:

            return "Not enough capacity."

        if fish.__class__.__name__ in ("FreshwaterFish", "SaltwaterFish"):
            self.fishes.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):

        for s_fish in self.fishes:
            if s_fish.name == fish.name:

                self.fishes.remove(s_fish)

    def add_decoration(self, decoration):

        self.decorations.append(decoration)

    def feed(self):

        for s_fish in self.fishes:

            s_fish.eat()

    def __str__(self):

        result = f"{self.name}:\n"

        if not self.fishes:

            result += 'Fish: none\n'

        else:
            result += f"Fish: {' '.join(fish.name for fish in self.fishes)}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}\n"

        return result.strip()