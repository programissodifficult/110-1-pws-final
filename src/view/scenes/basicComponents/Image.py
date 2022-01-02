import pygame
from ...componentLib.ComponentBase import ComponentBase

class Image(ComponentBase):
    def init(self, src, center):
        self.img = pygame.image.load(src)
        self.image_rect = self.img.get_rect()
        self.image_rect.center = center

    def render(self):
        self.screen.blit(self.img, self.image_rect)
