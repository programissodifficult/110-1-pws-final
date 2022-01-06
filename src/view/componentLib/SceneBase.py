from ..CONST import BackgroundColor, DefaultScreenSize
from .ComponentBase import ComponentBase

class Scene(ComponentBase):
    screen_size = DefaultScreenSize

    def __init__(self, name, background_color=BackgroundColor):
        super().__init__()
        self.name = name
        self.background_color = background_color
        self.scene = self
