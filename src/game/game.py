import random


from .CONST import StandMaxLevel

from .lib.GridImpl import make_grids
from .lib.EventImpl import make_event_cards
from .lib.TechImpl import make_tech_cards
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
        self.init_techs()

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

    def init_techs(self):
        self.tech_cards = make_tech_cards()

        for tech in self.tech_cards:
            tech.game = self

        self.tech_pointer = 0
        random.shuffle(self.tech_cards)

    # ############################################################
    #  game play helper
    # ############################################################

    def player_exists(self, player_id):
        return 0 <= player_id and player_id < len(self.players)

    def draw_event_card(self):
        card = self.event_cards[self.event_pointer]
        self.event_pointer += 1
        if self.event_pointer >= len(self.event_cards):
            self.reshuffle_events()
        return card

    def draw_tech_card(self):
        if self.tech_pointer >= len(self.event_cards):
            print(Exception('[Game.draw_tech_card] tech cards empty'))
            return
        card = self.tech_cards[self.tech_pointer]
        self.tech_pointer += 1
        return card

    def player_transfer_money(self, receiver_id, giver_id, amount):
        receiver = self.players[receiver_id]
        giver = self.players[giver_id]
        amount = min(amount, giver.money)
        receiver.alter_money(amount)
        giver.alter_money(-amount)

    def get_stand_profit(self, grid_id, triggerer_id):
        stand = self.grids[grid_id]
        triggerer = self.players[triggerer_id]
        owner = stand.owner
        if owner == None:
            raise Exception(f'Cannot get profit of stand {stand.name} with no owner')
        return stand.prices.profit[stand.level] - triggerer.stand_fee_discount + owner.extra_stand_fee

    def profit_stand(self, grid_id, triggerer_id):
        stand = self.grids[grid_id]
        owner = stand.owner
        if owner == None:
            raise Exception(f'Cannot profit stand {stand.name} with no owner')
        owner.alter_money(self.get_stand_profit(grid_id, triggerer_id))

    def get_stand_buy_price(self, player_id, grid_id):
        stand = self.grids[grid_id]
        return stand.prices.buy

    def get_stand_build_price(self, player_id, grid_id):
        player = self.players[player_id]
        stand = self.grids[grid_id]
        return stand.prices.build - player.build_discount

    def ask_for_build_table(self, player_id, stand_id):
        player = self.players[player_id]
        stand = self.grids[stand_id]
        price = self.get_stand_build_price(player_id, stand_id)

        # sanity check
        if stand.owner_id != player_id:
            print(Exception(f'[Game.ask_for_build_table] player "{player.name}" does not own stand {stand.name}'))

        if stand.level == StandMaxLevel:
            confirm("建設攤位", f"{stand.name}的桌子數量已達上限，無法再建造更多桌子了")
            return

        if player.money >= price:
            result = yesno("建設攤位", f"是否以 {price} 元在{stand.name}建設一張桌子")
            if result:
                self.build_stand(player_id, stand_id)

                # handle double table tech
                if player.double_table and player.money >= price:
                    if stand.level < StandMaxLevel:
                        confirm("建設攤位", f"[技術卡效果] {stand.name}的桌子數量已達上限，無法再建造更多桌子了")
                    else:
                        result = yesno("建設攤位", f"[技術卡效果] 是否要以 {price} 元在{stand.name}再建設一張桌子")
                        if result:
                            self.build_stand(player_id, stand_id)

        else:
            confirm("建設攤位", f"你的錢好像不太夠，你得要有 {stand.prices.buy} 元才能在{stand.name}建設一張桌子")

    def ask_for_buy_stand(self, player_id, stand_id):
        player = self.players[player_id]
        stand = self.grids[stand_id]
        owner_msg = ''
        if stand.owner_id != None:
            owner_msg = f"向 {stand.owner.name} "
        if player.money >= self.get_stand_buy_price(player_id, stand_id):
            result = yesno("購買攤位", f"是否以 {stand.prices.buy} 元{owner_msg}購買{stand.name}")
            if result:
                self.buy_stand(player_id, stand_id)
        else:
            confirm("購買攤位", f"你的錢好像不太夠，無法購買 {stand.prices.buy} 元的{stand.name}")

    def pass_kitchen(self, player_id):
        player = self.players[player_id]

        if player.idle_kitchen:
            player.idle_kitchen -= 1
            confirm("經過中央廚房", "受經營卡效果影響，暫停一次")
            return

        price = player.get_tech_invent_price()
        income = player.get_income()
        if player.money >= price:
            result = yesno("經過中央廚房", f"是否研發技術卡（若研發則不得領取 {income} 元）")
            if result:
                self.invent_tech(player_id)
                return
        player.alter_money(income)
        confirm("經過中央廚房", f"獲得收入 {income} 元")

    def buy_stand(self, player_id, grid_id):
        player = self.players[player_id]
        stand = self.grids[grid_id]
        owner = stand.owner
        if player.money < self.get_stand_buy_price(player_id, grid_id):
            print(Exception(f'[Game.buy_stand] Player {player.name} cannot afford buying stand {stand.name}'))
        stand.owner_id = player.id
        player.alter_money(-stand.prices.buy)
        if owner:
            owner.alter_money(stand.prices.buy)

    def build_stand(self, player_id, grid_id):
        player = self.players[player_id]
        stand = self.grids[grid_id]
        price = self.get_stand_build_price(player_id, grid_id)

        # sanity check
        if player.money < price:
            print(Exception(f'[Game.build_stand] Player {player.name} cannot afford building stand {stand.name}'))

        if stand.level == StandMaxLevel:
            print(Exception(f'[Game.build_stand] Stand {stand.name} already at max level'))

        stand.level += 1
        player.alter_money(-price)

    def invent_tech(self, player_id):
        player = self.players[player_id]
        card = self.draw_tech_card()
        player.alter_money(-player.get_tech_invent_price())
        confirm("研發技術卡", f"{card.tech_description}：\n{card.ability_description}")
        card.trigger(player)
        player.tech_invented += 1

    def next_turn(self):
        game.turn = (game.turn + 1) % len(self.players)

    def random_remove_table(self, player_id):
        player = self.players[player_id]
        stands = player.own_stands
        random.shuffle(stands)
        for stand in stands:
            if stand.level > 0:
                stand.level -= 1
                return stand
        else:
            confirm("移除桌子", "沒有任何桌子可以移除")
            return None

    def switch_position(self, player_id_1, player_id_2):
        player_1 = self.players[player_id_1]
        player_2 = self.players[player_id_2]
        player_1.position, player_2.position = player_2.position, player_1.position


game = Game()
