from player import Player
from tile import Tile

class Game:
    def __init__(self) -> None:
        pass

    def start_game(self):
        """Starts a new game, setting player position to 1,1 and coins to 0."""
        self.player = Player((1,1))
        self.player.coins = 0
        self.end = (3,1) #Can be modified later when multiple levels are implemented.
        return
        
    def run_game(self):
        """Contains main game loop."""
        while self.player.location != self.end:
            print(f"You are at {self.player.location}. You have {self.coins} gold coins.")
            self.player.move_player()
    
