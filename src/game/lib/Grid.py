import random
from util.Dialog import yesno, confirm
from .Character import characters
from .GridId import GridId
from .StandPrice import stand_prices

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.game import Game


class Grid():
    game = None  # type: Game

    def __init__(self, id, type):
        self.id = GridId(id)
        self.type = type

    def init(self):
        pass

    def trigger(self, triggerer):
        pass


class FoodStand(Grid):
    def __init__(self, id, name, price_level, default_char_id=None):
        super().__init__(id, 'FoodStand')
        self.name = name
        self.level = 0
        self.price_level = price_level
        self.owner_id = None
        self.default_char_id = default_char_id

    def init(self):
        if self.default_char_id != None:
            default_owner = self.game.players_by_char[self.default_char_id]
            if default_owner != None:
                self.owner_id = default_owner.id

    @property
    def prices(self):
        return stand_prices[self.price_level]

    @property
    def owner(self):
        if self.owner_id == None:
            return None
        else:
            return self.game.players[self.owner_id]

    def upgrade(self):
        self.level += 1

    def trigger(self, triggerer):
        if self.owner != None:
            if self.owner != triggerer:
                # 已被別人購買的攤位，觸發獲利事件
                self.game.profit_stand(self.id, triggerer.id)
                profit = self.game.get_stand_profit(self.id, triggerer.id)
                confirm('台灣發大財!', f'{triggerer.name} 光顧 {self.owner.name} 的 {self.name}，帶來 {profit} 元的收入!')
            else:
                # 自己的攤位，可添加桌子
                self.game.ask_for_build_table(triggerer.id, self.id)
        else:
            # 無人攤位，觸發購買事件
            self.game.ask_for_buy_stand(triggerer.id, self.id)

    def show_info(self):
        owner_name = self.owner.name if self.owner_id else '無'

        s = f"""攤位：{self.name}

擁有者：{owner_name}
桌子數量：{self.level}
購買價格：{self.prices.buy}
升級價格：{self.prices.build}
        """
        confirm('攤位格', s)


class EventGrid(Grid):
    def __init__(self, id):
        super().__init__(id, 'Event')

    def trigger(self, triggerer):
        card = self.game.draw_event_card()
        confirm("經營卡", f"{card.event_description}：\n{card.effect_description}")
        for chance in triggerer.redraw_chance:
            result = yesno('重抽經營卡', f'[{chance}] 是否重抽經營卡?')
            if result:
                card = self.game.draw_event_card()
                confirm("經營卡", f"{card.event_description}：\n{card.effect_description}")
            else:
                break

        card.trigger(triggerer)

        if triggerer.event_bonus:
            confirm('主廚能力', f'[主廚能力] 每次抽經營卡時可以獲得 {triggerer.event_bonus} 元')
            triggerer.alter_money(triggerer.event_bonus)


descriptions = {
    "fee": '向所有玩家收取 200 元',
    "switch": '隨機和一位玩家交換位置',
    "rest": '隨機一位玩家休息一回合',
    "buy": '可以隨機購買一個攤位',
}


class EffectGrid(Grid):
    def __init__(self, id, effect_type, name):
        super().__init__(id, 'Effect')
        self.effect_type = effect_type
        self.name = name
        self.effect_handler = {
            "fee": self.trigger_fee,
            "switch": self.trigger_switch,
            "rest": self.trigger_rest,
            "buy": self.trigger_buy,
        }

    @property
    def effect_description(self):
        return descriptions[self.effect_type]

    def trigger(self, triggerer):
        self.effect_handler[self.effect_type](triggerer)

    def confirm_effect(self, additional_msg):
        s = self.effect_description
        if additional_msg:
            s += f'：\n{additional_msg}'
        confirm('效果格', f'[{self.name}] {s}')

    def trigger_fee(self, triggerer):
        for p in self.game.players:
            if p != triggerer:
                self.game.player_transfer_money(triggerer.id, p.id, 200)
        self.confirm_effect()

    def trigger_switch(self, triggerer):
        other = random.choice([p for p in self.game.players if p != triggerer])
        self.game.switch_position(other.id, triggerer.id)
        self.confirm_effect(f'{triggerer.name} 和 {other.name} 交換位置了!')

    def trigger_rest(self, triggerer):
        other = random.choice([p for p in self.game.players if p != triggerer])
        other.idle_action += 1
        self.confirm_effect(f'{other.name} 休息一回合')

    def trigger_buy(self, triggerer):
        self.confirm_effect()
        unclaimed_stands = [grid for grid in self.game.grids if (grid.type == 'FoodStand' and grid.owner_id == None)]
        if len(unclaimed_stands) > 0:
            stand = random.choice(unclaimed_stands)
            self.game.ask_for_buy_stand(triggerer.id, stand.id)
        else:
            self.confirm_effect(f'已經沒有無人的攤位了')


class MainKitchen(Grid):
    def __init__(self, id, character_id):
        super().__init__(id, 'MainKitchen')
        self.character_id = character_id

    @property
    def owner(self):
        return self.game.players_by_char[self.character_id]

    def trigger(self, triggerer):
        if self.owner == None:
            confirm('參觀中央廚房', f"這裡是{characters[self.character_id].name}的中央廚房，不過好像沒有人在")
            return

        if triggerer.id != self.owner.id:
            if triggerer.reverse_visit_kitchen:
                confirm("參觀中央廚房", f"{triggerer.name} 拜訪 {self.owner.name} 的中央廚房幫助宣傳，{self.owner.name} 支付宣傳費 200 元(技術卡效果)")
                self.game.player_transfer_money(triggerer.id, self.owner.id, 200)
            else:
                confirm("參觀中央廚房", f"{triggerer.name} 拜訪 {self.owner.name} 的中央廚房，支付參觀費 200 元")
                self.game.player_transfer_money(self.owner.id, triggerer.id, 200)
