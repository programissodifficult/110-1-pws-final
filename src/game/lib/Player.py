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
        self.character_id = char_id
        self.name = CharacterNames[char_id]
        self.color = CharacterColors[char_id]
        self.color_light = CharacterColorsLight[char_id]
        self.home_position = GridId(HomePosition[char_id])
        self.position = GridId(HomePosition[char_id])
        self.money = InitialMoney
        self.idle_action = 0
        self.idle_kitchen = 0
        self.free_table = 0
        self.tech_invented = []

        # character ability
        self.invent_discount = 0

        # Tech ability
        self.double_table = False
        self.reverse_visit_kitchen = False
        self.extra_income = 0
        self.extra_stand_fee = 0
        self.stand_fee_discount = 0
        self.same_spot_fee = 0
        self.build_discount = 0

    def init(self):
        self.game.players_by_char[self.character_id] = self

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

    def get_score_total(self):
        return self.get_score()["total"]

    def get_score(self):
        scores = {
            "money": self.money // 1000,
            "stand": len(self.own_stands),
            "table": sum([stand.level for stand in self.own_stands]),
            "tech": sum([tech.score for tech in self.tech_invented]),
        }
        scores["total"] = sum(scores.values())
        return scores

    def show_info(self):
        stands = self.own_stands
        stand_names = [stand.name for stand in self.own_stands] if len(stands) else ['無']
        tech_info = ''.join([f'  - [{tech.score}分] {tech.ability_description}\n' for tech in self.tech_invented])
        s = f"""玩家：{self.name}

現金：{self.money}
攤位：{', '.join(stand_names)}
技術：
{tech_info}
        """
        confirm('玩家資訊', s)
