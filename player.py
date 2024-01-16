class Player:
    def __init__(self, starting_location: tuple[int]) -> None:
        self.location = starting_location
        self.coins = 0

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

    def display_state(self) -> None:
        print(f"You are at {self.location}. You have {self.coins} gold coins.")