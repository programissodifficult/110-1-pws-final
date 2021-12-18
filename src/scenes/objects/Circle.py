import pygame
from .BasicObject import BasicObject


class Circle(BasicObject):
    def __init__(self, radius, center, color):
        self.r = radius
        self.center = center
        self.color = color

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.r)
