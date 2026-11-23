#in order to run this fule from main, change 'from player' to 'from classes'
from player import Player
from pathlib import Path
import pandas as pd
from collections import deque
import random

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
            print('BFS')
            self.matchmake_BFS(player.match_making_region, player.mmr)


    def matchmake_greedy(self, match_making_region):
        #grab 9 random players regardless of mmr
        df = pd.read_csv(ROOT/"data/" / f"{match_making_region}.csv")
        df.columns = df.columns.str.strip().str.strip('"\'')

        available_players = [Player(**row) for row in df.to_dict(orient = 'records')]

        for _ in range(9):
            self.players.append(available_players.pop(random.randrange(len(available_players))))

        self.play()
        

        
    def matchmake_BFS(self, match_making_region, mmr):
        #look through the file to find 9 players who have an mmr of +- 100 (merge or quick sort)
        #mmr of the matchmaking player
        df = pd.read_csv(ROOT/"data/" / f"{match_making_region}.csv")
        df.columns = df.columns.str.strip().str.strip('"\'')        

        available_players = [Player(**row) for row in df.to_dict(orient = 'records')]
        
        matchmakingQueue= deque()
        matchmakingQueue.extend(available_players)
        playerOne=self.players[0]
        
        floorMMR=(playerOne.mmr-100)
        ceilingMMR=(playerOne.mmr+100)
        
        for p in matchmakingQueue:
            if (p.mmr>=floorMMR) and (p.mmr<=ceilingMMR):
                self.players.append(p)
                if len(self.players)==10:
                    break

        self.play()
            
    def play(self):
        pass  

    def print_players(self):
        print(self.players)
