class Player:
    def __init__(self,name,team):
        self.name = name
        self.team = team
        self.xp = 1500

    def introduce(self):
        print(f"Hi! I'm {self.name} and I play for {self.team}!")

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.players = []
    
    def show_players(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name):
        new_player = Player(name, self.name)
        self.players.append(new_player)

    def delete_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)

    def show_xp_sum(self):
        sum=0
        for player in self.players:
            sum+= player.xp
        print(f"{self.name} have {sum} xp!")

team_X = Team("team X")
team_X.add_player("kse")

team_Y = Team("team Y")
team_Y.add_player("jjg")
team_Y.add_player("gjh")
team_Y.add_player("csm")
team_Y.delete_player("csm")

team_Y.show_players()

team_Y.show_xp_sum()