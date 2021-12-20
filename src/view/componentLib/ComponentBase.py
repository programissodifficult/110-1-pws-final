from pygame import constants
from .ComponentList import ComponentList

Verbose = True

class ComponentBase:
    def __init__(self):
        self.children = ComponentList(self)

    @property
    def screen(self):
        return self.manager.screen

    def init(self):
        raise NotImplementedError

    def update(self):
        for child in self.children:
            child.update()
        self.debug(type(self).__name__, 'updated')

    def render(self):
        for child in self.children:
            child.render()
        self.debug(type(self).__name__, 'rendered')

    def handle_events(self, events):
        pass

    def debug(self, *args, **kwargs):
        if Verbose:
            print(*args, **kwargs)