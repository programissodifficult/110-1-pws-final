from game.game import game

from ...componentLib.ComponentBase import ComponentBase
from ..basicComponents.Circle import Circle
from ...CONST import *

from .gridHelper import grid_coord


class Player(ComponentBase):
    def __init__(self, id):
        super().__init__()
        self.player_id = id
        self.token = Circle(PlayerTokenRadius, self.get_center(), self.player.color)
        self.children.create_component(self.token)

    @property
    def player(self):
        return game.players[self.player_id]

    def get_center(self):
        return grid_coord(self.player.position, self.player.id)

    def step(self, step_size):
        self.step_to(self.player.position + step_size)

    def step_to(self, pos):
        timer = pygame.time.Clock()
        print(f'self.player.position {self.player.position}')
        while pos != self.player.position:
            print(f'self.player.position {self.player.position}')
            self.player.step(1)
            timer.tick(3)

    def update(self):
        self.token.center = self.get_center()
