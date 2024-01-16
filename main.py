from player import Player
from game import Game
from tile import Tile
from lever import Lever


player = Player((1, 1))
tiles = {
    (1, 1): Tile(["n"]),
    (2, 1): Tile(["n"]),
    (3, 1): Tile(["n"]),
    (1, 2): Tile(["n", "e", "s"], Lever()),
    (2, 2): Tile(["w", "s"], Lever()),
    (3, 2): Tile(["n", "s"]),
    (1, 3): Tile(["e", "s"]),
    (2, 3): Tile(["w", "e"], Lever()),
    (3, 3): Tile(["w", "s"], Lever())
}


def main():
    game = Game(player, tiles)
    game.run_game()


if __name__ == "__main__":
    main()
