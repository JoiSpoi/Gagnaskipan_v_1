from player import Player
from tile import Tile

class Game:
    def __init__(self, player: Player, tiles: dict[tuple, Tile]) -> None:
        """Starts a new game."""
        self.player = player
        self.tiles = tiles
        self.end = (3,1) #If different levels are implemented, can change this to allow various start/end locations.
        return
        
    def run_game(self):
        """Contains main game loop."""
        while self.player.location != self.end:
            current_tile = self.tiles[self.player.location]

            if current_tile.has_active_lever():
                print("You see a lever.")
                if input("PULL LEVER? (y/n): ").lower() == 'y':
                    added_coins = current_tile.lever.pull()
                    self.player.coins += added_coins
                    print(f"You received {added_coins} gold coins!")

            self.player.display_state()
            print(current_tile)

            move = input()
            if current_tile.is_valid_move(move):
                self.player.move_player(move)
            else:
                print("Not a valid direction!")

        if self.player.location == self.end:
            print(f"Congratulations! You've reached the victory tile with {self.player.coins} gold coins!")