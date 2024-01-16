from tile import Tile
from player import Player


player = Player((1, 1))
tiles = {
    (1, 1): Tile(['e', 's']),
    (2, 1): Tile(['w', 'e']),
    (3, 1): Tile(['w']),
    (1, 2): Tile(['e']),
    (2, 2): Tile(['w', 'e', 's']),
    (3, 2): Tile(['w', 's']),
    (1, 3): Tile(['e', 's']),
    (2, 3): Tile(['w', 's']),
}

def main():
    ...

if __name__ == "__main__":
    main()
