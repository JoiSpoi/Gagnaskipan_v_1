from player import Player
from tile import Tile

class Game:
    def __init__(self, player: Player, tiles: list[Tile]) -> None:
        """Starts a new game."""
        self.player = player
        self.tiles = tiles
        self.end = (3,1) #If different levels are implemented, can change this to allow various start/end locations.
        return
        
    def run_game(self):
        """Contains main game loop."""
        while self.player.location != self.end:
            possible_moves = self.tiles[self.player.location].possible_moves

            print(f"You are at {self.player.location}. You have {self.player.coins} gold coins.")
            print("Available directions:", end=" ")
            print(*possible_moves, sep=", ")

            move = input()
            if self.tiles[self.player.location].is_valid_move(move):
                self.player.move_player(move)
            else:
                print("Not a valid direction!")