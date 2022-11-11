class Player:

    skills = {}
    guild = "Unaffiliated"

    def __init__(self, name, hp, mp):

        self.name = name
        self.hp = hp
        self.mp = mp

    def add_skill(self, skill_name, mana_cost):

        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):

        result = f"Name: {self.name}\n"
        result += f"Guild: {self.guild}\n"
        result += f"HP: {self.hp}\n"
        result += f"MP: {self.mp}\n"

        string = ', '.join([f'==={key} - {value}' for key, value in self.skills.items()])
        result += string + '\n'

        return result