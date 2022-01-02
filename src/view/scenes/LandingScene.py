import pygame

from ..CONST import ScreenSize
from .basicComponents.Text import Text
from .basicComponents.Button import Button
from ..componentLib.SceneBase import Scene


class LandingScene(Scene):
    def __init__(self):
        super().__init__('landing')

    def init(self):
        (width, height) = ScreenSize
        self.children.create_component('Text', 'Monopoly', 'Title', center=(width / 2, height / 3))
        # self.children.create_component(Text('> How much player is there? <', 'Normal', width / 2, height * 1 / 2))
        # self.children.create_component(Button('1', (width * 4 / 12, height * 2 / 3),'Normal', pygame.Color('black'), lambda : self.start_game(1)))
        self.children.create_component('Button', '2P', (width * 4 / 12, height * 2 / 3), 'Normal', pygame.Color('black'), self.start_game, 2)
        self.children.create_component('Button', '3P', (width * 6 / 12, height * 2 / 3), 'Normal', pygame.Color('black'), self.start_game, 3)
        self.children.create_component('Button', '4P', (width * 8 / 12, height * 2 / 3), 'Normal', pygame.Color('black'), self.start_game, 4)

    def start_game(self, player_amount):
        self.manager.to_scene('game', player_amount)
