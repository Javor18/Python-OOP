class Horse:

    MAX_SPEED = 0

    def __init__(self, name, speed):

        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        if not isinstance(value, str) or len(value) < 4:

            raise ValueError(f"Horse name {value} is less than 4 symbols!")

        self.__name = value

    """
    ⦁	A string that represents the name of the horse.
    ⦁	If the name is less than 4 symbols, raise a ValueError with the message 
        "Horse name {value} is less than 4 symbols!"
    """

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):

        if not isinstance(value, int) or value > self.MAX_SPEED:

            raise ValueError("Horse speed is too high!")

        self.__speed = value

    """
   ⦁	An integer representing the speed that the horse can achieve.
   ⦁	Keep in mind that each horse breed has a different maximum speed, which cannot be exceeded.
        If the given horse speed exceeds the maximum, raise a ValueError with the message: "Horse speed is too high!"

    """

    def train(self):

        pass

    """
    Each horse can be additionally trained during the race days.
    When a horse is trained, it increases its speed by a value depending on its type.
    During training, a horse cannot exceed its maximum speed
    (just set its speed to the maximum one without raising an error).

    """