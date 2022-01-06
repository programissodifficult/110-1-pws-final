import pygame

from .util.cursor import use_default_cursor

from .CONST import BackgroundColor, DefaultScreenSize


class ViewManager():
    def __init__(self, ComponentRegistry):
        self.ComponentRegistry = ComponentRegistry
        self.scenes = {}
        self.scene = None

        self.flags = pygame.SHOWN
        pygame.display.set_caption('美食大富翁')
        self.screen = pygame.display.set_mode(DefaultScreenSize, self.flags)

    def add_scene(self, scene):
        self.scenes[scene.name] = scene
        scene.manager = self

    def to_scene(self, scene_name, *args, **kwargs):
        scene = self.scenes[scene_name]
        pygame.display.set_mode(scene.screen_size)
        scene.init(*args, **kwargs)
        self.scene = scene

    def rerender(self):
        self.screen.fill(BackgroundColor)
        self.scene.update()
        self.scene.render()
        pygame.display.flip()

    def tick(self):
        events = pygame.event.get()
        if len(events):
            for evt in events:
                if evt.type == pygame.MOUSEMOTION:
                    use_default_cursor()
                    break
            self.scene.handle_events(events)
        self.rerender()
