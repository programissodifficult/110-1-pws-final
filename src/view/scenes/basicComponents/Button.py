import pygame

from ...componentLib.ComponentBase import ComponentBase
from .Text import Text
from .Rectangle import Rectangle


class Button(ComponentBase):
    def __init__(self):
        super().__init__()
    
    def init(self, text,  center, font, border_color, cb, *cbargs):
        self.text = self.children.create_component('Text', text, 'Normal', center)
        text_rect = self.text.geometry.get_rect()
        text_rect.height += 15
        text_rect.width += 30
        text_rect.center = center
        self.rect = self.children.create_component('Rectangle', text_rect.width, text_rect.height, text_rect.x, text_rect.y, border_color)
        self.cb = cb
        self.cbargs = cbargs

    def handle_events(self, events):
        x, y = pygame.mouse.get_pos()
        for evt in events:
            if evt.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.geometry.collidepoint(x, y):
                    self.cb(*self.cbargs)
