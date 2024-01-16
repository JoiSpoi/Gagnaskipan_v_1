from player import Player
from tile import Tile

class Game:
    def __init__(self, player, tiles) -> None:
        """Starts a new game."""
        self.player = player
        self.tiles = tiles
        self.end = (3,1) #If different levels are implemented, can change this to allow various start/end locations.
        return
        
    def run_game(self):
        """Contains main game loop."""
        while self.player.location != self.end:
            print(f"You are at {self.player.location}. You have {self.coins} gold coins.")
            self.player.move_player()
    
