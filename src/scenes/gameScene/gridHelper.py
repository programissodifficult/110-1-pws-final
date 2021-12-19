from ..CONST import *

player_paddings = [
    (PlayerBorderPadding, PlayerBorderPadding),
    (BoxSize - PlayerBorderPadding, PlayerBorderPadding),
    (PlayerBorderPadding, BoxSize - PlayerBorderPadding),
    (BoxSize - PlayerBorderPadding, BoxSize - PlayerBorderPadding),
]

def grid_pos(i, player_id = None):
    line = i // 9
    offset = i % 9
    if line == 0:
        x = BoxSize * offset
        y = BoxSize * 0
    elif line == 1:
        x = BoxSize * 9
        y = BoxSize * offset
    elif line == 2:
        x = BoxSize * (9 - offset)
        y = BoxSize * 9
    else:
        x = BoxSize * 0
        y = BoxSize * (9 - offset)
    if not player_id == None:
        x += player_paddings[player_id][0]
        y += player_paddings[player_id][1]

    return x, y
