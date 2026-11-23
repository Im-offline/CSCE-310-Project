from classes import Player
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

class Game:
    def __init__(self):
        self.players: list[Player] = []

    def queue_player(self, player: Player):
        self.players.append(player)
        if player.matches_played <= 10:
            print('greedy')
            self.matchmake_greedy(player.match_making_region)
        else:
            print('divide and conquer')
            self.matchmake_DC(player.match_making_region, player.mmr)

    def matchmake_greedy(self, match_making_region):
        #grab the first 9 players regardless of mmr (kruskals algo)
        df = pd.read_csv(ROOT/"data/" / f"{match_making_region}.csv")
        #print(df)
        self.players.append()
        #add players from df into a queue, then just add the original player plus 9
        #others to the player list
        

    def matchmake_DC(self, match_making_region, mmr):
        #look through the file to find 9 players who have an mmr of +- 100 (merge or quick sort)
        #mmr of the matchmaking player
        df = pd.read_csv(ROOT/"data/" / f"{match_making_region}.csv")
        
        #add players from df into a queue, then search for 9 players who are within
        #100 mmr of the matchmaking player and add them all to the players list
        
        
        
    
    def play(self):
        pass   