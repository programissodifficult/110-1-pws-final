import pygame

class Character():
    def __init__(self, name, color, color_light, ability, ability_description):
        self.name = name
        self.color = color
        self.color_light = color_light
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
    Character('丁丁', pygame.Color('blue'), pygame.Color('lightblue'), build_discount_300, "每次建造桌子時可以少花 300 元"),
    Character('小波', pygame.Color('red'), pygame.Color('pink'), redraw_event, "每次抽經營卡時，可以選擇重抽一張"),
    Character('迪西', pygame.Color('green'), pygame.Color('lightgreen'), event_bonus_500, "每次抽經營卡時可獲得 500 元"),
    Character('拉拉', pygame.Color('yellow'), pygame.Color('lightgoldenrodyellow'), invent_discount_900, "研發技術時只需支付 3100 元"),
]