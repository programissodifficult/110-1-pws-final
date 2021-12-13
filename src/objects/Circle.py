import pygame
from .BasicObject import BasicObject


class Circle(BasicObject):
    def __init__(self, radius, center_x, center_y, color):
        self.x = center_x
        self.y = center_y
        self.r = radius
        self.color = color

    @property
    def center(self):
        return (self.x, self.y)

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.r)
