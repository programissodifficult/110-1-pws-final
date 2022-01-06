from os import path

from game.game import game
from game.CONST import BoardGridWidth
from ...CONST import BoxSize, DefaultScreenSize
from ...componentLib.ComponentBase import ComponentBase


class ScoreBoard(ComponentBase):
    def init(self, player_id):
        self.id = player_id
        score_board_height = DefaultScreenSize[1] / 4
        left_padding = BoxSize * BoardGridWidth
        top_padding = score_board_height * self.id

        # border
        border_left = left_padding
        border_top = top_padding
        border_width = DefaultScreenSize[0] - left_padding
        self.children.create_component('Rectangle', border_width, score_board_height, border_left, border_top)

        # player name
        name_left_padding = left_padding + 20
        name_mid_y_padding = top_padding + 30
        self.text_name = self.children.create_component('Text', str(self.player.name), 'Normal', midleft=(name_left_padding, name_mid_y_padding))

        # player money
        info_left_padding = left_padding + 50
        info_mid_y_padding = top_padding + 80
        self.text_money = self.children.create_component('Text', str(self.player.money), 'Normal', midleft=(info_left_padding, info_mid_y_padding))
        img_center_x = left_padding + 30
        img_center_y = top_padding + 80
        self.children.create_component('Image', path.join('assets/icons24/dollar.png'), center=(img_center_x, img_center_y))

        # player own stand
        info_mid_y_padding = top_padding + 120
        self.text_own_stand = self.children.create_component('Text', str(
            len(self.player.own_stands)), 'Normal', midleft=(info_left_padding, info_mid_y_padding))
        img_center_y = top_padding + 120
        self.children.create_component('Image', path.join('assets/icons24/stand.png'), center=(img_center_x, img_center_y))

        # player own technology
        info_mid_y_padding = top_padding + 160
        self.text_own_tech = self.children.create_component('Text', str(len(self.player.tech_invented)),
                                                            'Normal', midleft=(info_left_padding, info_mid_y_padding))
        img_center_y = top_padding + 160
        self.children.create_component('Image', path.join('assets/icons24/lamp.png'), center=(img_center_x, img_center_y))

        # player show info button
        btn_center_x = DefaultScreenSize[0] - 30
        btn_center_y = top_padding + 30
        self.children.create_component('Button', ' i ', (btn_center_x, btn_center_y), self.show_info, font='Small', inflate=True)

    def show_info(self):
        self.player.show_info()

    @property
    def player(self):
        return game.players[self.id]

    def update(self):
        self.text_money.content = str(self.player.money)
        self.text_own_stand.content = f'{len(self.player.own_stands)}/{sum([stand.level for stand in self.player.own_stands])}'
        self.text_own_tech.content = f'{len(self.player.tech_invented)}'
