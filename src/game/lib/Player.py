from util.Dialog import confirm, yesno
from ..CONST import *
from .GridId import GridId
from .Character import characters

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.game import Game


class Player:
    game = None  # type: Game

    def __init__(self, player_id, char_id):
        character = characters[char_id]
        self.character_id = char_id
        self.name = character.name
        self.color = character.color
        self.color_light = character.color_light

        self.id = player_id
        self.home_position = GridId(HomePosition[char_id])
        self.position = GridId(HomePosition[char_id])
        self.money = InitialMoney
        self.tech_invented = []

        # temp effect
        self.idle_action = 0
        self.idle_kitchen = 0
        self.free_table = 0

        # Tech ability
        self.invent_discount = 0
        self.double_table = False
        self.reverse_visit_kitchen = False
        self.extra_income = 0
        self.extra_stand_fee = 0
        self.stand_fee_discount = 0
        self.same_spot_fee = 0
        self.build_discount = 0
        self.event_bonus = 0
        self.redraw_chance = []

        character.init_ability(self)

    def init(self):
        self.game.players_by_char[self.character_id] = self

    @property
    def own_stands(self):
        return [grid for grid in self.game.grids if (grid.type == 'FoodStand' and grid.owner_id == self.id)]

    @property
    def character(self):
        return characters[self.character_id]

    def alter_money(self, amount):
        self.money += amount
        self.money = max(self.money, 0)

    def distance_to(self, id):
        MaxDistance = MapSize // 2
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
        temp_effect = ''
        if self.idle_action:
            temp_effect += f'  - 暫停行動 {self.idle_action} 回合\n'
        if self.idle_kitchen:
            temp_effect += f'  - 經過中央廚房不得領錢、研發科技 {self.idle_kitchen} 回合\n'
        if self.free_table:
            temp_effect += f'  - 免費建造桌子 {self.free_table} 次'

        s = f"""玩家：{self.name}

角色能力：{self.character.ability_description}
現金：{self.money}
攤位：{', '.join(stand_names)}
技術：
{tech_info if tech_info else '(無)'}
暫時效果：
{temp_effect if temp_effect else '(無)'}
        """
        confirm('玩家資訊', s)
