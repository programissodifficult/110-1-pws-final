from game.game import game

from ...componentLib.ComponentBase import ComponentBase
from ...CONST import *

board_height = 80
x_margin = 200


class PlayerScore(ComponentBase):
    def init(self, id, rank, real_rank):
        (scene_width, scene_height) = self.scene.screen_size
        self.player_id = id
        board_top_padding = (scene_height - board_height * len(game.players)) / 2 + rank * board_height + 20
        text_center_x = scene_width / 2
        text_center_y = board_top_padding + board_height / 2
        board_width = scene_width - 2 * x_margin
        scores = self.player.get_score()
        content = f'#{real_rank + 1} {self.player.name} {scores["total"]}'
        self.children.create_component('Rectangle', board_width, board_height, x_margin, board_top_padding, color=pygame.Color('gray10'), border_width=0)
        self.children.create_component('Text',  content, 'Normal', center=(text_center_x, text_center_y), color=pygame.Color('gray90'))
        self.children.create_component('Rectangle', board_width, board_height, x_margin, board_top_padding, color=pygame.Color('gray90'))

    @property
    def player(self):
        return game.players[self.player_id]
