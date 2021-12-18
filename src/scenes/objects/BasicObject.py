class BasicObject:
    def __init__(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def handle_events(self, events):
        pass
