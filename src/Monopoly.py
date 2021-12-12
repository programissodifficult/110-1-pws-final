import pygame
from pygame.locals import *
from scenes.SceneManager import SceneManager
from scenes.LandingScene import LandingScene
from scenes.GameScene import GameScene


class Monopoly:
    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        self.screen = pygame.display.set_mode((1024, 768), flags)
        self.screen.fill(Color('white'))
        self.timer = pygame.time.Clock()
        self.running = True
        self.init_scenes()

    def init_scenes(self):
        self.scene_manager = SceneManager()
        
        # add scene here
        self.scene_manager.add_scene(LandingScene(self.screen))
        self.scene_manager.add_scene(GameScene(self.screen))
        

    def run(self):
        while self.running:
            self.timer.tick(60)
            if pygame.event.get(QUIT):
                self.running = False
                return
            self.scene_manager.scene.handle_events(pygame.event.get())
            self.scene_manager.scene.update()
            self.scene_manager.scene.render(self.screen)
            pygame.display.flip()

        pygame.quit()
