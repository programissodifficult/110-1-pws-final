import pygame
from game.game import game
from ..objects.Rectangle import Rectangle
from ..Scene import Scene
from ..CONST import *
from .Grid import makeGrid
from .Player import Player


class GameScene(Scene):
    def __init__(self, screen):
        super().__init__('game', screen, background_color=pygame.Color('white'))

    def init_scene(self, player_amount):
        game.init(player_amount)

        for grid in game.grids:
            self.add_object(makeGrid(grid))

        for player in game.players:
            self.add_object(Player(player.id))

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                game.players[0].step(1)
