from util.Dialog import confirm, yesno
from ..CONST import *
from .GridId import GridId

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.game import Game

player_id = 0


class Player:
    game = None  # type: Game

    def __init__(self, player_id, char_id):
        self.id = player_id
        self.name = CharacterNames[char_id]
        self.color = CharacterColors[char_id]
        self.home_position = GridId(HomePosition[char_id])
        self.position = GridId(HomePosition[char_id])
        self.money = InitialMoney
        self.idle_action = 0
        self.idle_kitchen = 0
        self.free_table = 0
        self.tech_invented = 0

        # character ability
        self.invent_discount = 0

        # Tech ability
        self.double_table = False
        self.extra_income = 0
        self.extra_stand_fee = 0
        self.stand_fee_discount = 0
        self.same_spot_fee = 0
        self.build_discount = 0

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

    def get_tech_invent_price(self):
        return TechInventPrice - self.invent_discount

    def get_income(self):
        return BaseHomeIncome + self.extra_income

    def get_grid(self):
        return self.game.grids[self.position]

    def last_player(self):
        return self.game.players[(self.id - 1)]

    def next_player(self):
        return self.game.players[(self.id + 1) % len(self.game.players)]
