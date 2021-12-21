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
        self.price_level = price_level
        self.owner = None

    @property
    def price(self):
        return stand_prices[self.price_level]

    def trigger(self):
        # TODO
        pass


class EventGrid(Grid):
    def __init__(self, id):
        super().__init__(id, 'Event')

    def trigger(self):
        # TODO
        pass


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
