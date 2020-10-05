import numpy
from tcod.console import Console

import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = numpy.full((width, height), fill_value=tile_types.wall, order='F')

        self.visible = numpy.full((width, height), fill_value=False, order='F')
        self.explored = numpy.full((width, height), fill_value=False, order='F')

    def in_bounds(self, x: int, y: int) -> bool:
        """ Return true if x and y are in bounds of this map """
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """ 
        Renders the map. 
        If a tile is in the 'visible' array, then draw it with 'light' color.
        If it isn't, but it's in 'explored', then draw it with 'dark' color.
        Otherwise, default is 'SHROUD'.
        """
        # console.tiles_rgb[0:self.width, 0:self.height] = self.tiles['dark']
        console.tiles_rgb[0:self.width, 0:self.height] = numpy.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD)

