from game.CONST import *

class Player:
    def __init__(self, id, color):
        self.id = id
        self.name = PlayerNames[self.id]
        self.color = color
        self.home_position = HomePosition[id]
        self.position = 0
        self.money = InitialMoney

    def step(self, steps):
        self.position = (self.position + steps) % MapSize