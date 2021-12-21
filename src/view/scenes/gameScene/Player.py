from game.game import game

from ...componentLib.ComponentBase import ComponentBase
from ..basicComponents.Circle import Circle
from ...CONST import *

from .gridHelper import grid_coord


class Player(ComponentBase):
    def init(self, id):
        self.player_id = id
        self.token = self.children.create_component('Circle', PlayerTokenRadius, self.get_center(), self.player.color)

    @property
    def player(self):
        return game.players[self.player_id]

    def get_center(self):
        return grid_coord(self.player.position, self.player.id)

    def step(self, step_size):
        self.step_to(self.player.position + step_size)

    def step_to(self, pos):
        timer = pygame.time.Clock()
        while pos != self.player.position:
            self.player.step(1)
            self.manager.rerender()
            timer.tick(3)

    def update(self):
        self.token.center = self.get_center()
