from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    BREATHEN_OXYGEN = 5

    def __init__(self, name: str):
        super().__init__(name, 70)

    def breathe(self):

        self.oxygen -= self.BREATHEN_OXYGEN