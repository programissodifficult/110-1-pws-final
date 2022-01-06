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
        # self.children.create_component('Text', '美食大富翁', 'Title', center=(width / 2, height / 3))
        # self.children.create_component('Text', '> 選擇玩家人數以開始遊戲 <', 'Normal', center=(width / 2, height * 1 / 2))
        # self.children.create_component(Button('1', (width * 4 / 12, height * 2 / 3),'Normal', lambda : self.start_game(1)))
        # self.children.create_component('Button', '2P', (width * 4 / 12, height * 1 / 2), self.start_game, 2, color=pygame.Color('white'), background_color=pygame.Color('black'))
        # self.children.create_component('Button', '3P', (width * 6 / 12, height * 1 / 2), self.start_game, 3, color=pygame.Color('white'), background_color=pygame.Color('black'))
        # self.children.create_component('Button', '4P', (width * 8 / 12, height * 1 / 2), self.start_game, 4, color=pygame.Color('white'), background_color=pygame.Color('black'))
        self.children.create_component('ImageButton', 'assets/go.png', (width * 4 / 12, height * 1 / 2), self.start_game, 2, resize=(96, 96), onclick_src='assets/go_pressed.png')
        self.children.create_component('ImageButton', 'assets/go.png', (width * 6 / 12, height * 1 / 2), self.start_game, 3, resize=(96, 96), onclick_src='assets/go_pressed.png')
        self.children.create_component('ImageButton', 'assets/go.png', (width * 8 / 12, height * 1 / 2), self.start_game, 4, resize=(96, 96), onclick_src='assets/go_pressed.png')

    def start_game(self, player_amount):
        self.manager.to_scene('game', player_amount)
