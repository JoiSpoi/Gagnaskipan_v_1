class Player:
    def __init__(self, starting_location: tuple[int]) -> None:
        self.location = starting_location

    def move_player(self, movement: str):
        """
        Moves the player based on the given movement str. \n
        Possible moves are: "n", "s", "e", "w".
        """
        movement = movement.lower()
        x, y = self.location
        if movement == "n":
            self.location = (x, y+1)
        elif movement == "s":
            self.location = (x, y-1)
        elif movement == "e":
            self.location = (x+1, y)
        elif movement == "w":
            self.location = (x-1, y)
