class Game():
    def __init__(self, game_id=None, name=None, price=None, rate=None):
        self.game_id = game_id
        self.name = name
        self.price = price
        self.rate = rate

    def __str__(self):
        return (
                f'Game ID: {self.game_id}, '
                f'Name of the game: {self.name}, '
                f'Price in Dollars: {self.price}, '
                f'Given rate: {self.rate}'
                )

