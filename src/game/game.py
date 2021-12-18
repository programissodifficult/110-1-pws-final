import pygame
from .lib.EffectGrid import EffectGrid
from .lib.EventGrid import EventGrid
from .lib.FoodStand import FoodStand

from .lib.Player import Player
from .lib.MainKitchen import MainKitchen

class Game:
    def __init__(self):
        self.grids = [
            MainKitchen(0, 0),
            FoodStand(1, "珍珠奶茶", 2),
            FoodStand(2, "臭豆腐", 0),
            EffectGrid(3, "fee"),
            FoodStand(4, "牛肉麵", 3),
            FoodStand(5, "八寶冰", 0),
            EventGrid(6),
            FoodStand(7, "鹹酥雞", 1),
            FoodStand(8, "鱔魚麵", 2),
            MainKitchen(9, 1),
            FoodStand(10, "滷肉飯", 2),
            FoodStand(11, "仙草芋圓", 0),
            EffectGrid(12, "switch"),
            FoodStand(13, "大腸包小腸", 3),
            FoodStand(14, "魷魚羹", 0),
            EventGrid(15),
            FoodStand(16, "木瓜牛奶", 1),
            FoodStand(17, "鼎邊銼", 2),
            MainKitchen(18, 2),
            FoodStand(19, "四神湯", 2),
            FoodStand(20, "筒仔米糕", 0),
            EffectGrid(21, "rest"),
            FoodStand(22, "當歸麵線", 3),
            FoodStand(23, "棺材板", 0),
            EventGrid(24),
            FoodStand(25, "潤餅", 1),
            FoodStand(26, "蚵仔煎", 2),
            MainKitchen(27, 3),
            FoodStand(28, "甜不辣", 2),
            FoodStand(29, "小籠包", 0),
            EffectGrid(30, "rest"),
            FoodStand(31, "切仔麵", 3),
            FoodStand(32, "羊肉爐", 0),
            EventGrid(33),
            FoodStand(34, "肉圓", 1),
            FoodStand(35, "薑母鴨", 2),
        ]

    def init(self, player_amount):
        self.players = [
            Player(0, pygame.Color('blue')),
            Player(1, pygame.Color('red')),
            Player(2, pygame.Color('green')),
            Player(3, pygame.Color('yellow'))
        ][:player_amount]

game = Game()