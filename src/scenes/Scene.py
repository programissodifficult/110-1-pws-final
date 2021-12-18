import pygame


class Scene(object):
    def __init__(self, scene_name, screen, background_color=pygame.Color('white')):
        self.name = scene_name
        self.screen = screen
        self.objects = []
        self.background_color = background_color

    def init_scene(self):
        pass

    def add_object(self, object):
        self.objects.append(object)

    def render(self, screen):
        screen.fill(self.background_color)

        for obj in self.objects:
            obj.render(screen)

    def update(self):
        pass

    def handle_events(self, events):
        for obj in self.objects:
            obj.handle_events(events)
