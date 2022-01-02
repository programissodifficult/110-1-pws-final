import pygame
from ...componentLib.ComponentBase import ComponentBase

BorderWidth = 2


class Rectangle(ComponentBase):
    def init(self, width, height, left, top, color=pygame.Color('black')):
        self.color = color
        self.geometry = pygame.Rect(left, top, width - 1, height - 1)

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.geometry, BorderWidth)
