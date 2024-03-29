from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):

    BREATHEN_OXYGEN = 15

    def __init__(self, name: str):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= self.BREATHEN_OXYGEN