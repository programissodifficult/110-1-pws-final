import pygame
from ...componentLib.ComponentBase import ComponentBase


class Circle(ComponentBase):
    def init(self, radius, center, color, border=None):
        self.r = radius
        self.center = center
        self.color = color
        self.border = border

    def render(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.r)
        if self.border:
            pygame.draw.circle(self.screen, pygame.Color('black'), self.center, self.r, self.border)

