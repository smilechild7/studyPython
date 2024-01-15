kse = {
    "name" : "kse",
    "XP" : 1000,
    "team" : "Learning Crew"
}

def introduce_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hi my name is {name} and I play for {team} ")

introduce_player(kse)