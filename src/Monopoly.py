import pygame
from scenes.SceneManager import SceneManager
from scenes.LandingScene import LandingScene
from scenes.GameScene import GameScene


class Monopoly:
    def __init__(self):
        pygame.init()
        flags = pygame.RESIZABLE
        self.screen = pygame.display.set_mode((1100, 800), flags)
        self.screen.fill(pygame.Color('white'))
        self.timer = pygame.time.Clock()
        self.running = True
        self.init_scenes()

    def init_scenes(self):
        self.scene_manager = SceneManager()

        # add scene here
        self.scene_manager.add_scene(LandingScene(self.screen))
        self.scene_manager.add_scene(GameScene(self.screen))

        self.scene_manager.to_scene('landing')

    def run(self):
        while self.running:
            self.timer.tick(60)
            if pygame.event.get(pygame.QUIT):

                self.running = False
                return
            events = pygame.event.get()
            if len(events):
                self.scene_manager.scene.handle_events(events)
            self.scene_manager.scene.update()
            self.scene_manager.scene.render(self.screen)
            pygame.display.flip()

        pygame.quit()
