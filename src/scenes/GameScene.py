import pygame
from objects.Rectangle import Rectangle
from objects.Circle import Circle
from .Scene import Scene

BoxSize = 60
BoxColor = pygame.Color('black')
PlayerTokenRadius = 10
PlayerBorderPadding = 15


class GameScene(Scene):
    def __init__(self, screen):
        super().__init__('game', screen, background_color=pygame.Color('white'))

    def init_scene(self):
        self.add_object(Circle(PlayerTokenRadius, BoxSize + PlayerBorderPadding, BoxSize + PlayerBorderPadding, pygame.Color('blue')))
        self.add_object(Circle(PlayerTokenRadius, BoxSize + PlayerBorderPadding, BoxSize * 2 - PlayerBorderPadding, pygame.Color('red')))
        self.add_object(Circle(PlayerTokenRadius, BoxSize * 2 - PlayerBorderPadding, BoxSize + PlayerBorderPadding, pygame.Color('green')))
        self.add_object(Circle(PlayerTokenRadius, BoxSize * 2 - PlayerBorderPadding, BoxSize * 2 - PlayerBorderPadding, pygame.Color('yellow')))

        for i in range(1, 10):
            self.add_object(Rectangle(BoxSize, BoxSize, BoxSize * i, BoxSize * 1, BoxColor))
            self.add_object(Rectangle(BoxSize, BoxSize, BoxSize * 10, BoxSize * i, BoxColor))
            self.add_object(Rectangle(BoxSize, BoxSize, BoxSize * (11 - i), BoxSize * 10, BoxColor))
            self.add_object(Rectangle(BoxSize, BoxSize, BoxSize * 1, BoxSize * (11 - i), BoxColor))


    def handle_events(self, events):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                self.objects[0].x += BoxSize
