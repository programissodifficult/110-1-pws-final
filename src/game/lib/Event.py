import random
from util.Dialog import confirm


class Event:
    def __init__(self, event_description, effect_description, *args, **kwargs):
        self.event_description = event_description
        self.effect_description = effect_description
        self.init(*args, **kwargs)

    def init(self):
        pass

    def trigger(self, triggerer):
        raise NotImplementedError

# 觸發玩家停止行動一回合
# id: 1
class StopActionEvent(Event):
    def trigger(self, triggerer):
        triggerer.idle_action += 1

# 觸發玩家隨機在自己的攤位免費添加一張桌子
# id: 2
class AddTableEvent(Event):
    def trigger(self, triggerer):
        available_stands = [grid for grid in triggerer.own_stands if grid.level < 3]
        if len(available_stands):
            target_grid = random.choice(available_stands)
            target_grid.upgrade()
        else:
            confirm("", "你沒有任何可以升級的攤位QQ")

# 觸發玩家隨機拆除一張自己的桌子
# id: 21
class RemoveTableEvent(Event):
    def trigger(self, triggerer):
        pass

# 觸發玩家獲得/失去一定數量的錢
# id: 8, 12, 13, 14, 22, 23, 25
class AlterMoneyEvent(Event):
    def init(self, amount):
        self.amount = amount

    def trigger(self, triggerer):
        triggerer.alter_money(self.amount)

# 離某攤位最近的玩家獲得/失去一定數量的錢
# id: 5, 6, 7
class AlterMoneyNearestEvent(Event):
    def init(self, stand_id, amount):
        self.stand_id = stand_id
        self.amount = amount

    def trigger(self, triggerer):
        nearest_player = min(self.game.players, key=lambda p: p.distance_to(self.stand_id))
        nearest_player.alter_money(self.amount)

# 觸發玩家根據是否擁有攤位獲得/失去一定數量的錢
# id: 11
class EveryOneAlterMoneyIfOwnEvent(Event):
    def init(self, stand_id, amount_if_own, amount_otherwise):
        self.stand_id = stand_id
        self.amount_if_own = amount_if_own
        self.amount_otherwise = amount_otherwise

    def trigger(self, triggerer):
        if self.stand_id in [stand.id for stand in triggerer.own_stands]:
            triggerer.alter_money(self.amount_if_own)
        else:
            triggerer.alter_money(self.amount_otherwise)

# 擁有某些攤位的玩家獲得/失去一定數量的錢
# id: 3, 15
class EveryOneAlterMoneyIfOwnEvent(Event):
    def init(self, stand_ids, amount):
        self.stand_ids = stand_ids
        self.amount = amount

    def trigger(self, triggerer):
        for player in self.game.players:
            if any(stand.id in self.stand_ids for stand in player.own_stands):
                player.alter_money(-self.amount)

# 觸發玩家隨機獲得/失去一定數量的錢
# id: 10
class RandomAlterMoneyEvent(Event):
    def trigger(self, triggerer):
        pass

# 所有玩家獲得/失去一定數量的錢
# id: 19
class EveryoneAlterMoneyEvent(Event):
    def init(self, amount):
        self.amount = amount
    def trigger(self, triggerer):
        for player in self.game.players:
            player.alter_monoey(self.amount)

# 玩家 A 給玩家 B 一定量的錢
# id: 9
class TransferMoneyEvent(Event):
    def trigger(self, triggerer):
        pass

# 所有玩家給玩家 A 一定量的錢
# id: 24
class EveryoneTransferMoneyEvent(Event):
    def trigger(self, triggerer):
        pass

# 觸發玩家下次經過中央廚房不得領錢、研發技術
# id: 4
class IdleKitchenEvent(Event):
    def trigger(self, triggerer):
        triggerer.idle_kitchen += 1

# 所有玩家擲骰，大於七點者獲利 700 ，否則隨機拆除一張桌子
# id: 16
class RaceGainOrRemoveTableEvent(Event):
    def trigger(self, triggerer):
        pass

# 觸發玩家下次添加桌子免費
# id: 17
class FreeTableEvent(Event):
    def trigger(self, triggerer):
        pass

# 觸發玩家可選擇是否購買一個隨機選中的無人攤位
# id: 18
class RandomBuyStandEvent(Event):
    def trigger(self, triggerer):
        pass


# 觸發玩家可選擇是否購買一個隨機選中的有人攤位
# id: 20
class RandomBuyOthersStandEvent(Event):
    def trigger(self, triggerer):
        pass