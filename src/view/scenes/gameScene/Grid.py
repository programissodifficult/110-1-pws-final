from os import path

from game.game import game
from game.CONST import *

from ...CONST import *
from ...componentLib.ComponentBase import ComponentBase

from .gridHelper import grid_coord


class Grid(ComponentBase):
    def init(self, grid):
        self.id = grid.id
        self.border = self.children.create_component('Rectangle', BoxSize, BoxSize, *grid_coord(self.id), DefaultBoxColor)

    @property
    def grid(self):
        return game.grids[self.id]

    @property
    def grid_padding(self):
        return grid_coord(self.id)


class FoodStandGrid(Grid):
    def init(self, grid):
        super().init(grid)
        (x, y) = self.grid_padding
        self.name_label = self.children.create_component('Text', self.grid.name, 'Small', (x + BoxSize / 2, y + 15))
        self.children.create_component('Text', str(self.grid.prices.buy), 'Small', (x + BoxSize / 2, y + BoxSize - 15))
        self.children.create_component('Image', path.join(ImageFolder, f'{grid.name}.png'), (x + BoxSize / 2, y + BoxSize / 2))


    def update(self):
        self.name_label.content = self.grid.name + (f'({self.grid.level})' if self.grid.level else '')
        if self.grid.owner != None:
            self.border.color = self.grid.owner.color


class EffectGrid(Grid):
    def init(self, grid):
        super().init(grid)
        (x, y) = self.grid_padding
        self.children.create_component('Text', '效果', 'Small', (x + BoxSize / 2, y + BoxSize / 3))
        self.children.create_component('Text', self.grid.name, 'Small', (x + BoxSize / 2, y + BoxSize * 2 / 3))


class EventGrid(Grid):
    def init(self, grid):
        super().init(grid)
        (x, y) = self.grid_padding
        self.children.create_component('Text', '經營卡', 'Small', (x + BoxSize / 2, y + BoxSize / 2))


class MainKitchenGrid(Grid):
    def init(self, grid):
        super().init(grid)
        (x, y) = self.grid_padding
        self.children.create_component('Text', '中央廚房', 'Small', (x + BoxSize / 2, y + BoxSize * 1 / 2))
        self.children.create_component('Text', CharacterNames[self.grid.player_id], 'Small', (x + BoxSize / 2, y + BoxSize * 3 / 4))

    @property
    def player(self):
        return game.players[self.grid.player_id]
