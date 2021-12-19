from game.game import game

from ..objects.Rectangle import Rectangle
from ..objects.Text import Text
from ..objects.BasicObject import BasicObject
from ..CONST import *

from .gridHelper import grid_pos


class Grid(BasicObject):
    def __init__(self, grid):
        self.grid_id = grid.id
        self.box_color = DefaultBoxColor
        self.children = [
            Rectangle(BoxSize, BoxSize, *grid_pos(self.grid_id), self.box_color)
        ]

    @property
    def grid(self):
        return game.grids[self.grid_id]

    @property
    def grid_padding(self):
        return grid_pos(self.grid_id)

    def add_object(self, object):
        self.children.append(object)

    def render(self, screen):
        for child in self.children:
            child.render(screen)


class FoodStandGrid(Grid):
    def __init__(self, grid):
        super().__init__(grid)
        (x, y) = self.grid_padding
        self.add_object(Text(self.grid.name, 'Small', x + BoxSize / 2, y + BoxSize / 2)),
        self.add_object(Text(str(self.grid.price.buy), 'Small', x + BoxSize / 2, y + BoxSize * 3 / 4))


class EffectGrid(Grid):
    def __init__(self, grid):
        super().__init__(grid)
        (x, y) = self.grid_padding
        self.add_object(Text('Effect', 'Small', x + BoxSize / 2, y + BoxSize / 2))
        self.add_object(Text(self.grid.effect_type, 'Small', x + BoxSize / 2, y + BoxSize * 3 / 4))


class EventGrid(Grid):
    def __init__(self, grid):
        super().__init__(grid)
        (x, y) = self.grid_padding
        self.add_object(Text('抽一張經營卡', 'Small', x + BoxSize / 2, y + BoxSize / 2))


class MainKitchenGrid(Grid):
    def __init__(self, grid):
        super().__init__(grid)
        (x, y) = self.grid_padding
        self.add_object(Text('中央廚房', 'Small', x + BoxSize / 2, y + BoxSize * 1 / 2))
        self.add_object(Text(self.player.name, 'Small', x + BoxSize / 2, y + BoxSize * 2 / 3))

    @property
    def player(self):
        return game.players[self.grid.player_id]

GridClassByType = {
    'FoodStand': FoodStandGrid,
    'Effect': EffectGrid,
    'Event': EventGrid,
    'MainKitchen': MainKitchenGrid,
}


def makeGrid(grid):
    return GridClassByType[grid.type](grid)
