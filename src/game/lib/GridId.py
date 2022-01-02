from ..CONST import MapSize


class GridId:
    def __init__(self, pos) -> None:
        self.id = pos % MapSize

    def get(self):
        return self.id

    @property
    def line(self):
        return self.id // 9

    @property
    def offset(self):
        return self.id % 9

    def __add__(self, step):
        if not isinstance(step, int):
            raise TypeError
        else:
            return GridId(self.id + step)

    def __eq__(self, num):
        return self.id == num

    def __str__(self):
        return str(self.id)

    def __index__(self):
        return self.id
