from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply
from project.player import Player
from abc import abstractmethod


class Controller:

    def __init__(self):

        self.players = []
        self.supplies = []

    def add_player(self, *players):

        successfully_added = []

        for p in players:

            if p not in self.players:

                self.players.append(p)

                successfully_added.append(p.name)

        return f"Successfully added: {', '.join(successfully_added)}"

    def add_supply(self, *supplies):

        for supply in supplies:

            self.supplies.append(supply)

    def __take_last_sustenance(self, sustenance_type):

        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == sustenance_type:
                return self.supplies.pop(i)

        if sustenance_type == "Food":
            raise Exception("There are no food supplies left!")

        if sustenance_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def __find_player_by_name(self, player_name):

        for player in self.players:

            if player.name == player_name:

                return player

    def sustain(self, player_name: str, sustenance_type: str):

        player = self.__find_player_by_name(player_name)

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        supply = self.__take_last_sustenance(sustenance_type)

        if supply:

            player.sustain_player(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def __attack(p1, p2):

        p2.stamina -= (p1.stamina / 2)

        if p1.stamina - (p2.stamina / 2) < 0:

            p1.stamina = 0

        else:
            p1.stamina -= (p2.stamina / 2)

        if p1.stamina < p2.stamina:

            return f"Winner: {p2.name}"

        else:
            return f"Winner: {p1.name}"

    @staticmethod
    def __check_if_the_player_cannot_duel(*players):

        result = []

        for player in players:

            if player.stamina == 0:

                result.append(f"Player {player.name} does not have enough stamina.")

        if result:

            return '\n'.join(result)

    def duel(self, first_player_name, second_player_name):

        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        result = self.__check_if_the_player_cannot_duel(first_player, second_player)

        if result:

            return result

        if first_player.stamina < second_player.stamina:

            return self.__attack(first_player, second_player)

        else:
            return self.__attack(second_player, first_player)

    def next_day(self):

        for p in self.players:

            if p.stamina - (p.age * 2) < 0:

                p.stamina = 0

            else:
                p.stamina -= (p.age * 2)

        for p in self.players:

            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):

        info = []

        for player in self.players:

            info.append(player.__str__())

        for supply in self.supplies:

            info.append(supply.details())

        return '\n'.join(info)
