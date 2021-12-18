from .Grid import Grid

class MainKitchen(Grid):
    def __init__(self, id, player_id):
        super().__init__(id)
        self.player_id = player_id

    def trigger(self):
        # TODO
        pass