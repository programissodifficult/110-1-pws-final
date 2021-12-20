import pygame
import random
from game.game import game
from ...componentLib.SceneBase import Scene
from ...CONST import *
from .Grid import makeGrid
from .Player import Player


class GameScene(Scene):
    def __init__(self):
        super().__init__('game', background_color=pygame.Color('white'))
        self.grids = []
        self.players = []

    def init(self, player_amount):
        game.init(player_amount)

        for grid in game.grids:
            grid_token = makeGrid(self, grid)
            self.grids.append(grid_token)
            self.children.create_component(grid_token)

        for player in game.players:
            player_token = Player(player.id)
            self.players.append(player_token)
            self.children.create_component(player_token)

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                step = random.randint(1, 6)
                print(f"Clicked and go for {step} steps")
                self.players[game.turn].step(step)
                # game.players[0].step(1)
