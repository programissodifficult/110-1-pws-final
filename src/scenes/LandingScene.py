import pygame
from .Scene import Scene


class LandingScene(Scene):
    def __init__(self):
        super(LandingScene, self).__init__('landing')
        self.font = pygame.font.SysFont('Arial', 56)
        self.sfont = pygame.font.SysFont('Arial', 32)

    def render(self, screen):
        screen.fill((50, 50, 150))
        text1 = self.font.render('Monopoly', True, (255, 255, 255))
        text2 = self.font.render(
            '> press space to start <', True, (255, 255, 255))
        [width, height] = screen.get_size()
        screen.blit(text1, text1.get_rect(center=(width / 2, height / 3)))
        screen.blit(text2, text2.get_rect(center=(width / 2, height * 2 / 3)))

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.manager.to_scene('game')
