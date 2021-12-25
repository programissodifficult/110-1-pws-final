import random

from .lib.GridImpl import make_grids
from .lib.EventImpl import make_event_cards
from .lib.Grid import *
from .lib.Player import Player


class Game:
    def __init__(self):
        self.turn = 0

    # ############################################################
    #  getter
    # ############################################################

    @property
    def current_player(self):
        return self.players[self.turn]

    # ############################################################
    #  init
    # ############################################################

    def init(self, player_amount):
        self.init_grids()
        self.init_player(player_amount)
        self.init_events()

    def init_grids(self):
        self.grids = make_grids()

        for grid in self.grids:
            grid.game = self

    def init_player(self, player_amount):
        characters = [0, 1, 2, 3]
        random.shuffle(characters)
        characters = characters[:player_amount]
        self.players = [Player(index, char_id) for (index, char_id) in enumerate(characters)]

        for player in self.players:
            player.game = self

    def init_events(self):
        self.event_cards = make_event_cards()

        for event in self.event_cards:
            event.game = self

        self.reshuffle_events()


    def reshuffle_events(self):
        self.event_pointer = 0
        random.shuffle(self.event_cards)


    # ############################################################
    #  game play helper
    # ############################################################

    def draw_event_card(self):
        card = self.event_cards[self.event_pointer]
        self.event_pointer += 1
        if self.event_pointer >= len(self.event_cards):
            self.reshuffle_events()
        return card

    def player_transfer_money(self, receiver_id, giver_id, amount):
        receiver = self.players[receiver_id]
        giver = self.players[giver_id]
        amount = min(amount, giver.money)
        receiver.alter_money(amount)
        giver.alter_money(-amount)

    def profit_stand(self, grid_id):
        stand = self.grids[grid_id]
        owner = stand.owner
        if owner == None:
            raise Exception(f'Cannot profit stand {stand.name} with no owner')
        # TODO: add discount, extra fee
        owner.alter_money(stand.prices.profit[stand.level])

    def afford_stand(self, player_id, grid_id):
        player = self.players[player_id]
        stand = self.grids[grid_id]
        if player.money < stand.prices.buy:
            return False
        else:
            return True

    def buy_stand(self, player_id, grid_id):
        player = self.players[player_id]
        stand = self.grids[grid_id]
        if not self.afford_stand(player_id, grid_id):
            raise Exception(f'Player {player.name} cannot afford stand {stand.name}')
        stand.owner_id = player.id
        player.alter_money(-stand.prices.buy)

    def next_turn(self):
        game.turn = (game.turn + 1) % len(self.players)


game = Game()
