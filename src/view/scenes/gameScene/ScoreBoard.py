from os import path

from game.game import game
from game.CONST import BoardGridWidth
from ...CONST import BorderColor, GridSize, DefaultScreenSize
from ...componentLib.ComponentBase import ComponentBase


class ScoreBoard(ComponentBase):
    def init(self, player_id):
        self.id = player_id
        board_left = GridSize * BoardGridWidth
        width = DefaultScreenSize[0] - board_left
        height = DefaultScreenSize[1] / 4
        board_top = height * self.id

        left_padding = 20
        left_padding2 = 170
        top_padding = 90
        top_padding2 = 150
        text_padding = 35

        # inner border
        self.inner_border = self.children.create_component('Rectangle', width, height, board_left, board_top, border_width=4, color=self.player.color, inflate=(-4, -4))
        self.inner_border.disabled = True

        # border
        self.children.create_component('Rectangle', width, height, board_left, board_top, BorderColor)

        # player name
        text_pos = (board_left + left_padding, board_top + 40)
        self.text_name = self.children.create_component('Text', self.player.name, 'Normal', self.player.color, midleft=text_pos)

        # player money
        img_pos = (board_left + left_padding, board_top + top_padding)
        self.children.create_component('Image', path.join('assets/icons24/dollar.png'), midleft=img_pos)
        text_pos = (board_left + left_padding + text_padding, board_top + top_padding)
        self.text_money = self.children.create_component('Text', '', 'Normal', midleft=text_pos)

        # player own technology
        img_pos = (board_left + left_padding, board_top + top_padding2)
        self.children.create_component('Image', path.join('assets/icons24/lamp.png'), midleft=img_pos)
        text_pos = (board_left + left_padding + text_padding, board_top + top_padding2)
        self.text_own_tech = self.children.create_component('Text', '', 'Normal', midleft=text_pos)

        # player own stand
        img_pos = (board_left + left_padding2, board_top + top_padding)
        self.children.create_component('Image', path.join('assets/icons24/stand.png'), midleft=img_pos)
        text_pos = (board_left + left_padding2 + text_padding, board_top + top_padding)
        self.text_own_stand = self.children.create_component('Text', '', 'Normal', midleft=text_pos)

        # player own table
        img_pos = (board_left + left_padding2, board_top + top_padding2)
        self.children.create_component('Image', path.join('assets/icons24/table.png'), midleft=img_pos)
        text_pos = (board_left + left_padding2 + text_padding, board_top + top_padding2)
        self.text_own_table = self.children.create_component('Text', '', 'Normal', midleft=text_pos)

        # player show info button
        btn_center_x = DefaultScreenSize[0] - 45
        btn_center_y = board_top + 45
        self.children.create_component('ImageButton', 'assets/icons24/info.png', (btn_center_x, btn_center_y), self.show_info)

    def show_info(self):
        self.player.show_info()

    @property
    def player(self):
        return game.players[self.id]

    def update(self):
        self.inner_border.disabled = game.current_player != self.player
        self.text_money.set_content(self.player.money)
        self.text_own_stand.set_content(len(self.player.own_stands))
        self.text_own_table.set_content(sum([stand.level for stand in self.player.own_stands]))
        self.text_own_tech.set_content(len(self.player.tech_invented))
