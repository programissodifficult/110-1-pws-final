from .scenes.gameScene.RollButton import RollButton
from .scenes.gameScene.ScoreBoard import ScoreBoard
from .scenes.basicComponents.Text import Text
from .scenes.basicComponents.Button import Button
from .scenes.basicComponents.Circle import Circle
from .scenes.basicComponents.Rectangle import Rectangle

from .scenes.gameScene.Grid import FoodStandGrid, EventGrid, EffectGrid, MainKitchenGrid
from .scenes.gameScene.Player import Player


ComponentRegistry = {
    "Text": Text,
    "Button": Button,
    "Circle": Circle,
    "Rectangle": Rectangle,
    "Player": Player,
    "FoodStandGrid": FoodStandGrid,
    "EventGrid": EventGrid,
    "EffectGrid": EffectGrid,
    "MainKitchenGrid": MainKitchenGrid,
    "ScoreBoard": ScoreBoard,
    "RollButton": RollButton
}