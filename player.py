class Player:
    def __init__(self, starting_location: tuple[int]) -> None:
        self.location = starting_location

    def move_player(self, movement: str):
        ...
