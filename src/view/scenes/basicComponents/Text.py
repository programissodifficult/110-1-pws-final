import pygame
from ...componentLib.ComponentBase import ComponentBase
from ...CONST import DefaultTextColor

pygame.font.init()

FontFilePath = './assets/microsoftjhenghei.ttf'
# FontFilePath = './assets/TaipeiSans.ttf'

fonts = {
    'Title': pygame.font.Font(FontFilePath, 56),
    'Normal': pygame.font.Font(FontFilePath, 32),
    'Normal': pygame.font.Font(FontFilePath, 32),
    'Small': pygame.font.Font(FontFilePath, 14),
    'XSmall': pygame.font.Font(FontFilePath, 8),
}


# about Text positioning, see https://www.pygame.org/docs/ref/rect.html for rect attributes
class Text(ComponentBase):
    def init(self, content, font_type, color=DefaultTextColor, background_color=None, **kwargs):
        self.content = content
        self.font_type = font_type
        self.pos = kwargs
        self.color = color
        self.background_color = background_color

    def make_surface(self):
        return fonts[self.font_type].render(self.content, True, self.color, self.background_color)

    def render(self):
        text_surf = self.make_surface()
        self.screen.blit(text_surf, text_surf.get_rect(**self.pos))
