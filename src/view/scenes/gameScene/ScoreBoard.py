from os import path

from game.game import game
from game.CONST import BoardGridWidth
from ...CONST import BoxSize, ScreenSize
from ...componentLib.ComponentBase import ComponentBase


class ScoreBoard(ComponentBase):
    def init(self, player_id):
        self.id = player_id
        score_board_left_padding = BoxSize * BoardGridWidth
        score_board_height = ScreenSize[1] / 4

        # border
        border_left = score_board_left_padding
        border_top = score_board_height * self.id
        border_width = ScreenSize[0] - score_board_left_padding
        self.children.create_component('Rectangle', border_width, score_board_height, border_left, border_top)

        # player name
        text_center_x = score_board_left_padding + 20
        text_center_y = score_board_height * self.id + 30
        self.text_name = self.children.create_component('Text', str(self.player.name), 'Normal', midleft=(text_center_x, text_center_y))

        # player money
        text_center_x = score_board_left_padding + 50
        text_center_y = score_board_height * self.id + 80
        self.text_money = self.children.create_component('Text', str(self.player.money), 'Normal', midleft=(text_center_x, text_center_y))
        img_center_x = score_board_left_padding + 30
        img_center_y = score_board_height * self.id + 80
        self.children.create_component('Image', path.join('assets/icons24/dollar.png'), (img_center_x, img_center_y))

        # player own stand
        text_center_x = score_board_left_padding + 50
        text_center_y = score_board_height * self.id + 120
        self.text_own_stand = self.children.create_component('Text', str(
            len(self.player.own_stands)), 'Normal', midleft=(text_center_x, text_center_y))
        img_center_x = score_board_left_padding + 30
        img_center_y = score_board_height * self.id + 120
        self.children.create_component('Image', path.join('assets/icons24/stand.png'), (img_center_x, img_center_y))

        # player own technology
        text_center_x = score_board_left_padding + 50
        text_center_y = score_board_height * self.id + 160
        self.text_own_tech = self.children.create_component('Text', str(self.player.tech_invented), 'Normal', midleft=(text_center_x, text_center_y))
        img_center_x = score_board_left_padding + 30
        img_center_y = score_board_height * self.id + 160
        self.children.create_component('Image', path.join('assets/icons24/lamp.png'), (img_center_x, img_center_y))

    @property
    def player(self):
        return game.players[self.id]

    def update(self):
        self.text_name.content = str(self.player.name)
        self.text_money.content = str(self.player.money)
        self.text_own_stand.content = str(len(self.player.own_stands))
        self.text_own_tech.content = str(self.player.tech_invented)
