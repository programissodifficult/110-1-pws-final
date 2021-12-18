from .Grid import Grid
from .StandPrice import stand_prices


class FoodStand(Grid):
    def __init__(self, id, name, price_level):
        super().__init__(id)
        self.name = name
        self.price_level = price_level
        self.owner = None

    @property
    def price(self):
        return stand_prices[self.price_level]

    def trigger(self):
        # TODO
        pass
