from classes import Player
from pathlib import Path
import pandas as pd
#df=pandas.read_csv("dataframe.csv")
ROOT = Path(__file__).resolve().parent.parent

class Game:
    def __init__(self):
        self.players: list[Player] = []

    def queue_player(self, player: Player):
        if player.matches_played <= 10:
            self.matchmake_greedy(player.match_making_region)
            print('greedy')
        else:
            self.matchmake_DC(player.match_making_region)
            print('divide and conquer')

    def matchmake_greedy(self, match_making_region):
        #grab the first 11 players regardless of mmr (kruskals algo)
        df = pd.read_csv(ROOT/"data/" / f"{match_making_region}.csv")
        print(df)
        

    def matchmake_DC(self, match_making_region):
        #look through the file to find 11 players who have an mmr of +- 100 (merge or quick sort)
        #mmr of the matchmaking player
        pass
    
    def play(self):
        pass

    