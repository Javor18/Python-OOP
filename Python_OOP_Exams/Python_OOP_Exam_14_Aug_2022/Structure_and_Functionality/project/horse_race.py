class HorseRace:

    VALID_RACE_TYPES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, race_type):

        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):

        if value not in self.VALID_RACE_TYPES:

            raise ValueError("Race type does not exist!")

        self.__race_type = value

    """
        If the race type is NOT one of the above-mentioned,
        raise a ValueError with the message: "Race type does not exist!"    
    """