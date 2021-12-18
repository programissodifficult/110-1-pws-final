import pygame

from .BasicObject import BasicObject
from .Text import Text
from .Rectangle import Rectangle


class Button(BasicObject):
    def __init__(self, text,  center, font, border_color, cb, *cbargs):
        self.text = Text(text, 'Normal', center[0], center[1])
        text_rect = self.text.geometry.get_rect()
        text_rect.height += 15
        text_rect.width += 30
        text_rect.center = center
        self.rect = Rectangle(text_rect.width, text_rect.height, text_rect.x, text_rect.y, border_color)
        self.children = [
            self.text,
            self.rect
        ]
        self.cb = cb
        self.cbargs = cbargs

    def render(self, screen):
        for obj in self.children:
            obj.render(screen)

    def handle_events(self, events):
        x, y = pygame.mouse.get_pos()
        for evt in events:
            if evt.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.geometry.collidepoint(x, y):
                    self.cb(*self.cbargs)
