class Scene(object):
    def __init__(self, scene_name):
        self.name = scene_name

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError