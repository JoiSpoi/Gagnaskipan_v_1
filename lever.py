class Lever:
    def __init__(self) -> None:
        self.is_pulled = False
        self.coins = 1

    def pull(self):
        self.is_pulled = True