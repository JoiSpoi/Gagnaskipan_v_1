from lever import Lever


class Tile:
    def __init__(self, possible_moves: list[str], lever: Lever | None = None) -> None:
        self.possible_moves = possible_moves
        self.lever = lever

    def is_valid_move(self, move: str) -> bool:
        """Returns True if the move is valid."""
        if not isinstance(move, str):
            raise TypeError(f"expected move argument to be of type str, but got {type(move)}")

        move = move.lower()

        if move not in ["n", "w", "s", "e"]:
            raise ValueError("expected movement to be 'n', 'w', 's', 'e'")

        return move in self.possible_moves

    def has_active_lever(self) -> bool:
        if (self.lever is not None) and not (self.lever.is_pulled):
            return True
        return False

    def __str__(self) -> str:
        return f"Available directions: {', '.join(self.possible_moves).upper()}"
