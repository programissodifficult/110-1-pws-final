import pygame
from ...componentLib.ComponentBase import ComponentBase

class Image(ComponentBase):
    def init(self, src, **kwargs):
        self.img = pygame.image.load(src)
        self.image_rect = self.img.get_rect(**kwargs)

    def render(self):
        self.screen.blit(self.img, self.image_rect)
