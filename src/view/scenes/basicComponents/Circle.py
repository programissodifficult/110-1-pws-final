import pygame
from ...componentLib.ComponentBase import ComponentBase


class Circle(ComponentBase):
    def __init__(self, radius, center, color):
        self.r = radius
        self.center = center
        self.color = color

    def render(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.r)
