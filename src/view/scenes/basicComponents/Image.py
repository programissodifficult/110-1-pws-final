import pygame
from ...componentLib.ComponentBase import ComponentBase

class Image(ComponentBase):
    def init(self, src, resize=None, **kwargs):
        self.img = pygame.image.load(src)
        if resize:
            self.img = pygame.transform.scale(self.img, resize)
        self.image_rect = self.img.get_rect(**kwargs)

    def get_rect(self, **kwargs):
        return self.img.get_rect(**kwargs)

    def render(self):
        self.screen.blit(self.img, self.image_rect)
