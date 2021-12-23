from game.CONST import *
from .GridId import GridId


class Player:
    def __init__(self, id, color):
        self.id = id
        self.name = PlayerNames[self.id]
        self.color = color
        self.home_position = HomePosition[id]
        self.position = GridId(0)
        self.money = InitialMoney

    def step(self, steps):
        self.position = self.position + steps

    def get_grid(self):
        return self.game.grids[self.position]
