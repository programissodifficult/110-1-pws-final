from .scenes.basicComponents.Text import Text
from .scenes.basicComponents.Button import Button
from .scenes.basicComponents.Circle import Circle
from .scenes.basicComponents.Rectangle import Rectangle
from .scenes.basicComponents.Image import Image
from .scenes.basicComponents.ImageButton import ImageButton

from .scenes.gameScene.RollButton import RollButton
from .scenes.gameScene.ScoreBoard import ScoreBoard
from .scenes.gameScene.Grid import FoodStandGrid, EventGrid, EffectGrid, MainKitchenGrid
from .scenes.gameScene.Player import Player

from .scenes.scoreScene.PlayerScore import PlayerScore


ComponentRegistry = {
    # basic
    "Text": Text,
    "Button": Button,
    "Circle": Circle,
    "Rectangle": Rectangle,
    "Image": Image,
    "ImageButton": ImageButton,

    # game scene
    "RollButton": RollButton,
    "ScoreBoard": ScoreBoard,
    "FoodStandGrid": FoodStandGrid,
    "EventGrid": EventGrid,
    "EffectGrid": EffectGrid,
    "MainKitchenGrid": MainKitchenGrid,
    "Player": Player,

    # score scene
    "PlayerScore": PlayerScore
}
