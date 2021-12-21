import pygame
from .ComponentBase import ComponentBase

class Scene(ComponentBase):
    def __init__(self, name, background_color=pygame.Color('white')):
        super().__init__()
        self.name = name
        self.background_color = background_color
