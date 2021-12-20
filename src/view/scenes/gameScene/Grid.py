from game.game import game

from ...CONST import *
from ...componentLib.ComponentBase import ComponentBase
from ..basicComponents.Rectangle import Rectangle
from ..basicComponents.Text import Text

from .gridHelper import grid_coord


class Grid(ComponentBase):
    def __init__(self, grid):
        super().__init__()
        self.grid_id = grid.id
        self.box_color = DefaultBoxColor
        self.children = [
            Rectangle(BoxSize, BoxSize, *grid_coord(self.grid_id), self.box_color)
        ]

    @property
    def grid(self):
        return game.grids[self.grid_id]

    @property
    def grid_padding(self):
        return grid_coord(self.grid_id)


class FoodStandGrid(Grid):
    def __init__(self, grid):
        super().__init__(grid)
        (x, y) = self.grid_padding
        self.children.create_component(Text(self.grid.name, 'Small', x + BoxSize / 2, y + BoxSize / 2)),
        self.children.create_component(Text(str(self.grid.price.buy), 'Small', x + BoxSize / 2, y + BoxSize * 3 / 4))


class EffectGrid(Grid):
    def __init__(self, grid):
        super().__init__(grid)
        (x, y) = self.grid_padding
        self.children.create_component(Text('Effect', 'Small', x + BoxSize / 2, y + BoxSize / 2))
        self.children.create_component(Text(self.grid.effect_type, 'Small', x + BoxSize / 2, y + BoxSize * 3 / 4))


class EventGrid(Grid):
    def __init__(self, grid):
        super().__init__(grid)
        (x, y) = self.grid_padding
        self.children.create_component(Text('抽一張經營卡', 'Small', x + BoxSize / 2, y + BoxSize / 2))


class MainKitchenGrid(Grid):
    def __init__(self, grid):
        super().__init__(grid)
        (x, y) = self.grid_padding
        self.children.create_component(Text(self.manager, '中央廚房', 'Small', x + BoxSize / 2, y + BoxSize * 1 / 2))
        self.children.create_component(Text(self.manager, self.player.name, 'Small', x + BoxSize / 2, y + BoxSize * 2 / 3))

    @property
    def player(self):
        return game.players[self.grid.player_id]

GridClassByType = {
    'FoodStand': FoodStandGrid,
    'Effect': EffectGrid,
    'Event': EventGrid,
    'MainKitchen': MainKitchenGrid,
}


def makeGrid(manager, grid):
    return GridClassByType[grid.type](manager, grid)
