from player import Player
from game import Game
from tile import Tile
from tile import Lever


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
}


def get_movement_input(current_tile) -> str:
    player.display_location()
    print(current_tile)
    move = input("Choose a direction (n/e/s/w): ")
    return move


def main():
    game = Game(player, tiles)
    game.run_game()

    # current_tile = tile_map[player.location]
    # move = get_movement_input(current_tile)
    # while not current_tile.is_valid_move(move):
    #     print("Invalid move")
    #     move = get_movement_input(current_tile)
    # player.move_player(move)
    # player.display_location()


if __name__ == "__main__":
    main()
