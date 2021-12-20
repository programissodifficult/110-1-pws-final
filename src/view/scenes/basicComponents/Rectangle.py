import pygame
from ...componentLib.ComponentBase import ComponentBase

BorderWidth = 3

class Rectangle(ComponentBase):
    def init(self, width, height, x, y, color):
        self.color = color
        self.geometry = pygame.Rect(x, y, width, height)

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.geometry, BorderWidth)
