from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):

        self.booths = []
        self.delicacies = []
        self.income = 0.0

        self.valid_delicacy_types = {
            'Gingerbread': Gingerbread,
            'Stolen': Stolen
        }

        self.valid_booth_types = {
            'Open Booth': OpenBooth,
            'Private Booth': PrivateBooth
        }

    def __validate_delicacy(self, delicacy_type):

        if delicacy_type in self.valid_delicacy_types:
            return True
        return False

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        if any(d.name == name for d in self.delicacies):

            raise Exception(f"{name} already exists!")

        if not self.__validate_delicacy(type_delicacy):

            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if self.__validate_delicacy(type_delicacy):
            delicacy = self.valid_delicacy_types[type_delicacy](name, price)
            self.delicacies.append(delicacy)
            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def find_booth_by_number(self, booth_number):

        for booth in self.booths:

            if booth.booth_number == booth_number:

                return booth

    def find_delicacy_by_name(self, delicacy_name):

        for delicacy in self.delicacies:

            if delicacy.name == delicacy_name:

                return delicacy

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        s_booth = self.find_booth_by_number(booth_number)

        if s_booth:

            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ("Open Booth", "Private Booth"):

            raise Exception(f"{type_booth} is not a valid booth!")

        else:
            booth = self.valid_booth_types[type_booth](booth_number, capacity)
            self.booths.append(booth)
            return f"Added booth number {booth_number} in the pastry shop."

    def __find_if_booth_is_reserved(self, number_of_people):

        for booth in self.booths:

            if not booth.is_reserved:

                if booth.capacity >= number_of_people:
                    return booth

    def reserve_booth(self, number_of_people):

        booth = self.__find_if_booth_is_reserved(number_of_people)

        if not booth:

            raise Exception(f"No available booth for {number_of_people} people!")

        elif booth:

            booth.reserve(number_of_people)
            return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        booth = self.find_booth_by_number(booth_number)

        if not booth:

            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.find_delicacy_by_name(delicacy_name)

        if not delicacy:

            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):

        booth = self.find_booth_by_number(booth_number)

        price = booth.price_for_reservation + sum([d.price for d in booth.delicacy_orders])

        result = f"Booth {booth_number}:\n"\
                 f"Bill: {price:.2f}lv."

        self.income += price

        booth.is_reserved = False
        booth.price_for_reservation = 0
        booth.delicacy_orders = []

        return result

    def get_income(self):

        return f"Income: {self.income:.2f}lv."

