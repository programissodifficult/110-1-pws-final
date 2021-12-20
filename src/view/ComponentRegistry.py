from .scenes.basicComponents.Text import Text
from .scenes.basicComponents.Button import Button
from .scenes.basicComponents.Circle import Circle
from .scenes.basicComponents.Rectangle import Rectangle

from .scenes.gameScene import Grid
from .scenes.gameScene import Player


ComponentRegistry = {
    "Text": Text,
    "Button": Button,
    "Circle": Circle,
    "Rectangle": Rectangle,
    "Grid": Grid,
    "Player": Player
}