import pygame
from ...componentLib.ComponentBase import ComponentBase

BorderWidth = 2


class Rectangle(ComponentBase):
    def init(self, width, height, left, top, color=pygame.Color('black'), background_color=None, border_width=BorderWidth, inflate=None):
        self.color = color
        self.rect = pygame.Rect(left, top, width, height)
        if inflate:
            self.rect.inflate_ip(inflate)
        self.border_width = border_width
        self.bg_color = background_color

    def get_rect(self):
        return self.rect

    def render(self):
        if self.bg_color:
            pygame.draw.rect(self.screen, self.bg_color, self.rect)
        
        pygame.draw.rect(self.screen, self.color, self.rect, self.border_width)
