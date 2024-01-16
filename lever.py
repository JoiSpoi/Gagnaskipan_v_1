class Lever:
    def __init__(self) -> None:
        self.is_pulled = False
        self.coins = 1

    def pull(self) -> int:
        if self.is_pulled:
            return 0

        self.is_pulled = True
        return self.coins