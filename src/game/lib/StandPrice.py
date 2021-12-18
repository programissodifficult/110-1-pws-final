class StandPrice:
    def __init__(self, buy_price, build_price, fees):
        self.buy = buy_price
        self.build = build_price
        self.fees = fees

stand_prices = [
    StandPrice(500, 600, [600, 900, 1200, 1800]),
    StandPrice(700, 600, [700, 1000, 1400, 2000]),
    StandPrice(900, 700, [800, 1100, 1500, 2200]),
    StandPrice(1100, 700, [900, 1200, 1600, 2400])
]