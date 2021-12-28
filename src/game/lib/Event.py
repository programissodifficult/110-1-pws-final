import random
from util.Dialog import confirm

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.game import Game


class Event(object):
    game = None  # type: Game

    def __init__(self, event_description, effect_description, *args, **kwargs):
        self.event_description = event_description
        self.effect_description = effect_description
        self.init(*args, **kwargs)

    def init(self):
        pass

    def trigger(self, triggerer):
        raise NotImplementedError


class StopActionEvent(Event):
    """觸發玩家停止行動一回合

    For card id: 1
    """

    def trigger(self, triggerer):
        triggerer.idle_action += 1


class AddTableEvent(Event):
    """觸發玩家隨機在自己的攤位免費添加一張桌子

    For card id: 2
    """

    def trigger(self, triggerer):
        available_stands = [grid for grid in triggerer.own_stands if grid.level < 3]
        if len(available_stands):
            target_grid = random.choice(available_stands)
            target_grid.upgrade()
        else:
            confirm("", "你沒有任何可以升級的攤位QQ")


class RemoveTableEvent(Event):
    """觸發玩家隨機拆除一張自己的桌子

    For card id: 21
    """

    def trigger(self, triggerer):
        self.game.random_remove_table(triggerer.id)


class AlterMoneyEvent(Event):
    """觸發玩家獲得/失去一定數量的錢

    For card id: 8, 12, 13, 14, 22, 23, 25
    """

    def init(self, amount):
        self.amount = amount

    def trigger(self, triggerer):
        triggerer.alter_money(self.amount)


class AlterMoneyNearestEvent(Event):
    """離某攤位最近的玩家獲得/失去一定數量的錢

    For card id: 5, 6, 7
    """

    def init(self, stand_id, amount):
        self.stand_id = stand_id
        self.amount = amount

    def trigger(self, triggerer):
        nearest_player = min(self.game.players, key=lambda p: p.distance_to(self.stand_id))
        nearest_player.alter_money(self.amount)


class AlterMoneyIfOwnEvent(Event):
    """觸發玩家根據是否擁有攤位獲得/失去一定數量的錢

    For card id: 11
    """

    def init(self, stand_id, amount_if_own, amount_otherwise):
        self.stand_id = stand_id
        self.amount_if_own = amount_if_own
        self.amount_otherwise = amount_otherwise

    def trigger(self, triggerer):
        if self.stand_id in [stand.id for stand in triggerer.own_stands]:
            triggerer.alter_money(self.amount_if_own)
        else:
            triggerer.alter_money(self.amount_otherwise)


class EveryOneAlterMoneyIfOwnEvent(Event):
    """擁有某些攤位的玩家獲得/失去一定數量的錢

    For card id: 3, 15
    """

    def init(self, stand_ids, amount):
        self.stand_ids = stand_ids
        self.amount = amount

    def trigger(self, triggerer):
        for player in self.game.players:
            if any(stand.id in self.stand_ids for stand in player.own_stands):
                player.alter_money(-self.amount)


class RandomAlterMoneyEvent(Event):
    """觸發玩家隨機獲得/失去一定數量的錢

    For card id: 10
    """

    def init(self, amount):
        self.amount = amount

    def trigger(self, triggerer):
        success = random.choice([True, False])
        if success:
            triggerer.alter_money(self.amount)
        else:
            triggerer.alter_money(-self.amount)


class EveryoneAlterMoneyEvent(Event):
    """所有玩家獲得/失去一定數量的錢

    For card id: 19
    """

    def init(self, amount):
        self.amount = amount

    def trigger(self, triggerer):
        for player in self.game.players:
            player.alter_money(self.amount)


class TransferMoneyToNextEvent(Event):
    """觸發玩家給下一位玩家一定量的錢

    For card id: 9
    """

    def init(self, amount):
        self.amount = amount

    def trigger(self, triggerer):
        next_id = triggerer.next_player().id
        self.game.player_transfer_money(next_id, triggerer.id, self.amount)


class EveryoneTransferMoneyEvent(Event):
    """所有玩家給玩家 A 一定量的錢

    For card id: 24
    """

    def init(self, amount):
        self.amount = amount

    def trigger(self, triggerer):
        for player in self.game.players:
            if player != triggerer:
                self.game.player_transfer_money(triggerer.id, player.id, self.amount)


class IdleKitchenEvent(Event):
    """觸發玩家下次經過中央廚房不得領錢、研發技術

    For card id: 4
    """

    def trigger(self, triggerer):
        triggerer.idle_kitchen += 1


class RaceGainOrRemoveTableEvent(Event):
    """觸發玩家和上一位玩家比，擁有較多攤位者拆除一張桌子，較少攤位者獲利

    For card id: 16
    """

    def init(self, amount):
        self.amount = amount

    def trigger(self, triggerer):
        last_player = triggerer.last_player()
        last_player_stands = last_player.own_stands
        triggerer_stands = triggerer.own_stands
        if len(last_player_stands) > len(triggerer_stands):
            self.game.random_remove_table(last_player.id)
            triggerer.alter_money(self.amount)
        elif len(last_player_stands) < len(triggerer_stands):
            self.game.random_remove_table(triggerer.id)
            last_player.alter_money(self.amount)
        else:
            last_player.alter_money(self.amount // 2)
            triggerer.alter_money(self.amount // 2)


class FreeTableEvent(Event):
    """觸發玩家下次添加桌子免費

    For card id: 17
    """

    def trigger(self, triggerer):
        triggerer.free_table += 1


class RandomBuyStandEvent(Event):
    """觸發玩家可選擇是否購買一個隨機選中的無人攤位

    For card id: 18
    """

    def trigger(self, triggerer):
        unclaimed_stands = [grid for grid in self.game.grids if (grid.type == 'FoodStand' and grid.owner_id == None)]
        stand = random.choice(unclaimed_stands)
        self.game.ask_for_buy_stand(triggerer.id, stand.id)


class RandomBuyOthersStandEvent(Event):
    """觸發玩家可選擇是否購買一個隨機選中的有人攤位

    For card id: 20
    """

    def trigger(self, triggerer):
        others_stands = [grid for grid in self.game.grids if (
            grid.type == 'FoodStand' and
            not grid.owner_id in [None, triggerer.id] and
            grid.level == 0)
        ]
        if len(others_stands) > 0:
            stand = random.choice(others_stands)
            self.game.ask_for_buy_stand(triggerer.id, stand.id)
        else:
            confirm('沒有可以購買的攤位QQ')
