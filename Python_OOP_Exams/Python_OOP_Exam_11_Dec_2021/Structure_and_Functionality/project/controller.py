from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.race import Race
from project.driver import Driver


class Controller:

    def __init__(self):

        self.cars = []
        self.drivers = []
        self.races = []

        self.valid_car_types = {'MuscleCar': MuscleCar, 'SportsCar': SportsCar}

    def create_car(self, car_type: str, model: str, speed_limit: int):

        if car_type not in ['MuscleCar', 'SportsCar']:

            return

        if model in [c.model for c in self.cars]:

            raise Exception(f"Car {model} is already created!")

        new_car = self.valid_car_types[car_type](model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):

        if driver_name in [d.name for d in self.drivers]:

            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):

        if race_name in [r.name for r in self.races]:

            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def __find_driver_by_name(self, driver_name):

        for s_driver in self.drivers:

            if s_driver.name == driver_name:

                return s_driver

        raise Exception(f"Driver {driver_name} could not be found!")

    def __find_last_car_by_type(self, car_type):

        searched_car = [car for car in self.cars if type(car).__name__ == car_type and not car.is_taken]

        if searched_car:

            return searched_car[-1]

        raise Exception(f'Car {car_type} could not be found!')

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        car = self.__find_last_car_by_type(car_type)
        if driver.car:
            old_car = driver.car
            new_car = car

            driver.car = car
            car.is_taken = True
            old_car.is_taken = False
            return f"Driver {driver_name} changed his car from {old_car.model} to {new_car.model}."

        driver.car = car
        car.is_taken = True
        return f'Driver {driver_name} chose the car {car.model}.'

    def __find_race_by_name(self, race_name):

        for s_race in self.races:

            if s_race.name == race_name:

                return s_race
        return f"Race {race_name} could not be found!"

    def add_driver_to_race(self, race_name: str, driver_name: str):

        race = self.__find_race_by_name(race_name)
        driver = self.__find_driver_by_name(driver_name)

        if driver in race.drivers:

            return f"Driver {driver_name} is already added in {race_name} race."

        if driver.car is None:

            raise Exception(f"Driver {driver_name} could not participate in the race!")

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):

        race = self.__find_race_by_name(race_name)

        if len(race.drivers) < 3:

            return f"Race {race_name} cannot start with less than 3 participants!"

        result = []

        for driver in sorted(race.drivers, key= lambda x: -x.car.speed_limit)[:3]:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name}"
                          f" wins the {race_name}"
                          f" race with a speed of"
                          f" {driver.car.speed_limit}.")

        return '\n'.join(result)