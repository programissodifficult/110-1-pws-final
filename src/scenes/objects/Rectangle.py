import pygame
from .BasicObject import BasicObject

BorderWidth = 3

class Rectangle(BasicObject):
    def __init__(self, width, height, x, y, color):
        self.color = color
        self.geometry = pygame.Rect(x, y, width, height)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.geometry, BorderWidth)
