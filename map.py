from tile import Tile

class Map:
    def __init__(self) -> None:
        self.tiles = {
            (1, 1): Tile(["n"]),
            (2, 1): Tile(["n"]),
            (3, 1): Tile(["n"]),
            (1, 2): Tile(["n", "a", "s"]),
            (2, 2): Tile(["w", "s"]),
            (3, 2): Tile(["n", "s"]),
            (1, 3): Tile(["w", "s"]),
            (2, 3): Tile(["w", "a"]),
        }

    
