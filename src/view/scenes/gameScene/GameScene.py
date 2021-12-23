import pygame
import random
from game.game import game
from ...componentLib.SceneBase import Scene
from ...CONST import *


GridClassByType = {
    'FoodStand': 'FoodStandGrid',
    'Effect': 'EffectGrid',
    'Event': 'EventGrid',
    'MainKitchen': 'MainKitchenGrid',
}


class GameScene(Scene):
    def __init__(self):
        super().__init__('game', background_color=pygame.Color('white'))
        self.grids = []
        self.players = []

    def init(self, player_amount):
        game.init(player_amount)

        for grid in game.grids:
            grid_comp = self.children.create_component(GridClassByType[grid.type], grid)
            self.grids.append(grid_comp)

        for player in game.players:
            player_comp = self.children.create_component('Player', player.id)
            self.players.append(player_comp)

        for player in game.players:
            self.children.create_component('ScoreBoard', player.id)
        
        self.children.create_component('RollButton')

    # def handle_events(self, events):
    #     for e in events:
    #         if e.type == pygame.MOUSEBUTTONDOWN:
    #             step = random.randint(1, 6)
    #             self.players[game.turn].step(step)
    #             game.current_player.get_grid().trigger()
    #             game.next_turn()
