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
        text_center_x = score_board_left_padding + 50
        text_center_y = score_board_height * self.id + 50
        self.text_name = self.children.create_component('Text', self.player.name, 'Normal', (text_center_x, text_center_y))

        # player money
        text_center_x = score_board_left_padding + 50
        text_center_y = score_board_height * self.id + 70
        self.text_money = self.children.create_component('Text', str(self.player.money), 'Normal', (text_center_x, text_center_y))

    @property
    def player(self):
        return game.players[self.id]

    def update(self):
        self.text_name.content = self.player.name
        self.text_money.content = str(self.player.money)
