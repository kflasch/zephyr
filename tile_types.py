from typing import Tuple

import numpy

# tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = numpy.dtype([
    ("ch", numpy.int32), # Unicode codepoint
    ("fg", "3B"), # 3 unsigned bytes, for RGB colors
    ("bg", "3B"),
])

# tile struct used for statically defined tile data
tile_dt = numpy.dtype([
    ("walkable", numpy.bool), # true if this tile can be walked through
    ("transparent", numpy.bool), # true if this tile doesn't block FOV
    ("dark", graphic_dt), # graphics for when this tile is not in FOV
    ("light", graphic_dt), # graphics for when this tile is in FOV
])

def new_tile(*, walkable: int, transparent: int,
             dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
             light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]) -> numpy.ndarray:
    """ Helper fn for defining individual tile types """
    return numpy.array((walkable, transparent, dark, light), dtype=tile_dt)

# represents unexplored, unseen tiles
SHROUD = numpy.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True, transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50)))

wall = new_tile(
    walkable=False, transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
    light=(ord(" "), (255, 255, 255), (130, 110, 50)))
