from player import Player

class Game:
    def __init__(self) -> None:
        pass

    def start_game(self):
        """Starts a new game, setting player position to 1,1 and coins to 0."""
        self.player = Player((1,1))
        self.player.coins = 0
        self.end = (3,1)
        return
    
    def run_game(self):
        """Contains main game loop."""
        while self.player.location != self.end:
            pass
    

