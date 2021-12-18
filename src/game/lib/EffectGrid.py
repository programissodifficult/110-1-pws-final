from .Grid import Grid

class EffectGrid(Grid):
    def __init__(self, id, type):
        super().__init__(id)
        self.type = type

    def trigger(self):
        # TODO
        pass