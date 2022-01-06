from game.game import game

from ...componentLib.ComponentBase import ComponentBase
from ...CONST import *

height = 80
x_margin = 200


class PlayerScore(ComponentBase):
    def init(self, id, rank, real_rank):
        self.player_id = id
        board_top_padding = (DefaultScreenSize[1] - height * len(game.players)) / 2 + rank * height + 20
        text_center_x = DefaultScreenSize[0] / 2
        text_center_y = board_top_padding + height / 2
        scores = self.player.get_score()
        content = f'#{real_rank + 1} {self.player.name} {scores["total"]}'
        self.children.create_component('Text',  content, 'Normal', center=(text_center_x, text_center_y))
        self.children.create_component('Rectangle', DefaultScreenSize[0] - 2 * x_margin, height, x_margin, board_top_padding)

    @property
    def player(self):
        return game.players[self.player_id]
