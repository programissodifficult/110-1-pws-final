from game.CONST import *
from .GridId import GridId

player_id = 0

class Player:
    def __init__(self, player_id, char_id):
        self.id = player_id
        self.name = CharacterNames[char_id]
        self.color = CharacterColors[char_id]
        self.home_position = GridId(HomePosition[char_id])
        self.position = GridId(0)
        self.money = InitialMoney
        self.idle_round = 0

    def step(self, steps):
        self.position = self.position + steps

    def get_grid(self):
        return self.game.grids[self.position]
