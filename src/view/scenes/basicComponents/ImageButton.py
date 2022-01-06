import pygame
from time import sleep

from ...componentLib.ComponentBase import ComponentBase
from ...util.cursor import use_default_cursor, use_hand_cursor


class ImageButton(ComponentBase):
    def __init__(self):
        super().__init__()

    def init(self, src, center, cb, *cbargs, resize = None, onclick_src=None):
        self.img = self.children.create_component('Image', src, center=center, resize=resize)
        if onclick_src:
            self.onclick_img = self.children.create_component('Image', onclick_src, center=center, resize=resize)
            self.onclick_img.disabled = True
        else:
            self.onclick_img = None
        self.rect = self.img.get_rect(center=center)
        self.cb = cb
        self.cbargs = cbargs

    def handle_events(self, events):
        x, y = pygame.mouse.get_pos()

        for evt in events:
            if evt.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(*pygame.mouse.get_pos()):
                    use_hand_cursor()

            if evt.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(x, y):
                    if self.onclick_img:
                        self.img.disabled = True
                        self.onclick_img.disabled = False
                        self.manager.rerender()
                        sleep(0.1)
                        self.img.disabled = False
                        self.onclick_img.disabled = True
                        self.manager.rerender()
                    use_default_cursor()
                    self.cb(*self.cbargs)
