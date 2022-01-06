from os import path

from game.game import game
from game.CONST import *
from game.lib.Character import characters
from util.Dialog import confirm

from ...util.cursor import use_default_cursor, use_hand_cursor
from ...CONST import *
from ...componentLib.ComponentBase import ComponentBase

from .gridHelper import grid_coord


class Grid(ComponentBase):
    def init(self, grid):
        self.id = grid.id
        self.border = self.children.create_component('Rectangle', GridSize, GridSize, *grid_coord(self.id), BorderColor)

    def show_info(self):
        pass

    @property
    def grid(self):
        return game.grids[self.id]

    @property
    def grid_padding(self):
        return grid_coord(self.id)

    def handle_events(self, events):
        x, y = pygame.mouse.get_pos()

        for evt in events:
            if evt.type == pygame.MOUSEMOTION:
                if self.border.get_rect().collidepoint(*pygame.mouse.get_pos()):
                    self.border.color = pygame.Color('white')
                    use_hand_cursor()
                else:
                    self.border.color = BorderColor

            if evt.type == pygame.MOUSEBUTTONDOWN:
                if self.border.get_rect().collidepoint(x, y):
                    use_default_cursor()
                    self.show_info()

        super().handle_events(events)

deco = ['', '+', '++', '*']

class FoodStandGrid(Grid):
    def init(self, grid):
        super().init(grid)
        (x, y) = self.grid_padding
        self.inner_border = self.children.create_component('Rectangle', GridSize - 4, GridSize - 4, x + 2, y + 2, BackgroundColor)
        self.inner_border.disabled = True
        self.background = self.children.create_component('Rectangle', GridSize, GridSize, x, y, BackgroundColor, border_width=0, first=True)
        self.name_label = self.children.create_component('Text', self.grid.name, 'Small', center=(x + GridSize / 2, y + 15))
        self.text_level = self.children.create_component('Text', '', 'Small', bottomright=(x + GridSize - 5, y + GridSize - 5))
        self.children.create_component('Image', path.join(ImageFolder, f'{grid.name}.png'), center=(
            x + GridSize / 2, y + GridSize * 2 / 3), resize=(50, 50))

    def update(self):
        if self.grid.owner != None:
            self.name_label.color = self.grid.owner.color_secondary
            self.inner_border.color = self.grid.owner.color_secondary
            self.inner_border.disabled = False
            self.text_level.color = self.grid.owner.color_secondary
            # self.text_level.set_content(deco[self.grid.level])
            self.text_level.set_content(f'+{self.grid.level}' if self.grid.level else '')

    def show_info(self):
        self.grid.show_info()


class EffectGrid(Grid):
    def init(self, grid):
        super().init(grid)
        (x, y) = self.grid_padding
        self.background = self.children.create_component('Rectangle', GridSize, GridSize, x, y, BackgroundColor, border_width=0, first=True)
        # self.children.create_component('Text', '效果', 'Small', center=(x + BoxSize / 2, y + BoxSize / 3))
        self.children.create_component('Text', self.grid.name, 'Small', center=(x + GridSize / 2, y + GridSize / 2))

    def show_info(self):
        confirm('效果格', f'停留此處將觸發效果"{self.grid.name}"：\n{self.grid.effect_description}')


class EventGrid(Grid):
    def init(self, grid):
        super().init(grid)
        (x, y) = self.grid_padding
        self.background = self.children.create_component('Rectangle', GridSize, GridSize, x, y, BackgroundColor, border_width=0, first=True)
        self.children.create_component('Text', '經營卡', 'Small', center=(x + GridSize / 2, y + GridSize / 2))

    def show_info(self):
        confirm('經營卡格', '停留此處將觸發隨機事件')


class MainKitchenGrid(Grid):
    def init(self, grid):
        super().init(grid)
        (x, y) = self.grid_padding
        self.character = characters[grid.character_id]
        self.background = self.children.create_component('Rectangle', GridSize, GridSize, x, y, BackgroundColor, border_width=0, first=True)
        self.children.create_component('Text', '中央廚房', 'Small', self.character.color_secondary, center=(x + GridSize / 2, y + GridSize / 3))
        self.children.create_component('Text', self.character.name, 'Small', self.character.color_secondary,
                                       center=(x + GridSize / 2, y + GridSize * 2 / 3))

    def show_info(self):
        confirm('中央廚房格', f'停留此處需支付參觀費 200 元給主廚 {self.character.name}')
