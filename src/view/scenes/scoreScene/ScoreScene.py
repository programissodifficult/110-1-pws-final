from game.game import game
from ...CONST import ScreenSize
from ...componentLib.SceneBase import Scene


class ScoreScene(Scene):
    def __init__(self):
        super().__init__('score')

    def init(self):
        self.children.create_component('Text', '遊戲結束!', 'Title', center=(ScreenSize[0] / 2, (ScreenSize[1] - 80 * len(game.players)) / 2 - 35))
        players = game.players.copy()
        sorted_scores = sorted([p.get_score_total() for p in players], reverse=True)
        ranks = [sorted_scores.index(p.get_score_total()) for p in players]
        for i, player in enumerate(sorted(game.players, key=lambda p: p.get_score_total(), reverse=True)):
            self.children.create_component('PlayerScore', player.id, i, ranks[player.id])
