import pygame
from pygame.locals import *
from scenes.SceneManager import SceneManager
from scenes.LandingScene import LandingScene


class Monopoly:
    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        self.screen = pygame.display.set_mode((1024, 768), flags)
        self.screen.fill(Color('white'))
        self.timer = pygame.time.Clock()
        self.running = True
        self.init_scene()

    def init_scene(self):
        self.scene_manager = SceneManager()
        
        # add scene here
        self.scene_manager.add_scene(LandingScene())
        

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


if __name__ == '__main__':
    Monopoly().run()
