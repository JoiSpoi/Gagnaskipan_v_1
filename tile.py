class Tile:
    def __init__(self, possible_moves: list[str]) -> None:
        self.possible_moves = possible_moves

    def is_valid_move(self, move: str) -> bool:
        """Returns True if the move is valid."""
        if not isinstance(move, str):
            raise TypeError(f"expected move argument to be of type str, but got {type(move)}")
        
        if move not in ["n", "w", "s", "e"]:
            raise ValueError("expected movement to be 'n', 'w', 's', 'e'")

        return move.lower() in self.possible_moves
    
    def __str__(self) -> str:
        return f"Available directions: {', '.join(self.possible_moves).upper()}"