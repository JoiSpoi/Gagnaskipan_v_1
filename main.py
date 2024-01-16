from player import Player
from game import Game
from tile import Tile


player = Player((1, 1))
tiles = {
    (1, 1): Tile(["n"]),
    (2, 1): Tile(["n"]),
    (3, 1): Tile(["n"]),
    (1, 2): Tile(["n", "e", "s"]),
    (2, 2): Tile(["w", "s"]),
    (3, 2): Tile(["n", "s"]),
    (1, 3): Tile(["e", "s"]),
    (2, 3): Tile(["w", "e"]),
    (3, 3): Tile(["w", "s"])
}


def main():
    game = Game(player, tiles)
    game.run_game()


if __name__ == "__main__":
    main()
