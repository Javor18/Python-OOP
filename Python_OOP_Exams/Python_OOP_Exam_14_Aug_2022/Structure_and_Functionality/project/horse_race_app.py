from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_race import HorseRace
from project.jockey import Jockey

class HorseRaceApp:

    VALID_HORSE_BREEDS = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if horse_name in [h.name for h in self.horses]:

            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSE_BREEDS:
            self.horses.append(self.VALID_HORSE_BREEDS[horse_type](horse_name, horse_speed))

            return f"{horse_type} horse {horse_name} is added."

    """
    The method creates a horse and adds it to the horses' list.
    
    ⦁If the horse is successfully created and added, the method should return the message:
    "{horse_type} horse {horse_name} is added."

    ⦁If a horse with the same name already exists, raise an Exception with the message
     "Horse {horse_name} has been already added!"

    ⦁The valid types of horse breeds are "Appaloosa" and "Thoroughbred".
     All other types must be ignored.
"""

    def add_jockey(self, jockey_name: str, age: int):

        if jockey_name in [j.name for j in self.jockeys]:

            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    """
    The method creates a jockey and adds it to the jockeys' list.
    
    ⦁If the jockey is successfully created and added,
     the method should return the message "Jockey {jockey_name} is added."

    ⦁If a jockey with the given name already exists,
     raise an Exception with the message "Jockey {jockey_name} has been already added!"
    """

    def create_horse_race(self, race_type: str):

        if race_type in [r.race_type for r in self.horse_races]:

            raise Exception("Race {race type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    """
    The method creates a race and adds it to the horse races' list.

    ⦁When it is successfully created and added,
     the method returns the message "Race {race_type} is created."

    ⦁A race of each of the 4 types can be created just once.
    If a race of the same type already exists, raise an Exception
    with the message "Race {race type} has been already created!"
    """

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = list(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, self.horses))[-1]

        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    """
    Sets the last horse added from the given horse type to the jockey with the given name (if they both exist).
    
    ⦁If the jockey does NOT exist in the jockeys' list,
    raise an Exception with the message
    "Jockey {jockey_name} could not be found!"

    ⦁If there is no available horse (all horses of that type are taken, or no horse of that type exists)
    of the given type in the horses' list,
    raise an Exception with the message "Horse breed {horse_type} could not be found!".
    
    ⦁If there is an available horse (the horse is not taken),
    but the jockey already has a horse, return the message:
    "Jockey {jockey_name} already has a horse."
    
    ⦁If the horse can be added to the jockey, take it, and set it to the jockey.
    Then, return the message:
    "Jockey {jockey_name} will ride the horse {horse_name}."

    """

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        try:
            horse_race = next(filter(lambda r: r.race_type == race_type, self.horse_races))

        except StopIteration:
            raise Exception("Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:

            raise Exception("Jockey {jockey_name} could not be found!")

        if not jockey.horse:

            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:

            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    """
    Adds a jockey (object) to the given horse race type (if they both exist).
    A jockey can only participate in a horse race if he has a horse.
    
    ⦁	If a horse race of that type does NOT exist in the list with horse races,
        raise an Exception with the message "Race {race_type} could not be found!"
    
    ⦁	If the jockey does NOT exist in the jockeys' list,
        raise an Exception with the message "Jockey {jockey_name} could not be found!"
    
    ⦁	If the jockey is on the jockeys' list, but he/she doesn't have a horse,
        raise an Exception with the message "Jockey {jockey_name} cannot race without a horse!"
    
    ⦁	If the jockey has already been added to the horse race, return the message
        "Jockey {jockey_name} has been already added to the {race_type} race."

    ⦁	If both the race type and the jockey exist and the jockey has a horse,
        add the jockey (object) to the given horse race and return the message:
        "Jockey {jockey_name} added to the {race_type} race."
"""

    def start_horse_race(self, race_type: str):

        try:
            horse_race = next(filter(lambda r: r.race_type == race_type, self.horse_races))

        except StopIteration:

            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:

            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        winner = None

        for jockey in horse_race.jockeys:

            if jockey.horse.speed > highest_speed:

                highest_speed = jockey.horse.speed
                winner = jockey

            return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {winner.name}!"\
                   f"Winner's horse: {winner.horse.name}."

    """
    ⦁	If the horse race does NOT exist,
        raise an Exception with the message
        "Race {race_type} could not be found!"
    
    ⦁	The participants in a horse race must be at least 2.
        Otherwise, raise an Exception with the message
        "Horse race {race_type} needs at least two participants!"
    
    ⦁	If the race can be started, you should choose the winner
        - he/she is the jockey who rode the horse with the highest speed.
        Note: there will NOT be two or more jockeys riding their horse at the same highest speed.
        In the end, return the message: 
        "The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_name}!
         Winner's horse: {horse_name}."
    """