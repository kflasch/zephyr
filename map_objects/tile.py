class Tile:
    """
    A tile on a map.
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # by default, if a tile is blocked, it also blocks sight (glass?? etc)
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
