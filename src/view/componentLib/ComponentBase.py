from pygame import constants
from .ComponentList import ComponentList

# Verbose = True
Verbose = False


class ComponentBase:
    disabled = False

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
        self.debug('updated')

    def render(self):
        for child in self.children:
            if not child.disabled:
                child.render()
        self.debug('rendered')

    def handle_events(self, events):
        for child in self.children:
            child.handle_events(events)

    def debug(self, *args, **kwargs):
        if Verbose:
            print(type(self).__name__, *args, **kwargs)
