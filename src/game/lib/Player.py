from view.CONST import BoardGridWidth
from ..CONST import *
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
        self.idle_action = 0
        self.idle_kitchen = 0

    @property
    def own_stands(self):
        return [grid for grid in self.game.grids if (grid.type == 'FoodStand' and grid.owner_id == self.id)]

    def alter_money(self, amount):
        self.money += amount
        self.money = max(self.money, 0)

    def distance_to(self, id):
        MaxDistance = BoardGridWidth * 2
        return MaxDistance - abs(MaxDistance - abs(self.position.id - id))

    def step(self, steps):
        self.position = self.position + steps

    def get_grid(self):
        return self.game.grids[self.position]
