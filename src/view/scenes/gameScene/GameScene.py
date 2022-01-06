from game.game import game
from util.help import help
from ...componentLib.SceneBase import Scene
from ...CONST import *

GridClassByType = {
    'FoodStand': 'FoodStandGrid',
    'Effect': 'EffectGrid',
    'Event': 'EventGrid',
    'MainKitchen': 'MainKitchenGrid',
}


class GameScene(Scene):
    def __init__(self):
        super().__init__('game')
        self.grids = []
        self.players = []

    def init(self, player_amount):
        game.init(player_amount)

        img_size = (GridSize * 8, GridSize * 8)
        img_center = (GridSize * 5, GridSize * 5)
        self.children.create_component('Image', 'assets/background.png', resize=img_size, center=img_center)

        help_button_center = (GridSize + 60, GridSize + 60)
        self.children.create_component('ImageButton', 'assets/question.png', help_button_center, help, resize=(96, 96), onclick_src='assets/question_pressed.png')

        for grid in game.grids:
            grid_comp = self.children.create_component(GridClassByType[grid.type], grid)
            self.grids.append(grid_comp)

        for player in game.players:
            player_comp = self.children.create_component('Player', player.id)
            self.players.append(player_comp)

        for player in game.players:
            self.children.create_component('ScoreBoard', player.id)

        self.children.create_component('RollButton')
