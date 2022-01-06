import pygame

from game.game import game
from ...CONST import DefaultScreenSize
from ...componentLib.SceneBase import Scene


class ScoreScene(Scene):
    screen_size = (800, 800)
    
    def __init__(self):
        super().__init__('score')

    def init(self):
        (width, height) = self.screen_size
        self.children.create_component('Image', 'assets/score_background.png', resize=self.screen_size, center=(width / 2, height / 2))
        self.children.create_component('Text', '遊戲結束!', 'Title', center=(width / 2, (height - 80 * len(game.players)) / 2 - 35), color=pygame.Color('white'))
        players = game.players.copy()
        sorted_scores = sorted([p.get_score_total() for p in players], reverse=True)
        ranks = [sorted_scores.index(p.get_score_total()) for p in players]
        for i, player in enumerate(sorted(game.players, key=lambda p: p.get_score_total(), reverse=True)):
            self.children.create_component('PlayerScore', player.id, i, ranks[player.id])
