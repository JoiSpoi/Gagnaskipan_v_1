from tile import Tile
from player import Player
from game import Game


player = Player((1, 1))
tiles = {
    (1, 1): Tile(["n"]),
    (2, 1): Tile(["n"]),
    (3, 1): Tile(["n"]),
    (1, 2): Tile(["n", "a", "s"]),
    (2, 2): Tile(["w", "s"]),
    (3, 2): Tile(["n", "s"]),
    (1, 3): Tile(["w", "s"]),
    (2, 3): Tile(["w", "a"]),
}

def main():
    game = Game(player, tiles)
    game.run_game()

if __name__ == "__main__":
    main()
