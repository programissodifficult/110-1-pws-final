import pygame

from .CONST import ScreenSize


class ViewManager():
    def __init__(self, ComponentRegistry):
        self.ComponentRegistry = ComponentRegistry
        self.scenes = {}
        self.scene = None

        flags = pygame.RESIZABLE
        self.screen = pygame.display.set_mode(ScreenSize, flags)
        self.screen.fill(pygame.Color('white'))

    def add_scene(self, scene):
        self.scenes[scene.name] = scene
        scene.manager = self

    def to_scene(self, scene_name, *args, **kwargs):
        scene = self.scenes[scene_name]
        scene.init(*args, **kwargs)
        self.scene = scene

    def rerender(self):
        self.scene.update()
        self.scene.render()
        pygame.display.flip()

    def tick(self):
        events = pygame.event.get()
        if len(events):
            self.scene.handle_events(events)
        self.rerender()
