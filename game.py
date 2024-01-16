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
            current_tile = self.tiles[self.player.location]

            self.player.display_state()
            print(current_tile)

            move = input()
            if current_tile.is_valid_move(move):
                self.player.move_player(move)
            else:
                print("Not a valid direction!")

        if self.player.location == self.end:
            print(f"Congratulations! You've reached the victory tile with {self.player.coins} gold coins!")