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
        text_center_x = score_board_left_padding + 40
        text_center_y = score_board_height * self.id + 50
        self.text_name = self.children.create_component('Text', f'{self.player.name :<}', 'Normal', (text_center_x, text_center_y))

        # player money
        text_center_x = score_board_left_padding + 115
        text_center_y = score_board_height * self.id + 90
        self.text_money = self.children.create_component('Text', f': {self.player.money :<6}', 'Normal', (text_center_x, text_center_y))

        # player own stand
        text_center_x = score_board_left_padding + 73
        text_center_y = score_board_height * self.id + 130
        self.text_own_stand = self.children.create_component('Text', f'Stand: {len(self.player.own_stands) :<2}', 'Normal', (text_center_x, text_center_y))

        # player own technology
        text_center_x = score_board_left_padding + 133
        text_center_y = score_board_height * self.id + 170
        self.text_own_tech = self.children.create_component('Text', f'Tech Invented: {self.player.tech_invented :<2}', 'Normal', (text_center_x, text_center_y))

    @property
    def player(self):
        return game.players[self.id]

    def update(self):
        self.text_name.content = f'{self.player.name :<}'
        self.text_money.content = f'Money: {self.player.money :<6}'
        self.text_own_stand.content = f'Stand: {len(self.player.own_stands) :<2}'
        self.text_own_tech.content = f'Tech Invented: {self.player.tech_invented :<2}'
