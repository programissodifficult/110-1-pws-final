import random
from game.game import game

from ...componentLib.ComponentBase import ComponentBase
from ..basicComponents.Circle import Circle
from ...CONST import *



class RollButton(ComponentBase):
    def init(self):
        (width, height) = ScreenSize
        self.button = self.children.create_component('Button', 'Go', (width / 2, height / 2), 'Normal', pygame.Color('black'), self.roll)

    def roll(self):
        timer = pygame.time.Clock()
        for i in range(40):
            self.button.content = str(i % 6 + 1)
            self.manager.rerender()
            timer.tick(20)
        
        step = random.randint(1, 6)
        self.button.content = str(step)
        self.manager.scene.players[game.turn].step(step)
        game.current_player.get_grid().trigger()
        game.next_turn()
        self.button.content = "Go"
