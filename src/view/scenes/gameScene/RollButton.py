import random
from game.game import game
from game.CONST import BoardGridWidth
from util.Dialog import confirm

from ...componentLib.ComponentBase import ComponentBase
from ...CONST import *

l = [6] * 4 + [1] * 100
# l = [1, 2] + [36] * 100
# l = [3] * 4 + [9] * 100
# l = [9] * 100
# l = [1] * 100
l = [36] * 100
# l = [random.choice([9, 18, 27, 36]) for i in range(100)]
# l = [4, 6] + [9] * 100
def get_roll_number():
    # return l.pop(0)
    return random.randint(1, 6) + random.randint(1, 6)


class RollButton(ComponentBase):
    def init(self):
        (width, height) = DefaultScreenSize
        score_board_width = BoxSize * BoardGridWidth
        # self.button = self.children.create_component(
        #     'Button', 'Go', (score_board_width / 2, height / 2), self.roll)
        self.button = self.children.create_component('ImageButton', 'assets/go.png', (score_board_width / 2, height / 2), self.roll, resize=(128, 128), onclick_src='assets/go_pressed.png')
        self.text = self.children.create_component('Text', '', 'Title', center=(score_board_width / 2, height / 2 - 80), color=pygame.Color('white'))

    def roll(self):
        player = game.current_player

        # roll dice animation
        timer = pygame.time.Clock()
        for i in range(40):
            self.text.set_content(random.randint(2, 12))
            self.manager.rerender()
            timer.tick(40)

        # step animation
        step = get_roll_number()
        self.text.set_content(step)
        self.manager.rerender()
        self.manager.scene.players[game.turn].step(step)

        if game.is_end():
            return

        # trigger grid effect
        player.get_grid().trigger(player)

        # handle same spot tech
        for other in game.players:
            if other != player and other.position.get() == player.position.get():
                if player.same_spot_fee != 0:
                    confirm("技術卡效果", f"和 {player.name} 站在同一格的玩家({other.name})要付他 {player.same_spot_fee} 元")
                    game.player_transfer_money(player.id, other.id, player.same_spot_fee)
                if other.same_spot_fee != 0:
                    confirm("技術卡效果", f"和 {other.name} 站在同一格的玩家({player.name})要付他 {other.same_spot_fee} 元")
                    game.player_transfer_money(other.id, player.id, other.same_spot_fee)

        # post round
        self.next_turn()

    def next_turn(self):
        # self.text.set_content('')
        game.next_turn()
        if game.current_player.idle_action > 0:
            game.current_player.idle_action -= 1
            confirm("停止行動", f"{game.current_player.name} 暫停行動一回合...")
            self.next_turn()

    def handle_events(self, events):
        for evt in events:
            if evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_RETURN:
                    self.button.trigger()

        super().handle_events(events)
