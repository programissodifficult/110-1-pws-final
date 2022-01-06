from game.game import game

from ...componentLib.ComponentBase import ComponentBase
from ...CONST import *

block_height = 80
x_margin = 200


class PlayerScore(ComponentBase):
    def init(self, id, rank, real_rank):
        (scene_width, scene_height) = self.scene.screen_size
        self.player_id = id
        board_top_padding = (scene_height - block_height * len(game.players)) / 2 + rank * block_height + 20
        text_center_x = scene_width / 2
        text_center_y = board_top_padding + block_height / 2
        scores = self.player.get_score()
        content = f'#{real_rank + 1} {self.player.name} {scores["total"]}'
        self.children.create_component('Text',  content, 'Normal', center=(text_center_x, text_center_y), color=pygame.Color('white'))
        self.children.create_component('Rectangle', scene_width - 2 * x_margin, block_height, x_margin, board_top_padding, color=pygame.Color('white'))

    @property
    def player(self):
        return game.players[self.player_id]
