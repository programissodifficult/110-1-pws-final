import random
from game.game import game
from util.Dialog import confirm

from ...componentLib.ComponentBase import ComponentBase
from ..basicComponents.Circle import Circle
from ...CONST import *


def get_roll_number():
    return random.randint(1, 6) + random.randint(1, 6)


class RollButton(ComponentBase):
    def init(self):
        (width, height) = ScreenSize
        score_board_width = BoxSize * BoardGridWidth
        self.button = self.children.create_component('Button', 'Go', (score_board_width / 2, height / 2), 'Normal', pygame.Color('black'), self.roll)

    def roll(self):
        # roll dice animation
        timer = pygame.time.Clock()
        for i in range(40):
            self.button.content = str(get_roll_number())
            self.manager.rerender()
            timer.tick(40)

        # step animation
        step = get_roll_number()
        self.button.content = str(step)
        self.manager.scene.players[game.turn].step(step)

        # trigger grid effect
        game.current_player.get_grid().trigger()

        # post round
        self.next_turn()

    def next_turn(self):
        self.button.content = "Go"
        game.next_turn()
        if game.current_player.idle_round > 0:
            game.current_player.idle_round -= 1
            confirm("停止行動", f"{game.current_player.name} 暫停行動一回合...")
            self.next_turn()
