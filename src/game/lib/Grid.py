from util.Dialog import yesno, confirm
from .GridId import GridId
from .StandPrice import stand_prices

class Grid():
    def __init__(self, id, type):
        self.id = GridId(id)
        self.type = type

    def trigger(self):
        pass


class FoodStand(Grid):
    def __init__(self, id, name, price_level):
        super().__init__(id, 'FoodStand')
        self.name = name
        self.level = 0
        self.price_level = price_level
        self.owner_id = None

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

    def trigger(self):
        if self.owner != None:
            # 已有人購買的攤位，觸發獲利事件
            self.game.profit_stand(self.id)
            confirm('台灣發大財!', f'{self.game.current_player.name} 光顧 {self.owner.name} 的 {self.name}，帶來 {self.prices.profit[self.level]} 元的收入!')
        else:
            # 無人攤位，觸發購買事件
            if self.game.afford_stand(self.game.current_player.id, self.id):
                result = yesno("購買攤位", f"是否以 {self.prices.buy} 元購買{self.name}")
                if result:
                    self.game.buy_stand(self.game.current_player.id, self.id)
            else:
                confirm("購買攤位", f"你的錢好像不太夠，無法購買 {self.prices.buy} 元的{self.name}")


class EventGrid(Grid):
    def __init__(self, id):
        super().__init__(id, 'Event')

    def trigger(self):
        card = self.game.draw_event_card()
        confirm("經營卡", f"{card.event_description}：\n{card.effect_description}")
        card.trigger(self.game.current_player)


class EffectGrid(Grid):
    def __init__(self, id, effect_type):
        super().__init__(id, 'Effect')
        self.effect_type = effect_type

    def trigger(self):
        # TODO
        pass


class MainKitchen(Grid):
    def __init__(self, id, player_id):
        super().__init__(id, 'MainKitchen')
        self.player_id = player_id

    def trigger(self):
        # TODO
        pass
