import pygame
from view.ViewManager import ViewManager
from view.scenes.LandingScene import LandingScene
from view.scenes.gameScene import GameScene
from view.scenes.scoreScene.ScoreScene import ScoreScene
from view.ComponentRegistry import ComponentRegistry


class Monopoly:
    def __init__(self):
        pygame.init()
        self.timer = pygame.time.Clock()
        self.running = True 
        self.view_manager = ViewManager(ComponentRegistry)
        self.init_scenes()

    def init_scenes(self):
        self.view_manager.add_scene(LandingScene())
        self.view_manager.add_scene(GameScene())
        self.view_manager.add_scene(ScoreScene())

        self.view_manager.to_scene('landing')

    def run(self):
        while self.running:
            self.timer.tick(20)
            if pygame.event.get(pygame.QUIT):
                self.running = False
                return
            self.view_manager.tick()
        pygame.quit()
