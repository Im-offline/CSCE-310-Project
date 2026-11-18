from classes import Player
from classes import Game

game = Game()

p1 = Player("me")
p2 = Player('you', 'NA-E')
p3 = Player('who', 'EU', 10, 5, 552)
p4 = Player('bad name', 'Asia')

p1.print_stats()
p2.print_stats()
p3.print_stats()
p4.print_stats()

p4.update_name('good name')
p4.update_region('NA-W')
p4.update_matches_played()
p4.update_rank(1)
p4.update_mmr(100)

p4.print_stats()

p4.update_mmr(-5)
p4.update_rank(0)

p4.print_stats()

p2.ready_up(game)
p3.ready_up(game)
#asdf
# hello i am here
#works
