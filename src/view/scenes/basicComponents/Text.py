import pygame
from ...componentLib.ComponentBase import ComponentBase
from ...CONST import DefaultTextColor

pygame.font.init()

fonts = {
    'Title': pygame.font.SysFont('microsoftjhenghei', 56),
    'Normal': pygame.font.SysFont('microsoftjhenghei', 32),
    'Small': pygame.font.SysFont('microsoftjhenghei', 14),
    'XSmall': pygame.font.SysFont('microsoftjhenghei', 8),
}

class Text(ComponentBase):
    def init(self, content, font_type, center, color=DefaultTextColor, background_color=None):
        self.color = color
        self.geometry = fonts[font_type].render(content, True, color, background_color)
        self.center = center

    def render(self):
        self.screen.blit(self.geometry, self.geometry.get_rect(center=self.center))
