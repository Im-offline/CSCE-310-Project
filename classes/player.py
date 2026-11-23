class Player:
    def __init__(self, username: str, match_making_region: str = 'NA-W', matches_played: int = 0, rank: int = 0, mmr: int = 0):
        self.username = username
        self.match_making_region = match_making_region
        self.matches_played = matches_played
        self.rank = rank
        self.mmr = mmr

    def __repr__(self):
        return (
            f"Player(username={self.username!r}, "
            f"region={self.match_making_region!r}, "
            f"matches={self.matches_played}, "
            f"rank={self.rank}, "
            f"mmr={self.mmr})"
        )

    def print_stats(self):
        print("username = " + self.username)
        print("matchmaking region = " + self.match_making_region)
        print("matches played = " + str(self.matches_played))
        print("rank = " + str(self.rank))
        print("mmr = " + str(self.mmr))
        print()

    def update_name(self, new_username):
        self.username = new_username

    def update_region(self, new_region):
        self.match_making_region = new_region

    def update_matches_played(self):
        self.matches_played += 1

    def update_rank(self, new_rank):
        self.rank = new_rank

    def update_mmr(self, mmr):
        self.mmr += mmr

    def ready_up(self, game):
        game.queue_player(self)