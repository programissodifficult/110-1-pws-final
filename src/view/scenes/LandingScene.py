import pygame

from ..CONST import DefaultScreenSize
from .basicComponents.Text import Text
from .basicComponents.Button import Button
from ..componentLib.SceneBase import Scene


class LandingScene(Scene):
    screen_size = (800, 800)

    def __init__(self):
        super().__init__('landing')

    def init(self):
        (width, height) = self.screen_size
        self.children.create_component('Image', 'assets/background.png', resize=self.screen_size, center=(width / 2, height / 2))
        self.children.create_component('ImageButton', 'assets/2P.png', (width * 3 / 12, height * 1 / 2), self.start_game, 2, resize=(128, 128), onclick_src='assets/2P_pressed.png')
        self.children.create_component('ImageButton', 'assets/3P.png', (width * 6 / 12, height * 1 / 2), self.start_game, 3, resize=(128, 128), onclick_src='assets/3P_pressed.png')
        self.children.create_component('ImageButton', 'assets/4P.png', (width * 9 / 12, height * 1 / 2), self.start_game, 4, resize=(128, 128), onclick_src='assets/4P_pressed.png')

    def start_game(self, player_amount):
        self.manager.to_scene('game', player_amount)
