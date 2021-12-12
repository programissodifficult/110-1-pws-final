import pygame
from .BasicObject import BasicObject


class Circle(BasicObject):
    def __init__(self, radius, center_x, center_y, color):
        self.center = (center_x, center_y)
        self.radius = radius
        self.color = color

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radius)
