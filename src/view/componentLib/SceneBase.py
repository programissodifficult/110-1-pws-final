import pygame

from ..CONST import DefaultScreenSize
from .ComponentBase import ComponentBase

class Scene(ComponentBase):
    screen_size = DefaultScreenSize

    def __init__(self, name, background_color=pygame.Color('white')):
        super().__init__()
        self.name = name
        self.background_color = background_color
