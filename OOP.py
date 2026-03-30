class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition


class NFLTeam:
    def __init__(self, teamName, players):
        self.teamName = teamName
        self.players = players

    def printTeam(self):
        print("Team Name:", self.teamName)
        print("Players:")
        for player in self.players:
            print(player.playerName, "-", player.playerPosition)


# Create 4 players
player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

# Add players to a list
playerList = [player1, player2, player3, player4]

# Create team
team = NFLTeam("Smashmouth Football", playerList)

# Output
team.printTeam()