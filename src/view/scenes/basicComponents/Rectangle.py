import pygame
from ...componentLib.ComponentBase import ComponentBase

BorderWidth = 2


class Rectangle(ComponentBase):
    def init(self, width, height, left, top, color=pygame.Color('black'), border_width=BorderWidth):
        self.color = color
        self.geometry = pygame.Rect(left, top, width, height)
        self.border_width = border_width

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.geometry, self.border_width)
