import pygame
from game.game import game
from .objects.Rectangle import Rectangle
from .Player import Player
from .Scene import Scene
from .CONST import *
from .grid import grid

class GameScene(Scene):
    def __init__(self, screen):
        super().__init__('game', screen, background_color=pygame.Color('white'))

    def init_scene(self, player_amount):
        game.init(player_amount)
        for player in game.players:
            self.add_object(Player(player.id))
        # TODO: use `Grid` class instead
        for i in range(0, 36):
            (x, y) = grid(i)
            self.add_object(Rectangle(BoxSize, BoxSize, x, y, BoxColor))

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                game.players[0].step(1)
