from ...CONST import *

player_paddings = [
    (PlayerBorderPadding, PlayerBorderPadding),
    (GridSize - PlayerBorderPadding, PlayerBorderPadding),
    (PlayerBorderPadding, GridSize - PlayerBorderPadding),
    (GridSize - PlayerBorderPadding, GridSize - PlayerBorderPadding),
]

def grid_coord(pos, player_id = None):
    line = pos.line
    offset = pos.offset
    if line == 0:
        x = GridSize * offset
        y = GridSize * 0
    elif line == 1:
        x = GridSize * 9
        y = GridSize * offset
    elif line == 2:
        x = GridSize * (9 - offset)
        y = GridSize * 9
    else:
        x = GridSize * 0
        y = GridSize * (9 - offset)
    if not player_id == None:
        x += player_paddings[player_id][0]
        y += player_paddings[player_id][1]

    return x, y
