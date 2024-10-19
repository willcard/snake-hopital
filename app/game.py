import conf
from grid import Grid

class Game:
    def __init__(self) -> None:
        self.grid = Grid(*conf.GRID_SHAPE)
        print(self.grid.pretty_print())

    def run(self, move) -> None:
        self.grid.snake_move(move)
        if self.grid.snake_eat_apple():
            print('< apple touched >')
        print(self.grid.pretty_print())