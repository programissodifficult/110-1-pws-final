import pygame

from ...componentLib.ComponentBase import ComponentBase
from ...util.cursor import use_default_cursor, use_hand_cursor


class Button(ComponentBase):
    def __init__(self):
        super().__init__()

    def init(self, content, center, cb, *cbargs, color=pygame.Color('black'), background_color = None, inflate=True, font='Normal'):
        self.center = center
        self.text = self.children.create_component('Text', content, font, color=color, center=self.center)
        text_rect = self.text.make_surface().get_rect(center=self.center)
        if inflate:
            text_rect.inflate_ip((text_rect.width / 2, text_rect.height / 5))
        self.rect = self.children.create_component('Rectangle', text_rect.width, text_rect.height, text_rect.x, text_rect.y, color, background_color=background_color, first=True)
        self.cb = cb
        self.cbargs = cbargs

    def set_content(self, content):
        content = str(content)
        self.text.content = content

    def handle_events(self, events):
        x, y = pygame.mouse.get_pos()

        for evt in events:
            if evt.type == pygame.MOUSEMOTION:
                if self.rect.geometry.collidepoint(*pygame.mouse.get_pos()):
                    use_hand_cursor()

            if evt.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.geometry.collidepoint(x, y):
                    use_default_cursor()
                    self.cb(*self.cbargs)
