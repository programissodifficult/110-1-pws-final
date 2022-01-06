import pygame

class Character():
    def __init__(self, name, color, color_secondary, ability, ability_description):
        self.name = name
        self.color = color
        self.color_secondary = color_secondary
        self.init_ability = ability
        self.ability_description = ability_description


def invent_discount_900(player):
    player.invent_discount += 900

def redraw_event(player):
    player.redraw_chance.append('主廚能力')

def event_bonus_500(player):
    player.event_bonus += 500

def build_discount_300(player):
    player.build_discount += 300

characters = [
    Character('丁丁', (0, 128, 255), pygame.Color('lightblue'), build_discount_300, "每次建造桌子時可以少花 300 元"),
    Character('小波', pygame.Color('red'), pygame.Color('pink'), redraw_event, "每次抽經營卡時，可以選擇重抽一張"),
    Character('迪西', pygame.Color('green'), pygame.Color('lightgreen'), event_bonus_500, "每次抽經營卡時可獲得 500 元"),
    Character('拉拉', pygame.Color('yellow'), (255, 255, 120), invent_discount_900, "研發技術時只需支付 3100 元"),
]