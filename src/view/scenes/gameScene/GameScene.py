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
        super().__init__('game')
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
