import pygame
from .objects.Text import Text
from .objects.Button import Button
from .Scene import Scene


class LandingScene(Scene):
    def __init__(self, screen):
        super().__init__('landing', screen)

    def init_scene(self):
        [width, height] = self.screen.get_size()
        self.add_object(Text('Monopoly', 'Title', width / 2, height / 3))
        # self.add_object(Text('> How much player is there? <', 'Normal', width / 2, height * 1 / 2))
        # self.add_object(Button('1', (width * 4 / 12, height * 2 / 3),'Normal', pygame.Color('black'), lambda : self.start_game(1)))
        self.add_object(Button('2P', (width * 4 / 12, height * 2 / 3),'Normal', pygame.Color('black'), self.start_game, 2))
        self.add_object(Button('3P', (width * 6 / 12, height * 2 / 3),'Normal', pygame.Color('black'), self.start_game, 3))
        self.add_object(Button('4P', (width * 8 / 12, height * 2 / 3),'Normal', pygame.Color('black'), self.start_game, 4))

    def start_game(self, player_amount):
        self.manager.to_scene('game', player_amount)