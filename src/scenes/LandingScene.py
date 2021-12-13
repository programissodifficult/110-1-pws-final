import pygame
from objects.Text import Text
from .Scene import Scene


class LandingScene(Scene):
    def __init__(self, screen):
        super().__init__('landing', screen, background_color=pygame.Color('blue'))

    def init_scene(self):
        [width, height] = self.screen.get_size()
        self.add_object(Text('Monopoly', 'Title', width / 2, height / 3))
        self.add_object(Text('> press space to start <', 'Normal', width / 2, height * 2 / 3))

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.manager.to_scene('game')
