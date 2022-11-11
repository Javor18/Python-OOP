class Guild:

    def __init__(self, guild_name):

        self.guild_name = guild_name
        self.players = []

    def assign_player(self, player):

        if self.guild_name == player.guild:
            return f"Player {player.name} is already in the guild."

        if player.guild != player.guild:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.guild_name
        return f"Welcome player {player.name} to the guild {self.guild_name}"

    def kick_player(self, player_name):

        for player in self.players:

            if player.name == player_name:

                self.players.remove(player_name)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.guild_name}\n"

        for player in self.players:

            result += player.player_info() + "\n"

        return result.strip()