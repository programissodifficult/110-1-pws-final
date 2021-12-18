import pygame

from .objects.BasicObject import BasicObject
from .objects.Circle import Circle

from game.game import game
from .CONST import *
from .grid import grid


class Player(BasicObject):
    def __init__(self, id):
        self.player_id = id
        self.token = Circle(PlayerTokenRadius, self.get_center(), self.player.color)

    @property
    def player(self):
        return game.players[self.player_id]

    def get_center(self):
        return grid(self.player.position, self.player.id)

    def render(self, screen):
        self.token.center = self.get_center()
        self.token.render(screen)

    def handle_events(self, events):
        pass
