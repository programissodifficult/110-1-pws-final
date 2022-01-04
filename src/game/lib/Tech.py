import random
from util.Dialog import confirm

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.game import Game


class Tech(object):
    game = None  # type: Game

    def __init__(self, score, tech_description, ability_description, *args, **kwargs):
        self.score = score
        self.tech_description = tech_description
        self.ability_description = ability_description
        self.init(*args, **kwargs)

    def init(self):
        pass

    def trigger(self, inventor):
        raise NotImplementedError


class DoubleTableTech(Tech):
    """一次添加兩張桌子

    For card id: 1
    """

    def trigger(self, inventor):
        inventor.double_table = True


class SameSpotFeeTech(Tech):
    """站在同一格的玩家要付錢

    For card id: 3
    """

    def init(self, amount):
        self.amount = amount

    def trigger(self, inventor):
        inventor.same_spot_fee += self.amount


class ExtraIncomeTech(Tech):
    """額外廚房收入

    For card id: 4
    """

    def init(self, amount):
        self.amount = amount

    def trigger(self, inventor):
        inventor.extra_income += self.amount

class ReverseVisitKitchenTech(Tech):
    """停留他人廚房可以反過來收錢

    For card id: 6
    """
    def trigger(self, inventor):
        inventor.reverse_visit_kitchen = True

class ExtraStandFeeTech(Tech):
    """攤位多收錢

    For card id: 9
    """

    def init(self, amount):
        self.amount = amount

    def trigger(self, inventor):
        inventor.extra_stand_fee += self.amount


class StandFeeDiscountTech(Tech):
    """攤位少收錢

    For card id: 11
    """

    def init(self, amount):
        self.amount = amount

    def trigger(self, inventor):
        inventor.stand_fee_discount += self.amount


class TableDiscountTech(Tech):
    """桌子少付錢

    For card id: 12
    """

    def init(self, amount):
        self.amount = amount

    def trigger(self, inventor):
        inventor.build_discount += self.amount
