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
        timer = pygame.time.Clock()
        for i in range(step_size):
            self.player.step(1)
            self.manager.rerender()
            timer.tick(20)
            if self.player.position == self.player.home_position:
                game.pass_kitchen(self.player_id)

    def update(self):
        self.token.center = self.get_center()
