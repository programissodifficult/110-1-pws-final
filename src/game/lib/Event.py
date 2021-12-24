import random
from operator import attrgetter
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


class StopActionEvent(Event):
    def trigger(self, triggerer):
        triggerer.idle_action += 1


class AddTableEvent(Event):
    def trigger(self, triggerer):
        available_stands = [grid for grid in triggerer.own_stands if grid.level < 3]
        if len(available_stands):
            target_grid = random.choice()
            target_grid.upgrade()
        else:
            confirm("", "你沒有任何可以升級的攤位QQ")


class RemoveTableEvent(Event):
    def trigger(self, triggerer):
        pass


class GainMoneyEvent(Event):
    def trigger(self, triggerer):
        pass


class GainMoneyNearestEvent(Event):
    def init(self, stand_id, amount):
        self.stand_id = stand_id
        self.amount = amount

    def trigger(self, triggerer):
        nearest_player = min(self.game.players, key=lambda p: p.distance_to(self.stand_id))
        nearest_player.alter_money(self.amount)


class EveryOneLoseMoneyIfOwnEvent(Event):
    def init(self, stand_ids, amount):
        self.stand_ids = stand_ids
        self.amount = amount

    def trigger(self, triggerer):
        for player in self.game.players:
            if any(stand.id in self.stand_ids for stand in player.own_stands):
                player.alter_money(-self.amount)


class EveryoneGainMoneyEvent(Event):
    def trigger(self, triggerer):
        pass


class EveryoneLoseMoneyEvent(Event):
    def trigger(self, triggerer):
        pass


class GainLoseMoneyEvent(Event):
    def trigger(self, triggerer):
        pass


class TransferMoneyEvent(Event):
    def trigger(self, triggerer):
        pass


class IdleKitchenEvent(Event):
    def trigger(self, triggerer):
        triggerer.idle_kitchen += 1


class RaceGainOrRemoveTableEvent(Event):
    def trigger(self, triggerer):
        pass


class FreeTableEvent(Event):
    def trigger(self, triggerer):
        pass


class RandomBuyStandEvent(Event):
    def trigger(self, triggerer):
        pass
